import os
from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from gta.fetch import Fetcher
from threading import Thread
from random import choice, sample
from time import sleep

PORT = int(os.getenv("PORT", 5000))
REFRESH_INTERVAL = int(os.getenv("REFRESH_INTERVAL", 300))
RATE_LIMIT = os.getenv("RATE_LIMIT", "100 per minute")
BASE_URL = os.getenv("BASE_URL", "")

app = Flask(__name__)
app.url_map.strict_slashes = False

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=[RATE_LIMIT],
    storage_uri="memory://",
)

fetcher = Fetcher()
fetcher.refresh()


def update_trending_list():
    while True:
        sleep(REFRESH_INTERVAL)
        fetcher.refresh()


Thread(target=update_trending_list, daemon=True).start()


def _base():
    return BASE_URL or request.host_url


@app.get("/")
def home():
    base = _base()
    return {
        "repositories": {
            "url": f"{base}repositories",
            "params": {
                "count": "int (optional, default: all, max: 25)"
            }
        },
        "random": {
            "url": f"{base}random",
            "params": {
                "count": "int (optional, default: 1, max: 25)"
            }
        },
        "health": {
            "url": f"{base}health"
        }
    }


@app.get("/health")
def health():
    return {"status": "ok", "cached_repos": len(fetcher.results)}


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
