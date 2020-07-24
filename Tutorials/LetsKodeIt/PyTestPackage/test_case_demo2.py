'''
@pytest.fixture == @pytest.yield_fixture()
Both can be used w/o the yield method

yield is optional
'''

import pytest


@pytest.fixture()
def setUp1():
    print('Once BEFORE METHOD - pytest.fixture')
    yield
    print('Once AFTER METHOD - pytest.fixture')

@pytest.yield_fixture()
def setUp2():
    print('Once BEFORE every method - pytest.yield_fixture')
    yield
    print('Once AFTER every method - pytest.yield_fixture')


def test_methodA(setUp1):
    print('Running method A')

def test_methodB(setUp2):
    print('Running Method B')