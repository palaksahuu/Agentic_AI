from langgraph.graph import StateGraph, END
from agents.plan_agent import generate_plan
from agents.tool_agent import solve_task
# from langgraph.checkpoint.base import BaseCheckpointSaver, Checkpoint, CheckpointAt
from langgraph.checkpoint.base import BaseCheckpointSaver, Checkpoint

class TaskState:
    def __init__(self, query, tasks=None, results=None):
        self.query = query
        self.tasks = tasks or []
        self.results = results or []

def plan_node(state):
    tasks = generate_plan(state.query)
    return TaskState(query=state.query, tasks=tasks, results=[])

def tool_node(state):
    results = []
    for task in state.tasks:
        result = solve_task(task)
        results.append((task, result))
    return TaskState(query=state.query, tasks=state.tasks, results=results)

def graph():
    builder = StateGraph(TaskState)
    builder.add_node("planner", plan_node)
    builder.add_node("executor", tool_node)
    builder.set_entry_point("planner")
    builder.add_edge("planner", "executor")
    builder.add_edge("executor", END)
    return builder.compile()