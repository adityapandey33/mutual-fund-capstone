from pathlib import Path
import sqlite3
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent.parent
RAW = BASE / 'data' / 'processed'
DB_PATH = RAW / 'bluestock_mf.db'
OUT = BASE / 'output'
OUT.mkdir(exist_ok=True)


def safe_num(s):
    return pd.to_numeric(s, errors='coerce')


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    try:
        nav = pd.read_sql_query('select * from 02_nav_history', conn)
        perf = pd.read_sql_query('select * from 07_scheme_performance', conn)
        holdings = pd.read_sql_query('select * from 09_portfolio_holdings', conn)
        tx = pd.read_sql_query('select * from 08_investor_transactions', conn)
    finally:
        conn.close()

    for df in (nav, perf, holdings, tx):
        df.columns = [c.lower() for c in df.columns]

    nav_date_col = next((c for c in nav.columns if 'date' in c), nav.columns[0])
    nav_value_col = next((c for c in nav.columns if c not in {nav_date_col} and pd.api.types.is_numeric_dtype(safe_num(nav[c]))), None)
    if nav_value_col is None:
        nav_value_col = next((c for c in nav.columns if c != nav_date_col), nav.columns[1])
    nav[nav_date_col] = pd.to_datetime(nav[nav_date_col], errors='coerce')
    nav = nav.sort_values(nav_date_col)
    nav[nav_value_col] = safe_num(nav[nav_value_col])
    nav = nav.dropna(subset=[nav_date_col, nav_value_col])

    nav['return'] = nav[nav_value_col].pct_change()
    nav['cum_return'] = (1 + nav['return'].fillna(0)).cumprod() - 1
    n = max(len(nav['return'].dropna()), 1)
    annual_return = (nav[nav_value_col].iloc[-1] / nav[nav_value_col].iloc[0]) ** (252 / n) - 1 if len(nav) > 1 else np.nan
    annual_vol = nav['return'].std() * np.sqrt(252)
    sharpe = annual_return / annual_vol if annual_vol and annual_vol > 0 else np.nan
    var_95 = nav['return'].quantile(0.05)

    summary = pd.DataFrame([
        {'metric': 'start_nav', 'value': nav[nav_value_col].iloc[0]},
        {'metric': 'end_nav', 'value': nav[nav_value_col].iloc[-1]},
        {'metric': 'trading_days', 'value': len(nav)},
        {'metric': 'annualized_return', 'value': annual_return},
        {'metric': 'annualized_volatility', 'value': annual_vol},
        {'metric': 'sharpe_ratio', 'value': sharpe},
        {'metric': 'value_at_risk_95', 'value': var_95},
    ])

    summary.to_csv(OUT / 'performance_metrics.csv', index=False)
    nav.to_csv(OUT / 'nav_returns_with_metrics.csv', index=False)

    if not perf.empty:
        perf.to_csv(OUT / 'scheme_performance_clean.csv', index=False)
    if not holdings.empty:
        holdings.to_csv(OUT / 'holdings_clean.csv', index=False)
    if not tx.empty:
        tx.to_csv(OUT / 'transactions_clean.csv', index=False)


if __name__ == '__main__':
    main()
