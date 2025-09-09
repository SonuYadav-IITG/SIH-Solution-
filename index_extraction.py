
def calculate_indices(nir, red):
    ndvi = (nir - red) / (nir + red + 1e-6)
    print(f"NDVI: {ndvi}")

if __name__ == "__main__":
    calculate_indices(0.66, 0.36)
