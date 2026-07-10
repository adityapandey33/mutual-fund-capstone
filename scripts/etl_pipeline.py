from pathlib import Path
import sqlite3
import pandas as pd

BASE = Path(__file__).resolve().parent.parent
RAW = BASE / "data" / "processed"
DB_PATH = RAW / "bluestock_mf.db"

FILE_STEMS = {
    "fund_master": "01_fund_master_cleaned",
    "nav_history": "02_nav_history_cleaned",
    "aum_by_fund_house": "03_aum_by_fund_house",
    "monthly_sip_inflows": "04_monthly_sip_inflows",
    "category_inflows": "05_category_inflows",
    "industry_folio_count": "06_industry_folio_count",
    "scheme_performance": "07_scheme_performance_cleaned",
    "investor_transactions": "08_investor_transactions_cleaned",
    "portfolio_holdings": "09_portfolio_holdings",
    "benchmark_indices": "10_benchmark_indices",
}

POSSIBLE_EXTENSIONS = [".csv", ".xlsx", ".xls"]

def resolve_file(stem: str) -> Path:
    for ext in POSSIBLE_EXTENSIONS:
        path = RAW / f"{stem}{ext}"
        if path.exists():
            return path
    raise FileNotFoundError(f"Missing file for stem: {stem}")

def load_sheet(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    raise ValueError(f"Unsupported file type: {path}")

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out.columns = [
        str(c).strip().lower().replace(" ", "_").replace("-", "_")
        for c in out.columns
    ]
    return out

def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    try:
        for table_name, stem in FILE_STEMS.items():
            path = resolve_file(stem)
            df = normalize_columns(load_sheet(path))
            df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.commit()
        print(f"Database created/updated at: {DB_PATH}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()