from loan_app import app
import json

@pytest.fixture
def client():
    return app.test_client