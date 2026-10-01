import streamlit as st
import pandas as pd
import joblib

# Page settings
st.set_page_config(
    page_title="Student Exam Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Load trained models
regression_model = joblib.load("regression_model.pkl")
classification_model = joblib.load("classification_model.pkl")
scaler = joblib.load("classification_scaler.pkl")


# Prediction function
def predict_performance(
    attendance,
    assignment,
    participation,
    study_hours,
    previous_exam,
    practice_tests,
    sleep_hours
):
    data = pd.DataFrame([{
        "Attendance_Percent": attendance,
        "Assignment_Score": assignment,
        "Participation_Score": participation,
        "Study_Hours": study_hours,
        "Previous_Exam_Score": previous_exam,
        "Practice_Tests": practice_tests,
        "Sleep_Hours": sleep_hours
    }])

    # Regression
    predicted_marks = regression_model.predict(data)[0]

    # Classification
    scaled_data = scaler.transform(data)
    predicted_category = classification_model.predict(
        scaled_data
    )[0]

    return predicted_marks, predicted_category


# Title
st.title("🎓 Student Exam Performance Prediction System")

st.write(
    "Predict a student's final exam marks and performance category "
    "using Machine Learning."
)

st.divider()


# Student inputs
st.header("📝 Student Information")

col1, col2 = st.columns(2)

with col1:

    attendance = st.number_input(
        "Attendance Percentage",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=1.0
    )

    assignment = st.number_input(
        "Assignment Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )

    participation = st.number_input(
        "Participation Score",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0
    )

    study_hours = st.number_input(
        "Study Hours per Day",
        min_value=1.0,
        max_value=10.0,
        value=5.0,
        step=0.5
    )


with col2:

    previous_exam = st.number_input(
        "Previous Exam Score",
        min_value=0.0,
        max_value=100.0,
        value=65.0,
        step=1.0
    )

    practice_tests = st.number_input(
        "Practice Tests",
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )

    sleep_hours = st.number_input(
        "Sleep Hours per Day",
        min_value=5.0,
        max_value=9.0,
        value=7.0,
        step=0.5
    )


# Prediction
st.divider()

if st.button(
    "🚀 Predict Performance",
    use_container_width=True
):

    marks, category = predict_performance(
        attendance,
        assignment,
        participation,
        study_hours,
        previous_exam,
        practice_tests,
        sleep_hours
    )

    st.header("📊 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Predicted Final Exam Score",
            f"{marks:.2f}"
        )

    with col2:
        st.metric(
            "Performance Category",
            category
        )


# What-if analysis
st.divider()

st.header("🔄 What-If Analysis")

st.write(
    "Change study hours or attendance and compare "
    "the new prediction with the current scenario."
)

what_if_study = st.slider(
    "What if Study Hours change to:",
    min_value=1.0,
    max_value=10.0,
    value=study_hours,
    step=0.5
)

what_if_attendance = st.slider(
    "What if Attendance changes to:",
    min_value=0.0,
    max_value=100.0,
    value=attendance,
    step=1.0
)


if st.button(
    "🔍 Compare Scenarios",
    use_container_width=True
):

    current_marks, current_category = predict_performance(
        attendance,
        assignment,
        participation,
        study_hours,
        previous_exam,
        practice_tests,
        sleep_hours
    )

    new_marks, new_category = predict_performance(
        what_if_attendance,
        assignment,
        participation,
        what_if_study,
        previous_exam,
        practice_tests,
        sleep_hours
    )

    st.subheader("Scenario Comparison")

    comparison = pd.DataFrame({
        "Scenario": ["Current", "What-If"],
        "Study Hours": [
            study_hours,
            what_if_study
        ],
        "Attendance": [
            attendance,
            what_if_attendance
        ],
        "Predicted Marks": [
            round(current_marks, 2),
            round(new_marks, 2)
        ],
        "Performance": [
            current_category,
            new_category
        ]
    })

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    difference = new_marks - current_marks

    st.metric(
        "Change in Predicted Marks",
        f"{difference:+.2f}"
    )