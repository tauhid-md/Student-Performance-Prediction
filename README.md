# Student Exam Performance Prediction System

## 📌 Project Overview

The Student Exam Performance Prediction System is a Machine Learning project designed to predict a student's final exam performance using academic, study, and participation-related factors.

The project uses both Regression and Classification techniques to analyze student performance.

A simple Streamlit web application is also developed to allow users to enter student details and get predictions.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Predict the student's Final Exam Score.
- Classify students into different performance categories.
- Compare multiple Machine Learning algorithms.
- Evaluate model performance using different evaluation metrics.
- Save trained Machine Learning models for future predictions.
- Provide a simple and interactive Streamlit application.
- Perform What-If Analysis.
- Compare different student scenarios.

---

## 🔄 Project Workflow

The complete project follows this workflow:

Student Dataset
↓
Data Cleaning
↓
Exploratory Data Analysis (EDA)
↓
Feature Engineering
↓
Regression + Classification
↓
Model Evaluation
↓
Best Model Selection
↓
Model Saving
↓
Streamlit Application
↓
Prediction
↓
What-If Analysis
↓
Scenario Comparison

---

## 📊 Dataset

The dataset contains information related to students' academic performance and study habits.

### Features Used

- Attendance_Percent
- Assignment_Score
- Participation_Score
- Study_Hours
- Sleep_Hours
- Practice_Tests
- Previous_Exam_Score

### Target Variable

For Regression:

- Final_Exam_Score

For Classification:

- Performance_Category

---

## 🧹 Data Cleaning

The dataset was checked and prepared before applying Machine Learning algorithms.

The data cleaning process included:

- Checking for missing values
- Checking duplicate records
- Checking data types
- Removing unnecessary columns
- Preparing features and target variables
- Checking the final dataset structure

After cleaning, the dataset contained:

- 10,000 records
- No missing values
- 7 input features for prediction

---

## 📈 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the dataset and identify relationships between different features.

The following libraries were used for EDA:

- Pandas
- NumPy
- Matplotlib
- Seaborn

EDA was used to analyze:

- Feature distributions
- Relationships between variables
- Correlation between features
- Student performance patterns
- Target variable distribution

---

## ⚙️ Feature Engineering

Feature engineering was performed to prepare the data for Machine Learning models.

The selected academic and study-related features were used as input variables.

The final input features were:

1. Attendance Percentage
2. Assignment Score
3. Participation Score
4. Study Hours
5. Sleep Hours
6. Practice Tests
7. Previous Exam Score

---

# 🤖 Machine Learning

Two types of Machine Learning tasks were performed in this project:

## 1. Regression

Regression was used to predict the student's numerical Final Exam Score.

### Models Used

#### Linear Regression

Linear Regression was used as a baseline regression model to predict the final exam score.

#### Decision Tree Regressor

Decision Tree Regressor was used to learn non-linear relationships between student features and exam scores.

#### Random Forest Regressor

Random Forest Regressor combines multiple decision trees to improve prediction performance.

---

## 📊 Regression Model Evaluation

The regression models were evaluated using:

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

### Linear Regression Results

- MAE: 8.54
- MSE: 113.32
- RMSE: 10.65
- R² Score: 0.5522

The models were compared using these evaluation metrics to understand their prediction performance.

---

# 2. Classification

Classification was used to categorize students according to their predicted performance.

### Performance Categories

The classification target contains the following categories:

- Poor
- Average
- Good
- Very Good
- Excellent

### Classification Models Used

#### Logistic Regression

Logistic Regression was used as a classification baseline model.

#### Decision Tree Classifier

Decision Tree Classifier was used to classify students based on their academic and study-related features.

#### Random Forest Classifier

Random Forest Classifier was used to improve classification by combining multiple decision trees.

---

## 📊 Classification Model Evaluation

The classification models were evaluated using:

- Accuracy
- F1 Score
- Classification Report

### Logistic Regression Results

- Accuracy: 0.5305
- F1 Score: 0.5222

The classification models were compared based on their evaluation metrics.

---

# 💾 Model Saving

After training, the Machine Learning models were saved using Python's joblib/pickle-based model serialization approach.

The project contains:

- `regression_model.pkl`
- `classification_model.pkl`
- `classification_scaler.pkl`

These saved models are used by the Streamlit application to generate predictions without retraining the models every time.

---

# 🌐 Streamlit Application

A simple Streamlit web application was developed for interacting with the Machine Learning models.

The application allows users to enter student information such as:

- Attendance Percentage
- Assignment Score
- Participation Score
- Study Hours
- Sleep Hours
- Practice Tests
- Previous Exam Score

The application then provides:

- Predicted Final Exam Score
- Predicted Performance Category
- What-If Analysis
- Scenario Comparison

---

# 🔍 What-If Analysis

The What-If Analysis feature allows users to change student inputs and observe how the prediction changes.

For example:

A user can increase:

- Study Hours
- Attendance
- Assignment Score
- Practice Tests

and compare the resulting prediction with the original scenario.

This helps demonstrate how changes in input features can affect the model's prediction.

---

# 🔁 Scenario Comparison

The Scenario Comparison feature allows users to compare different student situations.

For example:

### Scenario 1
- Lower Study Hours
- Average Attendance
- Fewer Practice Tests

### Scenario 2
- Higher Study Hours
- Higher Attendance
- More Practice Tests

The application can then compare the predicted outcomes of both scenarios.

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Data Analysis

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Seaborn

## Machine Learning

- Scikit-learn

## Model Saving

- Joblib
- Pickle

## Web Application

- Streamlit

## Development Tools

- Jupyter Notebook
- Google Colab
- Visual Studio Code
- GitHub

---

# 📁 Project Structure

```text
Student-Performance-Prediction/
│
├── app.py
│
├── regression_model.pkl
│
├── classification_model.pkl
│
├── classification_scaler.pkl
│
├── README.md
│
└── requirements.txt




# How to Run the Project
Step 1: Clone the Repository
git clone https://github.com/tauhid-md/Student-Performance-Prediction.git

Step 2: Open the Project Folder
cd Student-Performance-Prediction

Step 3: Install Required Libraries
pip install -r requirements.txt

Step 4: Run the Streamlit Application
streamlit run app.py

The application will open in the browser.
# Required Libraries
The main Python libraries used in this project are:
numpy
pandas
matplotlib
seaborn
scikit-learn
streamlit
joblib

# Key Learning Outcomes
Through this project, I learned how to:
- Work with a Machine Learning dataset.
- Perform data cleaning.
- Perform Exploratory Data Analysis.
- Understand feature relationships.
- Perform feature engineering.
- Build Regression models.
- Build Classification models.
- Compare Machine Learning algorithms.
- Evaluate model performance.
- Save trained Machine Learning models.
- Load saved models for prediction.
- Build a Streamlit application.
- Implement What-If Analysis.
- Compare different prediction scenarios.
- Upload and manage a Machine Learning project using GitHub.
# Future Improvements
Possible future improvements include:
- Improve model accuracy using better feature engineering.
- Perform hyperparameter tuning.
- Add more student-related features.
- Add advanced Machine Learning algorithms.
- Add Deep Learning models.
- Improve the Streamlit user interface.
- Deploy the application online.
- Add interactive visualizations.
- Add a database for storing predictions.
 $$ Author
Mohammad Tauhid Alam
BSc.IT | AI/ML Student
Interested in:
- Artificial Intelligence
- Machine Learning
- Data Science
- Generative AI
- Python
- AI Projects
** Project
If you find this project useful, you can give the repository a star on GitHub.
Thank you for visiting this project!

**Ab pura content paste → neeche scroll → `Commit changes` → commit message ko `Add README documentation` rakhna → Commit changes.** ✅
