-- 1. Top 5 funds by AUM in fact_aum
SELECT fund_house, aum_cr
FROM fact_aum
ORDER BY aum_cr DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT substr(date_key, 1, 7) AS ym, AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY substr(date_key, 1, 7)
ORDER BY ym;

-- 3. SIP monthly trend
SELECT substr(transaction_date, 1, 7) AS ym, SUM(amount_inr) AS sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY substr(transaction_date, 1, 7)
ORDER BY ym;

-- 4. Transactions by state
SELECT state, COUNT(*) AS txn_count, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with expense ratio under 1%
SELECT scheme_name, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;
