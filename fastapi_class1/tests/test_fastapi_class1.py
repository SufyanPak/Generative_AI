from fastapi.testclient import TestClient
from fastapi_class1.main import app


def test_fastapi_root():
    client = TestClient(app=app)
    response = client.get("/")
    assert response.status_code ==200
    assert response.json() == {"Hello":"World"}

def test_fastapi_root1():
    client = TestClient(app=app)
    response = client.get("/pi")
    assert response.status_code ==200
    assert response.json() == {"Hello":"PIAIC"}

# def test_fastapi_post():
#     items = {
#         "id" : 101,
#         "name" : "Sufyan",
#         "email" : "Sufyan.Phy@gmail.com"
#     }
#     client = TestClient(app=app)
#     response = client.post("/main", json=items)
#     assert response.status_code ==200
#     assert response.json() == {
#         "id" : 101,
#         "name" : "Sufyan",
#         "email" : "Sufyan.Phy@gmail.com"
#     }
#     assert response.json() == {
#         "detail": "Valid data is Entered"
#     }