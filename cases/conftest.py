import pytest


@pytest.fixture(scope='session', autouse=True)
def bai_du():
    print('-----开始执行测试用例-----')



