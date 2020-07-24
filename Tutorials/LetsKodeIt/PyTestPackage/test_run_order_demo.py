"""
http://pytest-ordering.readthedocs.io/en/develop/

-- test are not run alphabetically but the time they are found
"""

import pytest

# Order of Run B A E C D F
@pytest.mark.run(order=4)
def test_run_order_methodF(oneTimeSetUp, setUp):
    print('Running Method F')

@pytest.mark.run(order=1)
def test_run_order_methodB(oneTimeSetUp, setUp):
    print('Running Method B')

# Order not Set - Runs 2nd last
def test_run_order_methodC(oneTimeSetUp, setUp):
    print('Running Method C')

# Order not Set - Runs last
def test_run_order_methodD(oneTimeSetUp, setUp):
    print('Running Method D')


@pytest.mark.run(order=2)
def test_run_order_methodA(oneTimeSetUp, setUp):
        print('Running Method A')

@pytest.mark.run(order=3)
def test_run_order_methodE(oneTimeSetUp, setUp):
    print('Running Method E')

