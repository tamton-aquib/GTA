from unittest.mock import patch
from requests import ConnectionError
from gta.fetch import Fetcher


def test_fetcher_parses_repos():
    html = """
    <article>
      <h2><a href="/user/repo1">user/repo1</a></h2>
      <p>First repo</p>
      <span itemprop="programmingLanguage">Python</span>
      <div></div>
      <div></div>
      <div><a>100</a><a>10</a></div>
    </article>
    """
    with patch("gta.fetch.requests.get") as mock_get:
        mock_get.return_value.text = html
        fetcher = Fetcher()
        fetcher.refresh()

    assert len(fetcher.results) == 1
    assert fetcher.results[0]["name"] == "user/repo1"
    assert fetcher.results[0]["language"] == "Python"


def test_fetcher_keeps_old_data_on_failure():
    fetcher = Fetcher()
    fetcher.results = [{"name": "cached/repo", "description": "", "language": "", "stars": "", "forks": ""}]

    with patch("gta.fetch.requests.get") as mock_get:
        mock_get.side_effect = ConnectionError("Network error")
        fetcher.refresh()

    assert len(fetcher.results) == 1
    assert fetcher.results[0]["name"] == "cached/repo"


def test_fetcher_handles_missing_fields():
    html = """
    <article>
      <h2><a href="/user/repo1">user/repo1</a></h2>
      <p></p>
      <div></div>
      <div></div>
      <div><a>0</a><a>0</a></div>
    </article>
    """
    with patch("gta.fetch.requests.get") as mock_get:
        mock_get.return_value.text = html
        fetcher = Fetcher()
        fetcher.refresh()

    assert len(fetcher.results) == 1
    assert fetcher.results[0]["description"] == ""
    assert fetcher.results[0]["language"] == ""
