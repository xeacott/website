"""
Basic config tests.
"""
import pytest


def test_config(app):
    assert not app.debug, 'Ensure the app not in debug mode'
