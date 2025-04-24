# LangGraph Agentic Workflow

## Overview
This project implements an agentic workflow using LangGraph where:
- A `PlanAgent` breaks a user query into subtasks.
- A `ToolAgent` solves each subtask using appropriate tools.
- A feedback loop ensures task refinement.

## Installation

pip install -r requirements.txt

## Usage

streamlit run frontend/app.py

## Project Structure
- `agents/`: Agents for planning and tool execution
- `workflow/`: LangGraph pipeline logic
- `frontend/`: Frontend using Streamlit