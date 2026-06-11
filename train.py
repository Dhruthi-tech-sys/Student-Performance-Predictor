import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("data/student_data.csv")

X = df[["study_hours", "attendance", "previous_score"]]
y = df["final_score"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model/student_model.pkl")

print("Model trained successfully!")
