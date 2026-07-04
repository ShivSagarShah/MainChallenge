"""
tests/conftest.py
─────────────────────────────────────────────────────────────────────────────
Shared pytest fixtures for the Culture Compass test suite.
"""
import sys
import os

import pytest

# Ensure project root is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from data.destinations import DESTINATION_MAP


@pytest.fixture(scope="session")
def base_prefs() -> dict:
    """Standard solo traveller preferences used across multiple test classes."""
    return dict(
        traveller_type    = "solo",
        interests         = ["history", "food"],
        budget_level      = 2,
        month             = 4,
        wants_hidden_gems = False,
    )


@pytest.fixture(scope="session")
def gem_prefs() -> dict:
    """Hidden-gem-seeking backpacker preferences."""
    return dict(
        traveller_type    = "backpacker",
        interests         = ["food", "craft"],
        budget_level      = 1,
        month             = 5,
        wants_hidden_gems = True,
    )


@pytest.fixture(scope="session")
def luxury_prefs() -> dict:
    """Luxury couple preferences."""
    return dict(
        traveller_type    = "couple",
        interests         = ["art", "architecture", "food"],
        budget_level      = 4,
        month             = 10,
        wants_hidden_gems = False,
    )


@pytest.fixture(scope="session")
def kyoto() -> dict:
    return DESTINATION_MAP["kyoto"]


@pytest.fixture(scope="session")
def tbilisi() -> dict:
    return DESTINATION_MAP["tbilisi"]


@pytest.fixture(scope="session")
def plovdiv() -> dict:
    return DESTINATION_MAP["plovdiv"]


@pytest.fixture(scope="session")
def all_destinations() -> list:
    from data.destinations import DESTINATIONS
    return DESTINATIONS
