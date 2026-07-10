# Mutual Fund Capstone Project Report

## Executive Summary
This project analyzes Indian mutual fund data using Python, SQL, and interactive reporting. It covers ETL, database creation, EDA, performance analytics, and portfolio insights across schemes, fund houses, transactions, holdings, and benchmark indices.

## Project Objectives
- Build a reproducible data pipeline.
- Store processed data in SQLite.
- Measure scheme and portfolio performance.
- Identify trends in inflows, investor activity, and benchmark behavior.
- Present findings in a clear dashboard and report format.

## Data Sources
The project uses processed datasets for fund master, NAV history, AUM by fund house, SIP inflows, category inflows, folio counts, scheme performance, investor transactions, portfolio holdings, and benchmark indices.

## Methodology
1. Ingest raw source files and standardize column names.
2. Load cleaned tables into SQLite.
3. Compute return-based metrics such as CAGR, volatility, Sharpe ratio, beta, and VaR.
4. Explore trends by fund house, category, and scheme.
5. Summarize the most important investment and risk findings.

## Key Findings
- NAV time series can be used to measure long-term fund consistency and drawdowns.
- Transaction and SIP data reveal investor behavior patterns across time.
- Performance must be interpreted alongside risk, not just absolute returns.
- Benchmark comparison is essential for judging whether returns are meaningful.
- Portfolio analytics improve when holdings are analyzed with diversification and concentration in mind.

## Performance Framework
The report should include:
- CAGR using trading-day annualization.
- Annualized volatility from daily returns.
- Sharpe ratio using excess return per unit of risk.
- Beta against a benchmark index.
- Historical Value at Risk for downside assessment.

## Dashboard Summary
The dashboard should contain four pages:
1. Overview and KPI summary.
2. Scheme performance and benchmark comparison.
3. Investor transactions and SIP trends.
4. Portfolio and risk analytics.

Each page should include at least two slicers for interactive filtering.

## Advanced Analytics
Suggested advanced analysis includes:
- Cohort analysis of investor behavior.
- Scheme ranking by risk-adjusted return.
- Recommender logic for fund selection.
- Monte Carlo projection for NAV growth.
- Efficient frontier for selected schemes.

## Conclusions
The dataset supports a full mutual fund analytics workflow from ingestion to reporting. The strongest results come from combining performance metrics with risk, investor behavior, and benchmark context.

## Next Deliverables
- PowerPoint presentation
- Dashboard workbook
- EDA notebook
- Performance metrics notebook
