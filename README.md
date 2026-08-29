# Student Performance Prediction & Analytics System

A college project that combines **Python, Machine Learning, and Power
BI** to analyze student performance and predict final scores.

## Project Overview

The system uses student academic and behavioral data to predict a
student's **Final Score** using a **Linear Regression** machine learning
model. The generated predictions are then exported to CSV and visualized
in an interactive Power BI dashboard.

## Objectives

-   Analyze student academic performance.
-   Predict Final Score using machine learning.
-   Evaluate the prediction model using MAE, RMSE, and R².
-   Generate predictions for all students.
-   Build an interactive Power BI dashboard for performance analytics.
-   Categorize students into performance groups.

## Technologies Used

-   **Python 3.12**
-   **Pandas** -- data handling and preprocessing
-   **Scikit-learn** -- machine learning and model evaluation
-   **Linear Regression** -- Final Score prediction
-   **Power BI** -- dashboard and data visualization
-   **Git & GitHub** -- version control and project hosting

## Dataset

The dataset contains student performance information such as:

-   Student ID
-   Gender
-   Age
-   Attendance
-   Study Hours
-   Previous Score
-   Assignment Score
-   Midterm Score
-   Final Score

## Machine Learning

The project uses **Linear Regression** to predict `Final_Score`.

### Model Evaluation

  Metric       Result
  ---------- --------
  MAE          1.7426
  RMSE         2.2134
  R² Score     0.9688

An example new-student prediction produced a **Predicted Final Score of
81.36**.

## Power BI Dashboard

The Power BI dashboard includes:

-   Total Students
-   Average Final Score
-   Average Attendance
-   Average Study Hours
-   Final Score by Gender
-   Attendance vs Final Score
-   Study Hours vs Final Score
-   Actual vs Predicted Score
-   Gender-wise filtering
-   Performance Category filtering

### Performance Categories

Students are grouped based on Final Score:

-   **High Performer:** Final Score \>= 80
-   **Average Performer:** Final Score \>= 60 and \< 80
-   **Low Performer:** Final Score \< 60

## Project Structure

``` text
student-performance-prediction/
│
├── dataset/
│   ├── Student_Performance_Analytics.pbix
│   ├── main.py
│   ├── student_performance.csv
│   └── student_performance_predictions.csv
│
└── README.md
```

## How to Run

### 1. Open the project folder

``` text
D:\student_performance
```

### 2. Run the Python program

``` bash
python .\dataset\main.py
```

The program trains the model, evaluates it, predicts a new student's
score, and creates:

``` text
student_performance_predictions.csv
```

### 3. Open the Power BI file

Open:

``` text
Student_Performance_Analytics.pbix
```

in Microsoft Power BI Desktop.

## Results

The Linear Regression model achieved an **R² score of 0.9688**,
indicating a strong relationship between the selected input features and
the Final Score in this dataset.

## Future Scope

-   Try advanced models such as Random Forest and Gradient Boosting.
-   Add more student-related features.
-   Deploy the prediction model as a web application.
-   Add automated model retraining.
-   Create real-time prediction functionality.

## Author

**Abdullah7028**

## License

This project was created for educational/college project purposes.
