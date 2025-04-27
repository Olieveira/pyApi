"""Módulo principal da API."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()
base = "https://api.coingecko.com/api/v3/"

@app.get("/moedas")
async def get_moedas():
    """
    Retorna informações de todas as moedas da API.

    Returns:
        list: Dados das moedas retornados pela API CoinGecko.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(base + "coins/list")
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        return JSONResponse(status_code=503, content={"erro": "Serviço indisponível", "detalhes": str(e)})

@app.get("/moedas/{id}")
async def moedas_by_id(id: str):
    """
    Retorna informações sobre uma moeda específica.

    Args:
        id (str): ID da moeda.

    Returns:
        dict: Dados da moeda retornados pela API CoinGecko.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(base + f"coins/{id}")
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        return JSONResponse(status_code=503, content={"erro": "Serviço indisponível", "detalhes": str(e)})
    
@app.get("/nfts")
async def get_nfts():
    """
    Retorna informações sobre todos os NFTs.

    Returns:
        list: Dados dos NFTs retornados pela API CoinGecko.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(base + "nfts/list")
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        return JSONResponse(status_code=503, content={"erro": "Serviço indisponível", "detalhes": str(e)})

@app.get("/nfts/{id}")
async def nfts_by_id(id: str):
    """
    Retorna informações sobre um NFT específico.

    Args:
        id (str): ID do NFT.

    Returns:
        dict: Dados do NFT retornados pela API CoinGecko.
    """

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(base + f"nfts/{id}")
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        return JSONResponse(status_code=503, content={"erro": "Serviço indisponível", "detalhes": str(e)})