from fastapi.testclient import TestClient


def test_create_link(f_client: TestClient) -> None:
    res = f_client.post("/shorten", json={"url": "https://example.com"})
    assert res.status_code == 200
    assert "short_id" in res.json()


def test_stats(f_client: TestClient) -> None:
    res = f_client.post("/shorten", json={"url": "https://example.com"})
    short_id = res.json()["short_id"]

    stats = f_client.get(f"/stats/{short_id}")

    assert stats.status_code == 200
    assert stats.json()["clicks"] == 0


def test_redirect_and_stats(f_client: TestClient) -> None:
    res = f_client.post("/shorten", json={"url": "https://example.com"})
    short_id = res.json()["short_id"]

    f_client.get(f"/{short_id}")
    stats = f_client.get(f"/stats/{short_id}")

    assert stats.status_code == 200
    assert stats.json()["clicks"] == 1


def test_not_found(f_client: TestClient) -> None:
    res = f_client.get("/unknown")
    assert res.status_code == 404

