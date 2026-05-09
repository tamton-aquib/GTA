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

## Usage

### Docker
```sh
docker build -t gta .
docker run -p 5000:5000 gta:latest
```

### Docker Compose
```sh
docker compose up -d
```

### Development
```sh
pip install -r requirements.txt
flask run
```

### Testing
```sh
pytest
```

### Rate Limiting
The API is rate-limited to **100 requests per minute** per client (by IP).

## Todo
- [x] Host somewhere
- [x] Input validation on `count` parameter
- [x] Error handling in fetcher (keeps stale data on failure)
- [x] Rate limiting with Flask-Limiter
- [x] Test suite with pytest
- [x] Docker Compose support
- [ ] developers endpoint
- [ ] date endpoint
