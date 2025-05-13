from crewai import Task
from agents.therapist_agent import therapist_agent
from agents.planner_agent import planner_agent

therapist_task = Task(
    description="Analyze the user's input and provide mental health support and encouragement based on their emotional state.",
    expected_output="An empathetic, supportive message, possibly including a motivational quote or suggestion.",
    agent=therapist_agent
)

planner_task = Task(
    description="Based on the user's emotional input, suggest a small, manageable daily routine to improve their mental well-being.",
    expected_output="A 2-3 step healthy routine aligned with the user's current mood.",
    agent=planner_agent
)