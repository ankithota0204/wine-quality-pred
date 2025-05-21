# 🍷 Wine Quality Prediction

A machine learning project that predicts wine quality based on physicochemical tests using a Random Forest model. The project includes MLflow tracking and CI/CD with GitHub Actions.

---

## 🚀 Features

- Predict wine quality from features like acidity, alcohol, etc.
- Tracks experiments with MLflow
- Automated training and validation via CI/CD
- Well-organized modular codebase

---

## 🧪 Tech Stack

- Python
- Scikit-learn
- Pandas, NumPy
- MLflow
- Git & GitHub Actions (CI/CD)
- VS Code

---

## 🗂️ Project Structure

├── .github/workflows/ # CI/CD pipeline
├── data/ # Dataset (winequality-red.csv)
├── src/ # Source code
│ ├── data_loader.py
│ └── train.py
├── requirements.txt
├── README.md
└── mlruns/ # MLflow logs (ignored by Git)


---

## 🏃‍♂️ How to Run

1. Clone the repo
2. Install dependencies:

```bash
pip install -r requirements.txt
