import pytest
from website.app import create_app

@pytest.fixture()
def app():
    app = create_app()
    return app
