# GTA
Github Trending API

> [!Note]
> The endpoint is at: https://github-trending.onrender.com

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

## Todo
- [x] Host somewhere
- [ ] developers endpoint
- [ ] language endpoint
- [ ] date endpoint
