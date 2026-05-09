from bs4 import BeautifulSoup
import requests
import logging

logger = logging.getLogger(__name__)


class Fetcher:
    def __init__(self) -> None:
        self.results = []

    def refresh(self):
        try:
            sauce = requests.get(
                "https://github.com/trending",
                timeout=10,
                headers={"User-Agent": "GTA/1.0"},
            ).text
        except Exception as e:
            logger.error("Failed to fetch GitHub trending: %s", e)
            return self.results

        soup = BeautifulSoup(sauce, "html.parser")
        boxes = soup.find_all("article")
        new_results = []

        for box in boxes:
            try:
                name = box.find("h2").find("a")
                desc = box.find("p")
                lang = box.find("span", attrs={"itemprop": "programmingLanguage"})
                stars, forks, *_ = box.find_all("div")[2].find_all("a")

                new_results.append(
                    {
                        "name": name.text.replace("\n", "").replace(" ", "").strip(),
                        "description": desc.text.replace("\n", "").strip() if desc else "",
                        "language": lang.text.replace("\n", "") if lang else "",
                        "stars": stars.text.replace("\n", "").strip(),
                        "forks": forks.text.replace("\n", "").strip(),
                    }
                )
            except Exception as e:
                logger.warning("Failed to parse a repo box: %s", e)

        if new_results:
            self.results = new_results
        else:
            logger.warning("No results parsed, keeping previous data")

        return self.results
