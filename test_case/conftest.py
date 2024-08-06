import pytest
import requests
from common.yaml_func import read_yaml


@pytest.fixture(scope='session', autouse=True)
def bai_du():
    print('-----开始执行测试用例-----')


@pytest.fixture(scope='session', autouse=True)
def config_data():
    return read_yaml('../data/data.yaml')


@pytest.fixture(scope='session', autouse=True)
def get_access_token(config_data):
    test_appid = config_data['wechat']['appid']
    test_secret = config_data['wechat']['secret']
    # print(test_appid, test_secret)
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={test_appid}&secret={test_secret}'.format(
        test_appid=test_appid, test_secret=test_secret)
    # print('url: {url}'.format(url=url))
    res = requests.get(url)
    # assert 200 == res.status_code
    res_json = res.json()
    # assert 7200 == res_json['expires_in']
    # assert res.elapsed.total_seconds() < 3
    return res_json['access_token']
