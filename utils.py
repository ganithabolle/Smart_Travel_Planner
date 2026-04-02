import pandas as pd
from pathlib import Path


def load_data():
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "student.csv"

    def default_data():
        return pd.DataFrame([
            {"Place": "Goa", "Location": "India", "Interest": "Beach", "Hotel": "Sea View Resort", "Price": 5000, "Distance": 800, "lat": 15.2993, "lon": 74.1240},
            {"Place": "Manali", "Location": "India", "Interest": "Mountains", "Hotel": "Hill Stay", "Price": 3000, "Distance": 1200, "lat": 32.2432, "lon": 77.1892},
            {"Place": "Delhi", "Location": "India", "Interest": "City", "Hotel": "Grand Hotel", "Price": 4000, "Distance": 500, "lat": 28.7041, "lon": 77.1025},
            {"Place": "Rishikesh", "Location": "India", "Interest": "Adventure", "Hotel": "River Camp", "Price": 2500, "Distance": 300, "lat": 30.0869, "lon": 78.2676},
            {"Place": "Mumbai", "Location": "India", "Interest": "City", "Hotel": "Luxury Inn", "Price": 6000, "Distance": 700, "lat": 19.0760, "lon": 72.8777},
            {"Place": "Pondicherry", "Location": "India", "Interest": "Beach", "Hotel": "Ocean Bliss", "Price": 4500, "Distance": 600, "lat": 11.9416, "lon": 79.8083},
            {"Place": "Ooty", "Location": "India", "Interest": "Mountains", "Hotel": "Green Valley", "Price": 3500, "Distance": 900, "lat": 11.4102, "lon": 76.6950},
            {"Place": "Jaipur", "Location": "India", "Interest": "City", "Hotel": "Royal Palace", "Price": 3800, "Distance": 550, "lat": 26.9124, "lon": 75.7873}
        ])

    if not csv_path.exists() or csv_path.stat().st_size == 0:
        # fallback to default dataset if missing/empty
        return default_data()

    try:
        df = pd.read_csv(csv_path)
    except pd.errors.EmptyDataError:
        return default_data()

    if df.empty or df.columns.empty:
        return default_data()

    return df