# GTA
Github Trending API

> [!Note]
> The endpoint is at: https://gta.tamton.com

### Repositories

> <details><summary>/repositories</summary>
>
> ```jsonc
> [
>   {
>     "description": "Python code to parse a Twitter archive and output in various ways",
>     "forks": "25",
>     "language": "Python",
>     "name": "timhutton/twitter-archive-parser",
>     "stars": "630"
>   },
>   {...}, // total 25 repositories
> ]
> ```
> </details>

> <details><summary>/repositories?count=3</summary>
>
> ```jsonc
> [
>   {
>     "description": "Python code to parse a Twitter archive and output in various ways",
>     "forks": "25",
>     "language": "Python",
>     "name": "timhutton/twitter-archive-parser",
>     "stars": "630"
>   },
>   {...}, // total 3 repositories
> ]
> ```
> </details>

### Random

> <details><summary>/random</summary>
>
> ```jsonc
> {
>   "description": "Python code to parse a Twitter archive and output in various ways",
>   "forks": "25",
>   "language": "Python",
>   "name": "timhutton/twitter-archive-parser",
>   "stars": "630"
> }
> ```
> </details>

> <details><summary>/random?count=3</summary>
>
> ```jsonc
> [
>   {
>     "description": "Python code to parse a Twitter archive and output in various ways",
>     "forks": "25",
>     "language": "Python",
>     "name": "timhutton/twitter-archive-parser",
>     "stars": "630"
>   },
>   {...}, // total 3 random repositories
> ]
> ```
> </details>

### Healthcheck

> <details><summary>/health</summary>
>
> ```jsonc
> {
>   "status": "ok",
>   "cached_repos": 25
> }
> ```
> </details>

## Usage

### Prerequisites
- Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (Python package manager)

### Development
```sh
uv sync
uv run flask run --port ${PORT:-5000}
```

### Testing
```sh
uv run pytest
```

### Docker
```sh
docker build -t gta .
docker run -p 5000:5000 gta:latest
```

### Docker Compose
```sh
docker compose up -d
```

### Makefile
```sh
make install   # uv sync
make run       # start dev server
make test      # run tests
make docker    # docker compose up -d --build
```

## Configuration

All settings are controlled via environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `5000` | Server port |
| `REFRESH_INTERVAL` | `300` | Seconds between GitHub trending refreshes |
| `RATE_LIMIT` | `100 per minute` | Rate limit string (Flask-Limiter format) |

### Rate Limiting
The API is rate-limited to **100 requests per minute** per client (by IP).

## Todo
- [x] Host somewhere
- [x] Input validation on `count` parameter
- [x] Error handling in fetcher (keeps stale data on failure)
- [x] Rate limiting with Flask-Limiter
- [x] Test suite with pytest
- [x] Docker Compose support
- [x] Migrate to uv (no C-ext compilation needed)
- [ ] developers endpoint
- [ ] date endpoint
