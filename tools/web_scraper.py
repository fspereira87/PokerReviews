from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
from bs4 import BeautifulSoup


class ScrapeWebsiteInput(BaseModel):
    url: str = Field(..., description="Full website URL to scrape")


class ScrapeWebsiteTool(BaseTool):
    name: str = "scrape_website"
    description: str = (
        "Scrape and extract the main visible text content from a website URL "
        "for SEO analysis."
    )

    # 🔴 REQUIRED annotation
    args_schema: type[BaseModel] = ScrapeWebsiteInput

    def _run(self, url: str) -> str:
        try:
            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0 Safari/537.36"
                )
            }

            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            for tag in soup(["script", "style", "noscript", "iframe", "svg"]):
                tag.decompose()

            text = soup.get_text(separator=" ", strip=True)
            return text[:8000]

        except Exception as e:
            return f"Error scraping website {url}: {str(e)}"
