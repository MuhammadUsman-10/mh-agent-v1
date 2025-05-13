from crewai import Crew
from agents.therapist_agent import therapist_agent
from agents.planner_agent import planner_agent
from tasks import therapist_task, planner_task 

crew = Crew(
    agents=[therapist_agent, planner_agent],
    tasks=[therapist_task, planner_task],
    verbose=True
)

def main():
    print("🌟 Your Personal Agentic Assistant is Live!")
    user_input = input("You: ")
    result = crew.kickoff(inputs={"input": user_input})
    print("AI Assistant:", result)

if __name__ == "__main__":
    main()