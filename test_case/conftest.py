import pytest
import requests
import sys
from os.path import dirname, join

sys.path.append(dirname(dirname(__file__)))
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
    res_json = res.json()
    return res, res_json, res_json['access_token']
