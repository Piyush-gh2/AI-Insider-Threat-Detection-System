import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

from src.agents import analyze_logs
from src.rag import load_knowledge, build_index, retrieve

st.title("🔐 AI Insider Threat Detection System")

query = st.text_input("Ask Security Insight")

if st.button("Analyze Logs"):
    
    df, graph = analyze_logs()
    
    st.subheader("📊 Employee Activity Logs")
    st.dataframe(df)
    
    st.subheader("⚠️ Risk Analysis")
    st.write(df[["employee", "action", "risk"]])
    
    st.subheader("🕸️ Employee Relationship Graph")
    
    fig, ax = plt.subplots()
    nx.draw(graph, with_labels=True, ax=ax)
    st.pyplot(fig)
    
    # RAG
    docs = load_knowledge()
    index = build_index(docs)
    
    if query:
        
        insights = retrieve(query, docs, index)
        
        st.subheader("🔎 Security Insights")
        
        for i in insights:
            st.write(i)