import pandas as pd

def recommend(risk_appetite, perf_path="output/07_scheme_performance.csv"):
    df=pd.read_csv(perf_path)
    m={'Low':['Low'], 'Moderate':['Moderate','Medium'], 'High':['High']}
    vals=m.get(risk_appetite.title(), [risk_appetite])
    if 'risk_grade' not in df.columns:
        raise ValueError('risk_grade column missing')
    sub=df[df['risk_grade'].astype(str).str.title().isin(vals)].copy()
    if sub.empty:
        return pd.DataFrame(columns=['scheme_name','fund_house','risk_grade','sharpe_ratio'])
    sub=sub.sort_values('sharpe_ratio', ascending=False).head(3)
    return sub[['scheme_name','fund_house','risk_grade','sharpe_ratio']]

if __name__ == '__main__':
    import sys
    risk=sys.argv[1] if len(sys.argv)>1 else 'Moderate'
    print(recommend(risk).to_string(index=False))
