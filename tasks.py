from crewai import Task


class SEOCrewTasks:

    # 1️⃣ OPERATOR RESEARCH
    def operator_research_task(self, agent, operator_input):
        return Task(
            agent=agent,
            description=(
                f"Research the poker operator '{operator_input}'. "
                "Collect verified, structured information including:\n"
                "- Welcome bonus details\n"
                "- Rakeback structure\n"
                "- Game types and traffic\n"
                "- Software and mobile support\n"
                "- Deposit and withdrawal methods\n"
                "- Licensing and regulatory status\n"
                "- Reputation indicators\n\n"
                "Use search and scraping tools where necessary. "
                "Output structured factual data only, not prose."
            ),
            expected_output=(
                "Structured JSON-style data including bonuses, rakeback, "
                "games, banking, licensing, and trust indicators. "
                "Include confidence level for each major data point."
            ),
            config={}
        )

    # 2️⃣ SERP INTELLIGENCE
    def serp_analysis_task(self, agent, operator_input, research_task):
        return Task(
            agent=agent,
            depends_on=[research_task],
            description=(
                f"Analyze search engine results for '{operator_input} review', "
                f"'{operator_input} rakeback', and related keywords.\n\n"
                "Identify:\n"
                "- Primary and secondary keywords\n"
                "- Common structural patterns\n"
                "- Competitor content gaps\n"
                "- Ranking angles used by competitors\n\n"
                "Do not rewrite competitor content. Extract insights only."
            ),
            expected_output=(
                "Keyword strategy including primary keyword, "
                "secondary keywords, structural expectations, "
                "and identified content opportunities."
            ),
            config={}
        )

    # 3️⃣ REVIEW ARCHITECTURE
    def review_outline_task(self, agent, operator_input, research_task, serp_task):
        return Task(
            agent=agent,
            depends_on=[research_task, serp_task],
            description=(
                f"Create a structured outline for a full poker operator review "
                f"for '{operator_input}'.\n\n"
                "The structure must follow WorldPokerDeals-style format including:\n"
                "- H1 Title\n"
                "- Summary Box\n"
                "- Introduction\n"
                "- Bonuses\n"
                "- Rakeback\n"
                "- Games & Traffic\n"
                "- Software\n"
                "- Banking\n"
                "- Security & Licensing\n"
                "- Pros & Cons\n"
                "- Final Verdict\n"
                "- FAQ\n\n"
                "Do not write full content yet."
            ),
            expected_output=(
                "Detailed content outline including section hierarchy "
                "and required data blocks."
            ),
            config={}
        )

    # 4️⃣ REVIEW WRITING
    def review_writing_task(self, agent, operator_input, research_task, outline_task):
        return Task(
            agent=agent,
            depends_on=[research_task, outline_task],
            description=(
                f"Write a complete poker operator review for '{operator_input}' "
                "following the approved outline.\n\n"
                "Use only verified data from the research phase. "
                "Avoid unverified claims. "
                "Flag any uncertain information.\n\n"
                "Maintain a neutral-professional affiliate tone."
            ),
            expected_output=(
                "Full long-form poker operator review in Markdown format "
                "with structured headings and clearly separated sections."
            ),
            config={}
        )

    # 5️⃣ SEO OPTIMIZATION
    def seo_optimization_task(self, agent, operator_input, writing_task, serp_task):
        return Task(
            agent=agent,
            depends_on=[writing_task, serp_task],
            description=(
                f"Optimize the '{operator_input}' review for search engines.\n\n"
                "Ensure:\n"
                "- Primary keyword appears naturally in H1, intro, and conclusion\n"
                "- Secondary keywords are integrated semantically\n"
                "- Meta title and description are generated\n"
                "- FAQ section targets featured snippet potential\n"
                "- Internal linking suggestions are included\n\n"
                "Preserve readability and natural tone."
            ),
            expected_output=(
                "SEO-optimized review content including meta title, "
                "meta description, FAQ schema suggestions, and "
                "internal linking recommendations."
            ),
            config={}
        )

    # 6️⃣ COMPLIANCE & RISK REVIEW
    def compliance_review_task(self, agent, operator_input, seo_task):
        return Task(
            agent=agent,
            depends_on=[seo_task],
            description=(
                f"Review the '{operator_input}' review for compliance risks.\n\n"
                "Check for:\n"
                "- Misleading claims\n"
                "- Guaranteed profit language\n"
                "- Jurisdictional inaccuracies\n"
                "- Missing responsible gambling disclaimers\n"
                "- Bonus clarity issues\n\n"
                "Add necessary disclaimers where required."
            ),
            expected_output=(
                "Compliance-reviewed version of the article with "
                "risk flags identified and corrections applied."
            ),
            config={}
        )

    # 7️⃣ FINAL EDITORIAL PACKAGING
    def editorial_packaging_task(self, agent, operator_input, compliance_task):
        return Task(
            agent=agent,
            depends_on=[compliance_task],
            description=(
                f"Prepare the final publication-ready version of the "
                f"'{operator_input}' poker review.\n\n"
                "Deliver:\n"
                "- Final formatted Markdown/HTML\n"
                "- Executive summary for human editor\n"
                "- Confidence score\n"
                "- Fact-check checklist\n"
                "- Sections requiring manual verification\n\n"
                "This is the final output before human approval."
            ),
            expected_output=(
                "Publication-ready review article with editorial summary "
                "and review checklist."
            ),
            config={}
        )
