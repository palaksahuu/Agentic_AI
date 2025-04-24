import streamlit as st
from workflow.graph import graph, TaskState

def run_workflow(query):
    g = graph()
    final_state = g.invoke(TaskState(query=query))
    return final_state.results

st.title("LangGraph Agentic Workflow")
query = st.text_input("Enter your complex query:")

if st.button("Run Workflow") and query:
    results = run_workflow(query)
    st.subheader("Results")
    for task, result in results:
        st.write(f"**{task}**: {result}")