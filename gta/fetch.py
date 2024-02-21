from bs4 import BeautifulSoup
import requests

class Fetcher:
    def __init__(self) -> None:
        self.results = []

    def refresh(self):
        sauce = requests.get('https://github.com/trending').text
        soup = BeautifulSoup(sauce, 'lxml')

        boxes = soup.find_all('article')

        for box in boxes:
            name = box.find('h2').find('a')
            desc = box.find('p')
            lang = box.find('span', attrs={"itemprop": "programmingLanguage"})
            stars, forks, *_ = box.find_all('div')[2].find_all('a')

            self.results.append({
                    "name": name.text.replace('\n', '').replace(' ', '').strip(),
                    "description":  desc.text.replace('\n', '').strip() if desc else '',
                    "language": lang.text.replace('\n', '') if lang else '',
                    "stars": stars.text.replace('\n', '').strip(),
                    "forks": forks.text.replace('\n', '').strip()
                }
            )
