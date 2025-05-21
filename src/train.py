import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from data_loader import load_data
import joblib

def train_model(data_path):
    df = pd.read_csv(data_path,delimiter=";")
    X = df.drop("quality", axis=1)
    y = df["quality"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Start MLflow run
    with mlflow.start_run():
        # Train model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Predict and evaluate
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)

        # Log params and metrics
        mlflow.log_param("n_estimators", 100)
        mlflow.log_metric("mse", mse)

        # Log model
        mlflow.sklearn.log_model(model, "random_forest_model")

        print(f"Training completed. MSE: {mse}")

        # Save model
        joblib.dump(model, "model/wine_quality_model.pkl")
        print("Model saved to model/wine_quality_model.pkl")


if __name__ == "__main__":
    train_model("data/winequality-red.csv")