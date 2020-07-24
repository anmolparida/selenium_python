'''
run from terminal :

py.test <no filename>>: runs all files. Does not print if everything passes, prints if fails
py.test filename.py: does not print if everything passes, prints if fails
py.test filename.py-v -s : prints the statements

'''

import pytest

@pytest.fixture()
def setUp():
    print(' setUp -Once before every method')

def test_methodA(setUp):
    print('Running Method A')

def test_methodB(setUp):
    print('Running Method B')

