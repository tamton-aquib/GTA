from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from gta.fetch import Fetcher
from threading import Thread
from random import choice, sample
from time import sleep

app = Flask(__name__)
app.url_map.strict_slashes = False

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["100 per minute"],
    storage_uri="memory://",
)

fetcher = Fetcher()
fetcher.refresh()


def update_trending_list():
    while True:
        sleep(5 * 60)
        fetcher.refresh()


Thread(target=update_trending_list, daemon=True).start()


@app.get("/")
def home():
    return {
        "repositories": f"{request.host_url}repositories",
        "random": f"{request.host_url}random",
    }


@app.get("/repositories")
def repositories():
    count = request.args.get("count")
    if count is None:
        return fetcher.results
    try:
        count = int(count)
    except (ValueError, TypeError):
        return {"error": "count must be an integer"}, 400
    if count < 0 or count > len(fetcher.results):
        return {
            "error": f"count must be between 0 and {len(fetcher.results)}"
        }, 400
    return fetcher.results[:count]


@app.get("/random")
def random():
    count = request.args.get("count")
    if count is None:
        return choice(fetcher.results)
    try:
        count = int(count)
    except (ValueError, TypeError):
        return {"error": "count must be an integer"}, 400
    if count < 0 or count > len(fetcher.results):
        return {
            "error": f"count must be between 0 and {len(fetcher.results)}"
        }, 400
    return sample(fetcher.results, count)
