import pytest

from core.client import PetApi
from core import settings


def pytest_collection_modifyitems():
    if not settings.configured:
        settings.configure()
    return settings


@pytest.fixture(scope='session')
def pet_client() -> 'PetApi':
    return PetApi(settings.host, settings.user, settings.password)
