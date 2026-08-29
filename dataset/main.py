import pandas as pd

df = pd.read_csv("student_performance.csv")

print(df.head())
print(df.shape)
df.info()
# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

import matplotlib.pyplot as plt
import seaborn as sns

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Final Score Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Final_Score"], bins=20, kde=True)
plt.title("Final Score Distribution")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.show()

# Attendance vs Final Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Attendance", y="Final_Score", data=df)
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.show()

# Study Hours vs Final Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Study_Hours", y="Final_Score", data=df)
plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Attendance vs Final Score
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Attendance", y="Final_Score")
plt.title("Attendance vs Final Score")
plt.xlabel("Attendance")
plt.ylabel("Final Score")
plt.show()

# Study Hours vs Final Score
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Study_Hours", y="Final_Score")
plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Features (X)
X = df[
    [
        "Age",
        "Attendance",
        "Study_Hours",
        "Previous_Score",
        "Assignment_Score",
        "Midterm_Score"
    ]
]

# Target (Y)
y = df["Final_Score"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

print("Model training completed!")

# Make predictions
y_pred = model.predict(X_test)

# Model Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

# Predict Final Score for a new student

new_student = pd.DataFrame([[
    18,
    85,
    6,
    75,
    80,
    78
]], columns=X.columns)

prediction = model.predict(new_student)

print("\nNew Student Prediction:")
print("Predicted Final Score:", round(prediction[0], 2))

print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)
# Predict scores for all students
df["Predicted_Final_Score"] = model.predict(X)

# Save data for Power BI
df.to_csv("student_performance_predictions.csv", index=False)

print("\nPower BI file created successfully!")