def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert "repositories" in data
    assert "random" in data


def test_repositories(client):
    resp = client.get("/repositories")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert len(data) == 3


def test_repositories_count(client):
    resp = client.get("/repositories?count=2")
    assert resp.status_code == 200
    data = resp.get_json()
    assert len(data) == 2


def test_repositories_invalid_count(client):
    resp = client.get("/repositories?count=abc")
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_repositories_negative_count(client):
    resp = client.get("/repositories?count=-1")
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_repositories_excessive_count(client):
    resp = client.get("/repositories?count=999")
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_random(client):
    resp = client.get("/random")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, dict)


def test_random_count(client):
    resp = client.get("/random?count=2")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert len(data) == 2


def test_random_invalid_count(client):
    resp = client.get("/random?count=abc")
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_random_negative_count(client):
    resp = client.get("/random?count=-1")
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_random_excessive_count(client):
    resp = client.get("/random?count=999")
    assert resp.status_code == 400
    assert "error" in resp.get_json()


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"
    assert isinstance(data["cached_repos"], int)


def test_trailing_slash_redirect(client):
    resp = client.get("/repositories/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
