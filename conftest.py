import pytest

"""
工程目录下的conftest作用于全局，不同测试子目录也可以放，但只在该层级及以下生效
"""


@pytest.fixture(scope='session', autouse=True)
def begin():
    print('----前置操作----')

    yield
    print('----后置操作----')


"""
    yield:
    
"""
