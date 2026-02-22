import pytest
from loan_app_cicd import app

# it will mimic like a server is running and we can send request to it
@pytest.fixture #it give developer ability to feed the data in these kind of simulation server
def client():
    return app.test_client()

def test_home(client):
    resp=client.get('/ping')
    assert resp.status_code==200

def test_predict(client):
    data={'Gender':"Male", 'Married':"Unmarried",'Credit_History' : "Unclear Debts",'ApplicantIncome':100000,'LoanAmount':2000000}
    resp=client.post('/predict',json=data)
    assert resp.status_code==200
    assert resp.json=={'loan_approval_status': 'Rejected'}