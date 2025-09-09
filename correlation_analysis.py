
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

def find_correlation(datafile):
    df = pd.read_csv(datafile)
    X = df[["temperature", "salinity"]]
    y = df["species_diversity"]
    model = RandomForestRegressor().fit(X, y)
    print("Top feature importances:", model.feature_importances_)

if __name__ == "__main__":
    find_correlation("marine_combined.csv")
