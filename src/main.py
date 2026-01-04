import pandas as pd
from math import radians, cos, sin, asin, sqrt

# =============================
# Load & Clean Dataset
# =============================
df = pd.read_csv("data/data.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# =============================
# State-level Coordinates
# =============================
state_coords = {
    "andhra pradesh": (15.9129, 79.7400),
    "assam": (26.2006, 92.9376),
    "bihar": (25.0961, 85.3131),
    "delhi": (28.7041, 77.1025),
    "goa": (15.2993, 74.1240),
    "gujarat": (22.2587, 71.1924),
    "haryana": (29.0588, 76.0856),
    "himachal pradesh": (31.1048, 77.1734),
    "karnataka": (15.3173, 75.7139),
    "kerala": (10.8505, 76.2711),
    "madhya pradesh": (22.9734, 78.6569),
    "maharashtra": (19.7515, 75.7139),
    "punjab": (31.1471, 75.3412),
    "rajasthan": (27.0238, 74.2179),
    "tamil nadu": (11.1271, 78.6569),
    "uttar pradesh": (26.8467, 80.9462),
    "uttarakhand": (30.0668, 79.0193),
    "west bengal": (22.9868, 87.8550),
}

# =============================
# Distance Function
# =============================
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return 6371 * (2 * asin(sqrt(a)))

def safe_normalize(series):
    if series.max() == series.min():
        return 1
    return (series - series.min()) / (series.max() - series.min())

# =============================
# Recommendation Engine
# =============================
def recommend_places(source_state, top_n=5):
    source_state = source_state.lower()

    if source_state not in state_coords:
        raise ValueError("Source state not supported.")

    src_lat, src_lon = state_coords[source_state]

    df["distance_km"] = df["state"].str.lower().apply(
        lambda s: haversine(
            src_lat, src_lon,
            *state_coords.get(s, (src_lat, src_lon))
        )
    )

    df["rating_score"] = safe_normalize(df["google_review_rating"])
    df["popularity_score"] = safe_normalize(df["number_of_google_review_in_lakhs"])
    df["distance_score"] = 1 - safe_normalize(df["distance_km"])

    df["final_score"] = (
        0.45 * df["distance_score"] +
        0.35 * df["rating_score"] +
        0.20 * df["popularity_score"]
    )

    return (
        df.sort_values("final_score", ascending=False)
          .head(top_n)[["name", "city", "state", "distance_km", "final_score"]]
    )

# =============================
# Run
# =============================
if __name__ == "__main__":
    state = input("Enter source state: ")
    print(recommend_places(state))
