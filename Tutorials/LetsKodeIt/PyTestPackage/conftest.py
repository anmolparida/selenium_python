import pytest

@pytest.yield_fixture()
def setUp():
    print('Running conftest demo <METHOD SETUP>')
    yield
    print('Running conftest demo <METHOD TEARDOWN>')

@pytest.yield_fixture(scope="class")
def oneTimeSetUp():
    print('Running conftest demo <MODULE ONE TIME SETUP>')
    yield
    print('Running conftest demo <MODULE ONE TIME TEARDOWN>')



