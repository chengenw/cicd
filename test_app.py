from app import app


def test_home():
    client = app.test_client()
    res = client.get("/")
    # assert res.data == b"Hello from CI/CD 🚀"
    assert res.data.decode("utf-8") == "Hello from CI/CD 🚀"
    # assert False
