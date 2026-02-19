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
                "Structured JSON-style data including bonuses, rakeback, games, banking, licensing, and trust "
                "indicators. For each key field, include: `value`, `source_url`, and `confidence` "
                "(high/medium/low). If offers differ by region or source, record them as `variants` instead "
                "of picking one."
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
                "- Ranking angles used by competitors\n"
                "- How clearly competitors explain who the room is best for (stakes, player types)\n"
                "- How they describe rakeback and bonus clearing (vague vs concrete)\n"
                "- Obvious marketing hype or over-promising to avoid\n\n"
                "Do not rewrite competitor content. Extract insights only."
            ),
            expected_output=(
                "Keyword strategy including primary keyword, secondary keywords, structural expectations, "
                "and identified content opportunities, including gaps in honesty, specificity, and target player profile."
            ),
            config={}
        )

    # 3️⃣ REVIEW ARCHITECTURE
    def review_outline_task(self, agent, operator_input, research_task, serp_task):
        return Task(
            agent=agent,
            depends_on=[research_task, serp_task],
            description=(
                f"Create a structured outline for a full poker operator review for '{operator_input}'.\n\n"
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
                "- Who This Room Is Best For / Who It’s Not For\n"
                "- Pros & Cons\n"
                "- Final Verdict\n"
                "- FAQ\n\n"
                "Make sure the outline supports a candid, poker-native tone for regs and serious recs, "
                "and makes it easy to explain practical pros/cons."
            ),
            expected_output=(
                "Detailed content outline including section hierarchy and required data blocks, "
                "with bullets for key points under each section."
            ),
            config={}
        )

    # 4️⃣ REVIEW WRITING
    def review_writing_task(self, agent, operator_input, research_task, outline_task):
        return Task(
            agent=agent,
            depends_on=[research_task, outline_task],
            description=(
                f"Write a complete poker operator review for '{operator_input}' following the approved outline.\n\n"
                "Use only verified data from the research phase. Do not invent specific numerical offers or "
                "guarantees. If data varies by region or source, explain that clearly.\n\n"
                "Tone: professional but conversational, as if a knowledgeable poker player is explaining the room "
                "to another player. Use standard industry vocabulary (e.g., regs, recs, micro-stakes, mid-stakes, "
                "liquidity, traffic, rakeback, PKO) and avoid generic hype phrases such as 'premier platform', "
                "'top choice', or 'unmatched experience'.\n\n"
                "Include practical details that help players decide if this room fits their profile: stakes, "
                "traffic peaks, rakeback realism vs advertised maximums, and software strengths/weaknesses.\n\n"
                "Maintain a neutral-professional affiliate tone with honest pros and cons."
            ),
            expected_output=(
                "Full long-form poker operator review in Markdown format with structured headings and clearly "
                "separated sections, written for intermediate to advanced online poker players."
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
                "Do NOT remove or soften critical points about weaknesses (e.g., lower traffic than biggest rooms, "
                "average rakeback compared to competitors, limited high-stakes action). Optimize headings, internal "
                "anchors, and keyword placement, but keep the poker-player voice intact.\n\n"
                "Preserve readability and natural tone."
            ),
            expected_output=(
                "SEO-optimized review content including meta title, meta description, FAQ schema suggestions, "
                "and internal linking recommendations, with the original poker-native tone preserved."
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
                "Add necessary disclaimers where required. Preserve honest discussion of drawbacks (e.g., traffic, "
                "rakeback, software issues). Do not remove balanced criticism unless it creates legal risk."
            ),
            expected_output=(
                "Compliance-reviewed version of the article with risk flags identified and corrections applied, "
                "with honest pros and cons still intact."
            ),
            config={}
        )

    # 7️⃣ FINAL EDITORIAL PACKAGING
    def editorial_packaging_task(self, agent, operator_input, compliance_task):
        return Task(
            agent=agent,
            depends_on=[compliance_task],
            description=(
                f"Prepare the final publication-ready version of the '{operator_input}' poker review.\n\n"
                "Deliver:\n"
                "- Final formatted Markdown/HTML\n"
                "- Executive summary for human editor\n"
                "- Confidence score\n"
                "- Fact-check checklist\n"
                "- Sections requiring manual verification\n\n"
                "Before finalizing, check:\n"
                "- Does the review clearly state who the room is ideal for and who might be better off elsewhere?\n"
                "- Are bonus and rakeback descriptions honest about variability and conditions?\n"
                "- Is the tone consistent with a knowledgeable poker player speaking to another player?\n"
                "- Are any phrases too generic or promotional for a reg audience? If so, rewrite them.\n\n"
                "This is the final output before human approval."
            ),
            expected_output=(
                "Publication-ready review article with editorial summary and review checklist, preserving a "
                "poker-native, honest tone."
            ),
            config={}
        )


