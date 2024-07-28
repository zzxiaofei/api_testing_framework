import pytest


@pytest.fixture(scope='session', autouse=True)
def bai_du():
    print('-----登录百度页面-----')



