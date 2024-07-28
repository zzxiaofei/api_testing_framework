import pytest


@pytest.fixture(scope='session', autouse=True)
def begin():
    print('----前置操作----')

    yield
    print('----后置操作----')


"""
    yield:
    
"""