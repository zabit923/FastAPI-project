from httpx import AsyncClient


async def test_add_specific_operations(ac: AsyncClient):
    response = await ac.post("/operations", json={
        "id": 1,
        "quantity": "string",
        "figi": "string",
        "instrument_type": "string",
        "date": "2024-06-30T17:10:14.689",
        "type": "string"
    })

    assert response.status_code == 200


async def test_get_specific_operations(ac: AsyncClient):
    response = await ac.get("/operations", params={
        "operation_type": "string",
    })

    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert len(response.json()["data"]) == 1
