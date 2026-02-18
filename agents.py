from crewai import Agent
from langchain_openai import ChatOpenAI

from tools.search import DuckDuckGoSearchTool
from tools.web_scraper import ScrapeWebsiteTool


class SEOCrewAgents:
    def __init__(self):
        # Tools (CrewAI-native)
        self.search_tool = DuckDuckGoSearchTool()
        self.scrape_tool = ScrapeWebsiteTool()

        # LLM
        self.llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.7
        )

    def operator_researcher(self):
        return Agent(
            role="Poker Operator Intellegence Researcher",
            goal=(
                "Collect verified, structured information about a poker operator "
                "including bonuses, rakeback, traffic, software, banking methods, "
                "licensing, buy-ins values, different cash games values, and reputation."
            ),
            backstory=(
                "A data-driven iGaming market analyst specializing in poker rooms, "
                "networks, affiliate deals, and regulatory structures."
            ),
            tools=[self.search_tool, self.scrape_tool],
            verbose=True,
            llm=self.llm
        )

    def serp_intelligence_agent(self):
        return Agent(
            role="SERP Intelligence Analyst",
            goal=(
                "Analyze top-ranking pages for the operator review keyword and "
                "identify content gaps, structural patterns, and keyword opportunities."
            ),
            backstory=(
                "An advanced SEO strategist who reverse engineers affiliate pages "
                "to uncover ranking patterns and monetization structures."
            ),
            tools=[self.search_tool],
            verbose=True,
            llm=self.llm
        )

    def review_architect(self):
        return Agent(
            role="Poker Review Content Architect",
            goal=(
                "Design a structured outline for a poker operator review that "
                "matches WorldPokerDeals-style formatting and affiliate positioning,"
                "and adapt the structure based on the operator's unique selling points and SERP insights."
            ),
            backstory=(
                "A senior affiliate editor experienced in structuring high-converting "
                "long-form poker room reviews."
            ),
            verbose=True,
            llm=self.llm
        )

    def review_writer(self):
        return Agent(
            role="Poker Review Writer",
            goal=(
                "Write a comprehensive, persuasive, and factually grounded "
                "poker operator review following the approved outline,"
                "use the correct tone of voice, relaxed but professional, using normal industry vocabulary, and include all relevant information for players to make informed decisions."
            ),
            backstory=(
                "A professional poker content writer, ex-poker professional poker player, with deep knowledge of "
                "online poker ecosystems, rake structures, and affiliate dynamics."
            ),
            tools=[self.search_tool],
            verbose=True,
            llm=self.llm
        )

    def seo_optimizer(self):
            return Agent(
            role="On-Page SEO Optimizer",
            goal=(
                "Enhance the review to maximize ranking potential while preserving "
                "natural readability and compliance."
            ),
            backstory=(
                "An SEO specialist focused on affiliate content optimization, "
                "semantic keyword distribution, and search intent alignment."
            ),
            verbose=True,
            llm=self.llm
        )

    def compliance_agent(self):
        return Agent(
            role="iGaming Compliance & Risk Reviewer",
            goal=(
                "Ensure all claims are jurisdictionally safe, non-misleading, "
                "and include required responsible gambling disclaimers."
            ),
            backstory=(
                "A regulatory specialist familiar with online gambling compliance, "
                "advertising standards, and affiliate risk management."
            ),
            verbose=True,
            llm=self.llm
        )

    def editorial_supervisor(self):
        return Agent(
            role="Editorial Supervisor",
            goal=(
                "Compile the final optimized review and prepare a concise "
                "editorial summary highlighting uncertainties or risk areas "
                "for human approval."
            ),
            backstory=(
                "A senior managing editor responsible for ensuring quality, "
                "consistency, and strategic positioning before publication."
            ),
            verbose=True,
            llm=self.llm
        )
