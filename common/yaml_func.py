import requests
import os
import yaml

params = {
    "limit": 1,
    "tab": "share"
}
url = 'http://42.192.6.197:3000/api/v1/topics'
res = requests.request('GET', url=url, params=params)
"""响应值字典转换为json字符串"""
# print(type(res.json()))
# response = json.dumps(res.json(), ensure_ascii=False, indent=4)
# print(type(response))
"""json字符串转换为字典"""
# response = json.loads(response)
# print(type(response))


"""
读取YAML文件的方法
"""

# current_dir = os.path.dirname(os.path.abspath(__file__))
# print(current_dir)


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data
