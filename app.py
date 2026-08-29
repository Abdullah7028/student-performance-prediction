import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Page settings
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Performance Prediction System")
st.write("Predict a student's final score using academic and attendance data.")

# Load dataset
data_path = "dataset/student_performance.csv"
df = pd.read_csv(data_path)

# Features and target
target = "Final_Score"

X = df.drop(columns=[target])
y = df[target]

# Remove ID column if present
if "Student_ID" in X.columns:
    X = X.drop(columns=["Student_ID"])

# Separate categorical and numerical columns
categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
numeric_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

# Model
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ]
)

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

# Sidebar inputs
st.sidebar.header("📝 Student Details")

input_data = {}

for col in numeric_cols:
    min_value = float(df[col].min())
    max_value = float(df[col].max())
    default_value = float(df[col].mean())

    input_data[col] = st.sidebar.number_input(
        col.replace("_", " "),
        min_value=min_value,
        max_value=max_value,
        value=default_value
    )

for col in categorical_cols:
    input_data[col] = st.sidebar.selectbox(
        col.replace("_", " "),
        sorted(df[col].dropna().unique())
    )

# Prediction button
if st.sidebar.button("🔮 Predict Final Score"):

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    st.success(f"### Predicted Final Score: {prediction:.2f}")

    # Performance category
    if prediction >= 80:
        category = "🌟 High Performer"
    elif prediction >= 60:
        category = "👍 Average Performer"
    else:
        category = "⚠️ Low Performer"

    st.info(f"Performance Category: **{category}**")

# Model performance
st.divider()

st.subheader("📊 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("MAE", f"{mae:.2f}")

with col2:
    st.metric("RMSE", f"{rmse:.2f}")

with col3:
    st.metric("R² Score", f"{r2:.4f}")

# Dataset preview
with st.expander("📋 View Dataset"):
    st.dataframe(df.head(20), use_container_width=True)