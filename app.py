import streamlit as st
import joblib

# Page settings
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

# Load model
model = joblib.load("model/student_model.pkl")

# Header
st.title("🎓 Student Performance Predictor")
st.markdown(
    "Predict a student's final score using Machine Learning."
)

st.divider()

# Input section
st.subheader("📊 Enter Student Details")

study_hours = st.slider(
    "Study Hours",
    min_value=0,
    max_value=12,
    value=5
)

attendance = st.slider(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

previous_score = st.slider(
    "Previous Score",
    min_value=0,
    max_value=100,
    value=70
)

st.divider()

# Prediction button
if st.button("🚀 Predict Score", use_container_width=True):

    prediction = model.predict(
        [[study_hours, attendance, previous_score]]
    )[0]

    st.success(
        f"🎯 Predicted Final Score: {prediction:.2f}"
    )

    if prediction >= 85:
        st.balloons()
        st.info("Excellent performance expected!")
    elif prediction >= 70:
        st.info("Good performance expected!")
    else:
        st.warning("Needs more preparation to improve performance.")

# Footer
st.divider()
st.caption("Built using Python, Scikit-Learn and Streamlit")