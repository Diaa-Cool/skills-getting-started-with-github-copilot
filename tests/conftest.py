import pytest
import copy
from fastapi.testclient import TestClient
from src.app import app, activities

# Store initial activities state
INITIAL_ACTIVITIES = copy.deepcopy(activities)

@pytest.fixture
def client():
    """Fixture for FastAPI TestClient"""
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_activities():
    """Automatically reset activities to initial state before each test"""
    activities.clear()
    activities.update(copy.deepcopy(INITIAL_ACTIVITIES))
    yield
    # Reset after test as well
    activities.clear()
    activities.update(copy.deepcopy(INITIAL_ACTIVITIES))
