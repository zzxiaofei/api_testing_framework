import requests
import json
import pytest
import yaml
from common.yaml_func import read_yaml
import os

# 获取 YAML 文件的绝对路径 '../data/wechat.yaml'
yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'wechat.yaml')
print(yaml_path)

yaml_data = read_yaml(yaml_path)
tags = [f'"{tags}"' for tags in yaml_data['create']['tags']['name']]


class TestWeixin:

    def test_get_access_token(self, get_access_token):
        res, res_json, res_json['access_token'] = get_access_token
        # print("In test_get_access_token_response - Response JSON:", res_json)
        # print("In test_get_access_token_response - Access Token:", res_json['access_token'])
        # print("In test_get_access_token_response - get_access_token:", get_access_token)
        assert res.status_code == 200
        assert 7200 == res_json['expires_in']
        assert res.elapsed.total_seconds() < 3

    # @pytest.mark.skip
    @pytest.mark.parametrize('value', tags)
    def test_create_tag(self, get_access_token, value):
        res, res_json, res_json['access_token'] = get_access_token
        url = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token={access_token}'.format(
            access_token=get_access_token[2])
        data = {"tag": {"name": value}}
        res = requests.post(url, json=data)
        assert 200 == res.status_code
        assert 'name' == list(res.json()['tag'].keys())[1]

    def test_create_tag_f_errortoken(self):
        url = 'https://api.weixin.qq.com/cgi-bin/tags/create?access_token=1111'
        res = requests.get(url)
        assert 200 == res.status_code
        assert 40001 == res.json()['errcode']


# @pytest.fixture()
# def get_tag(get_access_token):
#     url = 'https://api.weixin.qq.com/cgi-bin/tags/get?access_token={access_token}'.format(
#         access_token=get_access_token)
#     res = requests.get(url)
#     # print(res.json())
#     data_json_tag = res.json()
#     data_list_tag = [tag['id'] for tag in data_json_tag['tags']]
#     print(data_list_tag)
#     assert 200 == res.status_code
#     assert 'tags' in res.json()
#     return data_list_tag


# @pytest.fixture(scope='module')
# def shared_data():
#     return {}


# def test_get_tag(get_access_token):


# def test_update_tag(get_access_token, shared_data):
#     url = 'https://api.weixin.qq.com/cgi-bin/tags/update?access_token={access_token}'.format(
#         access_token=get_access_token)
#     print(shared_data)
#     data = {"tag": {"id": shared_data[-3], "name": "shanxi"}}
#     res = requests.post(url, json=data)
#     print(res.json())
# data_json_tag = res.json()
# data_list_tag = [tag['id'] for tag in data_json_tag['tags']]
# print(data_list_tag)
# assert 200 == res.status_code
# assert 'tags' in res.json()


if __name__ == '__main__':
    pytest.main(['-s', 'test_weixin.py'])
