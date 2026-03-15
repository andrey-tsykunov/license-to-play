"""
CrewAI Tech Stack Evaluator

Demonstrates CrewAI's core strength: role-based multi-agent pipelines where
specialised agents each own a stage, and task outputs chain forward as context.

The crew consists of three agents working sequentially:
  1. Technology Researcher  — gathers facts, adoption data, and ecosystem details
  2. Technical Analyst      — evaluates trade-offs, strengths, weaknesses, ideal use cases
  3. Technical Writer       — synthesises everything into a polished evaluation report

Usage:
    PYTHONPATH=src python src/crewai_agent/main.py
    PYTHONPATH=src python src/crewai_agent/main.py --topic "FastAPI"
    PYTHONPATH=src python src/crewai_agent/main.py --topic "Rust"
"""

import argparse

from dotenv import load_dotenv

from crewai_agent.crew import run_evaluation

load_dotenv()


def main() -> None:
    parser = argparse.ArgumentParser(description="Tech Stack Evaluator powered by CrewAI")
    parser.add_argument(
        "--topic",
        default="LangGraph",
        help="Technology or framework to evaluate (default: LangGraph)",
    )
    args = parser.parse_args()

    print(f"\n{'=' * 60}")
    print(f"  Tech Stack Evaluator — Topic: {args.topic}")
    print(f"{'=' * 60}\n")

    report = run_evaluation(args.topic)

    print(f"\n{'=' * 60}")
    print("  FINAL REPORT")
    print(f"{'=' * 60}\n")
    print(report)


if __name__ == "__main__":
    main()
