import pytest
from httpx import AsyncClient
from src.main import app

@pytest.mark.asyncio
async def test_get_moedas():
    """Test the /moedas endpoint."""
    async with AsyncClient(base_url="http://test") as client:
        response = await client.get("/moedas")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_moedas_by_id():
    """Test the /moedas/{id} endpoint."""
    async with AsyncClient(base_url="http://test") as client:
        response = await client.get("/moedas/bitcoin")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["id"] == "bitcoin"

@pytest.mark.asyncio
async def test_get_nfts():
    """Test the /nfts endpoint."""
    async with AsyncClient(base_url="http://test") as client:
        response = await client.get("/nfts")
        assert response.status_code == 200
        assert isinstance(response.json(), list)
 
@pytest.mark.asyncio
async def test_nfts_by_id():
    """Test the /nfts/{id} endpoint."""
    async with AsyncClient(base_url="http://test") as client:
        response = await client.get("/nfts/hashmasks")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["id"] == "hashmasks"

@pytest.mark.asyncio
async def test_api_server():
    """Test the external API server."""
    async with AsyncClient() as client:
        response = await client.get("https://api.coingecko.com/api/v3/ping")
        assert response.status_code == 200
