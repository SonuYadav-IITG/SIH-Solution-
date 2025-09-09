
import pandas as pd

def integrate_data(ocean_file, fish_file):
    ocean = pd.read_csv(ocean_file)
    fish = pd.read_csv(fish_file)
    merged = pd.merge(ocean, fish, on="location")
    print("Integrated data shape:", merged.shape)
    return merged

if __name__ == "__main__":
    integrate_data("ocean.csv", "fish.csv")
