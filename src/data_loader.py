import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """
    Load wine quality dataset from the given path.
    """
    try:
        df = pd.read_csv(path)
        print(f"Data loaded successfully with shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Test when running directly
if __name__ == "__main__":
    df = load_data("data/winequality-red.csv")
    print(df.head())
