
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date TEXT,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL,
    min_lumpsum_amount REAL,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT
);

CREATE TABLE IF NOT EXISTS dim_date (
    date_key TEXT PRIMARY KEY,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    month_name TEXT,
    day INTEGER,
    day_of_week INTEGER,
    day_name TEXT,
    is_weekend INTEGER
);

CREATE TABLE IF NOT EXISTS fact_nav (
    amfi_code INTEGER,
    date_key TEXT,
    nav REAL,
    PRIMARY KEY (amfi_code, date_key)
);

CREATE TABLE IF NOT EXISTS fact_transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id TEXT,
    transaction_date TEXT,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT
);

CREATE TABLE IF NOT EXISTS fact_performance (
    amfi_code INTEGER,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    plan TEXT,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    return_10yr_pct REAL,
    sharpe_ratio REAL,
    alpha REAL,
    beta REAL,
    sortino_ratio REAL,
    rolling_std REAL,
    max_drawdown_pct REAL,
    aum_cr REAL,
    expense_ratio_pct REAL,
    rating REAL,
    risk_category TEXT,
    PRIMARY KEY (amfi_code, plan)
);

CREATE TABLE IF NOT EXISTS fact_aum (
    fund_house TEXT,
    aum_cr REAL,
    source_period TEXT
);
