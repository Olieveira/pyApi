from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/repos/{username}")
async def get_repos(username: str):
    url = f"https://api.github.com/users/{username}/repos"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    
    return [
        {
            "name": repo["name"],
            "url": repo["html_url"]
        }
        for repo in data
    ]
