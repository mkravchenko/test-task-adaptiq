from pytest import fixture

from airport_service.src.client import AeroportClient


@fixture(scope='session')
def aeroport_client():
    return AeroportClient()
