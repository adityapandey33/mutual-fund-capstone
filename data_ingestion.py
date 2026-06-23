from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
RAW = BASE / "data" / "raw"
FILES = sorted(RAW.glob("*.csv"))

for file in FILES:
    df = pd.read_csv(file)
    print(f"\n=== {file.name} ===")
    print("shape:", df.shape)
    print("dtypes:\n", df.dtypes)
    print("head:\n", df.head())

    unnamed = [c for c in df.columns if str(c).startswith("Unnamed")]
    if unnamed:
        print("anomaly: unnamed columns", unnamed)

    nulls = df.isna().sum()
    nulls = nulls[nulls > 0]
    if not nulls.empty:
        print("anomaly: missing values", nulls.sort_values(ascending=False).head(5).to_dict())