from flask import Flask, request
from gta.fetch import Fetcher
from threading import Thread

from random import choice, sample
from time import sleep

app = Flask(__name__)
HOST = "https://localhost:8000"

fetcher = Fetcher()
fetcher.refresh()
data = fetcher.results

def update_trending_list():
    while True:
        sleep(5 * 60)
        data = fetcher.refresh()

@app.get("/")
def home():
    return {
        "repositories": f"{HOST}/repositories",
        "random": f"{HOST}/random",
    }

@app.get("/repositories/")
def repositories():
    count = request.args.get('count')
    return data if not count else data[:int(count)]

@app.get("/random")
def random():
    count = request.args.get('count')
    return sample(data, int(count)) if count else choice(data)

Thread(target=update_trending_list).start()
