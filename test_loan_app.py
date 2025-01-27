from loan_app import app
import json
import pytest

@pytest.fixture
def client():
    return app.test_client()