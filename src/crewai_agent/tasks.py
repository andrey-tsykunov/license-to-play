from crewai import Agent, Task


def create_research_task(researcher: Agent, topic: str) -> Task:
    return Task(
        description=(
            f"Research the technology or framework: **{topic}**.\n\n"
            "Cover the following:\n"
            "1. What it is and what problem it solves\n"
            "2. Core concepts and architecture\n"
            "3. Adoption: who uses it, community size, GitHub stars, release history\n"
            "4. Ecosystem: integrations, plugins, tooling\n"
            "5. Any notable real-world case studies or benchmarks\n\n"
            "Be factual and specific. Avoid marketing language."
        ),
        expected_output=(
            "A structured research brief (400-600 words) covering the five areas above, "
            "with specific version numbers, statistics, and named companies/projects where possible."
        ),
        agent=researcher,
    )


def create_analysis_task(analyst: Agent, topic: str) -> Task:
    return Task(
        description=(
            f"Using the research brief on **{topic}**, perform a critical technical analysis.\n\n"
            "Your analysis must include:\n"
            "1. **Strengths** — where this technology genuinely excels (with concrete reasons)\n"
            "2. **Weaknesses** — honest limitations and known pain points\n"
            "3. **Ideal use cases** — specific scenarios where this is the right choice\n"
            "4. **When to avoid it** — scenarios where alternatives serve better\n"
            "5. **Comparison** — how it stacks up against 1-2 direct alternatives\n\n"
            "Base your analysis on the provided research brief. Add engineering insight."
        ),
        expected_output=(
            "A technical analysis document (400-500 words) with clearly labelled sections "
            "for Strengths, Weaknesses, Ideal Use Cases, When to Avoid, and Comparison. "
            "Conclude with a one-sentence verdict."
        ),
        agent=analyst,
    )


def create_report_task(writer: Agent, topic: str) -> Task:
    return Task(
        description=(
            f"Using the research brief and technical analysis for **{topic}**, "
            "write a polished evaluation report.\n\n"
            "The report must:\n"
            "- Open with a 2-3 sentence executive summary\n"
            "- Include an Overview section synthesising the research\n"
            "- Include a Strengths & Weaknesses section from the analysis\n"
            "- Include a 'Best Fit' section: when to choose this technology\n"
            "- Close with a 'Verdict & Recommendation' (3-4 sentences)\n"
            "- Use markdown formatting with headers, bullet points, and bold key terms\n\n"
            "Target audience: senior engineers making a technology adoption decision."
        ),
        expected_output=(
            "A complete markdown evaluation report (600-800 words) with the sections: "
            "Executive Summary, Overview, Strengths & Weaknesses, Best Fit, "
            "and Verdict & Recommendation."
        ),
        agent=writer,
    )
