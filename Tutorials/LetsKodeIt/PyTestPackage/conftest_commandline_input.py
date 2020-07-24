'''
Need to Understand Better
'''


# import pytest
#
# @pytest.yield_fixture()
# def setUp():
#     print('Running conftest demo <METHOD SETUP>')
#     yield
#     print('Running conftest demo <METHOD TEARDOWN>')
#
# @pytest.yield_fixture(scope="module")
# def oneTimeSetUp(browser, osType):
#     print('Running conftest demo <MODULE ONE TIME SETUP>')
#     if browser == 'firefox':
#         print('Running test on Firefox')
#     else:
#         print('Running Test on Chrome')
#     yield
#     print('Running conftest demo <MODULE ONE TIME TEARDOWN>')
#
# def py_test_adoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--asType", help="Type of OS")
#
# @pytest.fixture(scope='session')
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope='session')
# def osType(request):
#     return request.config.getoption("--asType")
#
#
