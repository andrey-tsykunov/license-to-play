from crewai import Crew, Process

from crewai_agent.agents import create_analyst, create_researcher, create_writer
from crewai_agent.tasks import create_analysis_task, create_report_task, create_research_task


def create_tech_evaluator_crew(topic: str) -> Crew:
    """
    Assemble the Tech Stack Evaluator crew for a given topic.

    Three specialised agents run sequentially:
      1. Researcher  — gathers facts and context
      2. Analyst     — evaluates trade-offs and use cases
      3. Writer      — synthesises everything into an actionable report

    Each task's output is automatically passed as context to the next task,
    demonstrating CrewAI's core strength: structured, role-based pipelines
    where agents build on each other's work.
    """
    researcher = create_researcher()
    analyst = create_analyst()
    writer = create_writer()

    research_task = create_research_task(researcher, topic)
    analysis_task = create_analysis_task(analyst, topic)
    report_task = create_report_task(writer, topic)

    # context= wires explicit data dependencies between tasks
    analysis_task.context = [research_task]
    report_task.context = [research_task, analysis_task]

    return Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, report_task],
        process=Process.sequential,
        verbose=True,
    )


def run_evaluation(topic: str) -> str:
    crew = create_tech_evaluator_crew(topic)
    result = crew.kickoff(inputs={"topic": topic})
    return str(result)
