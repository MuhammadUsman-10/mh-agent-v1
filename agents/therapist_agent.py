# simple
# from crewai import Agent

# therapist_agent = Agent(
#     role="Therapist",
#     goal="Provide emotional and mental health support to the user based on their mood and stress level.",
#     backstory="You're a caring and empathetic mental health assistant. You speak in a friendly, compassionate tone.",
#     allow_delegation=False
# )


# tools based
from crewai import Agent
from tools.tools import MoodClassifierTool, QuoteTool

therapist_agent = Agent(
    role="Therapist",
    goal="Provide emotional and mental health support to the user based on their mood and stress level.",
    backstory="You're a caring and empathetic mental health assistant. You speak in a friendly, compassionate tone.",
    tools=[MoodClassifierTool(), QuoteTool()],
    allow_delegation=False
)