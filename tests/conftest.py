import pytest
from website.app import Website

@pytest.fixture()
def app():
    app = Website()
    return app.website
