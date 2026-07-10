# Data Dictionary

## dim_fund
- amfi_code: Unique mutual fund code.
- fund_house: Asset management company name.
- scheme_name: Mutual fund scheme name.
- category: Broad fund category.
- sub_category: Fund sub-category.
- plan: Direct or Regular plan.
- launch_date: Fund launch date.
- benchmark: Benchmark index.
- expense_ratio_pct: Expense ratio percent.
- exit_load_pct: Exit load percent.
- min_sip_amount: Minimum SIP amount.
- min_lumpsum_amount: Minimum lumpsum amount.
- fund_manager: Fund manager name.
- risk_category: Risk label.
- sebi_category_code: SEBI classification code.

## dim_date
- date_key: Calendar date.
- year, quarter, month, month_name, day, day_of_week, day_name: Date attributes.
- is_weekend: Weekend flag.

## fact_nav
- amfi_code: Fund code.
- date_key: NAV date.
- nav: NAV value.

## fact_transactions
- investor_id: Investor identifier.
- transaction_date: Date of transaction.
- amfi_code: Fund code.
- transaction_type: SIP, Lumpsum, or Redemption.
- amount_inr: Transaction amount.
- state, city, city_tier: Investor geography.
- age_group, gender, annual_income_lakh: Investor profile.
- payment_mode: Payment method.
- kyc_status: KYC verification status.

## fact_performance
- Created as an empty table because 07_scheme_performance.csv is malformed and not parsed correctly.

## fact_aum
- fund_house: Asset management company.
- aum_cr: AUM in crore.
- source_period: Reporting period.
