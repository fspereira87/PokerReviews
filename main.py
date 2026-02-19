from crewai import Crew, Process
from agents import SEOCrewAgents
from tasks import SEOCrewTasks


class PokerReviewCrew:
    def __init__(self, operator_input, log_callback=None):
        """
        operator_input: Operator name or URL
        """
        self.operator_input = operator_input
        self.current_year = datetime.now().year
        self.agents = SEOCrewAgents()
        self.tasks = SEOCrewTasks()
        self.log_callback = log_callback or (lambda x: None)

    def log(self, message):
        print(message)
        self.log_callback(message)

    def run(self):
        self.log("👤 Initializing Poker Review Agents...")

        researcher = self.agents.operator_researcher()
        serp_agent = self.agents.serp_intelligence_agent()
        architect = self.agents.review_architect()
        writer = self.agents.review_writer()
        seo_optimizer = self.agents.seo_optimizer()
        compliance = self.agents.compliance_agent()
        editor = self.agents.editorial_supervisor()

        self.log("📌 Defining Poker Review Tasks...")

        # 1️⃣ Research (root task)
        research_task = self.tasks.operator_research_task(
            researcher,
            self.operator_input
        )

        # 2️⃣ SERP Intelligence
        serp_task = self.tasks.serp_analysis_task(
            serp_agent,
            self.operator_input,
            research_task
        )

        # 3️⃣ Outline Architecture
        outline_task = self.tasks.review_outline_task(
            architect,
            self.operator_input,
            research_task,
            serp_task
        )

        # 4️⃣ Writing
        writing_task = self.tasks.review_writing_task(
            writer,
            self.operator_input,
            research_task,
            outline_task
        )

        # 5️⃣ SEO Optimization
        seo_task = self.tasks.seo_optimization_task(
            seo_optimizer,
            self.operator_input,
            writing_task,
            serp_task
        )

        # 6️⃣ Compliance Review
        compliance_task = self.tasks.compliance_review_task(
            compliance,
            self.operator_input,
            seo_task
        )

        # 7️⃣ Final Editorial Packaging
        final_task = self.tasks.editorial_packaging_task(
            editor,
            self.operator_input,
            compliance_task
        )

        self.log("🚀 Kicking off Poker Review Crew...")

        crew = Crew(
            agents=[
                researcher,
                serp_agent,
                architect,
                writer,
                seo_optimizer,
                compliance,
                editor
            ],
            tasks=[
                research_task,
                serp_task,
                outline_task,
                writing_task,
                seo_task,
                compliance_task,
                final_task
            ],
            process=Process.sequential
        )

        result = crew.kickoff()

        self.log("✅ Poker Review process completed.")
        return result


