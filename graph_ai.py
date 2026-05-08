import networkx as nx

def build_graph(df):
    
    G = nx.Graph()
    
    for _, row in df.iterrows():
        employee = row["employee"]
        file = row["file"]
        
        G.add_node(employee)
        G.add_node(file)
        
        G.add_edge(employee, file)
    
    return G