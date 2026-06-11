# 🎓 Student Performance Predictor

A Machine Learning project that predicts a student's final score based on:

- Study Hours
- Attendance Percentage
- Previous Academic Score

This project demonstrates the complete Machine Learning workflow, including data preprocessing, model training, prediction, and deployment using Streamlit.

---

## 🚀 Features

- Predicts student performance using Machine Learning
- Simple and interactive web interface
- Fast predictions
- Beginner-friendly AI/ML project
- Easy to deploy and extend

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

---

## 📁 Project Structure

```text
student-performance-predictor/
│
├── data/
│   └── student_data.csv
│
├── model/
│   └── student_model.pkl
│
├── app.py
├── train.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset contains:

| Feature | Description |
|----------|-------------|
| study_hours | Number of study hours |
| attendance | Attendance percentage |
| previous_score | Previous exam score |
| final_score | Target value to predict |

Example:

```csv
study_hours,attendance,previous_score,final_score
2,70,60,65
3,75,65,70
4,80,70,75
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/student-performance-predictor.git
cd student-performance-predictor
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model

Run:

```bash
python train.py
```

Output:

```text
Model trained successfully!
```

This generates:

```text
model/student_model.pkl
```

---

## ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📈 How It Works

1. Load student dataset
2. Train a Linear Regression model
3. Save the trained model
4. Accept user inputs
5. Predict final student score

---

## 🔮 Future Improvements

- Larger real-world dataset
- Multiple ML algorithms
- Performance comparison dashboard
- Student analytics visualization
- Cloud deployment
- AI-powered recommendations

---

## 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository and submit pull requests.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Created as a Machine Learning learning project for AI & ML students.# Student-Performance-Predictor