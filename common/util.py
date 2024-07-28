import requests
import json

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
