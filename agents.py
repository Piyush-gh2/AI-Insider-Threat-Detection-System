from src.loader import load_logs
from src.risk_engine import calculate_risk
from src.graph_ai import build_graph

def analyze_logs():
    
    df = load_logs()
    
    risks = []
    
    for _, row in df.iterrows():
        risk = calculate_risk(row["action"], row["time"])
        risks.append(risk)
    
    df["risk"] = risks
    
    graph = build_graph(df)
    
    return df, graph