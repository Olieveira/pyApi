"""Módulo principal da API."""

from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/repos/{username}")
async def get_repos(username: str):
    """
    Retorna uma lista de repositórios públicos de um usuário do GitHub.

    Args:
        username (str): Nome de usuário do GitHub.

    Returns:
        list: Lista de dicionários contendo o nome e a URL dos repositórios.
    """
    url = f"https://api.github.com/users/{username}/repos"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()  # Garante que erros HTTP sejam tratados
        data = response.json()

    return [
        {"name": repo["name"], "url": repo["html_url"]}
        for repo in data
    ]
