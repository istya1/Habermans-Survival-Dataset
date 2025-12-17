import pandas as pd

def load_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/haberman/haberman.data"
    df = pd.read_csv(url, header=None)
    df.columns = [
        "Age",
        "Year_of_Operation",
        "Positive_Axillary_Nodes",
        "Survival_Status"
    ]
    df["Survival_Status"] = df["Survival_Status"].apply(lambda x: 0 if x == 1 else 1)
    return df