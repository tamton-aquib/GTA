from unittest.mock import patch
import pytest

MOCK_HTML = """
<article>
  <h2><a href="/user/repo1">user/repo1</a></h2>
  <p>First repo</p>
  <span itemprop="programmingLanguage">Python</span>
  <div></div>
  <div></div>
  <div><a>100</a><a>10</a></div>
</article>
<article>
  <h2><a href="/user/repo2">user/repo2</a></h2>
  <p>Second repo</p>
  <span itemprop="programmingLanguage">JavaScript</span>
  <div></div>
  <div></div>
  <div><a>200</a><a>20</a></div>
</article>
<article>
  <h2><a href="/user/repo3">user/repo3</a></h2>
  <p>Third repo</p>
  <span itemprop="programmingLanguage">Rust</span>
  <div></div>
  <div></div>
  <div><a>300</a><a>30</a></div>
</article>
"""

patcher = patch("gta.fetch.requests.get")
mock_get = patcher.start()
mock_get.return_value.text = MOCK_HTML

from gta.main import app, fetcher


@pytest.fixture
def client():
    with app.test_client() as c:
        yield c


@pytest.fixture(autouse=True)
def refresh_fetcher():
    fetcher.refresh()
    yield
