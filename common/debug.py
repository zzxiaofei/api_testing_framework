import json

# 假设 res.json() 的值如下
json_data = {'tag': {'id': 128, 'name': '"\\u6211\\u7684\\u6807\\u7b7e"'}}

# 获取 JSON 数据
data = json_data

# 提取 "name" 字段的值
tag_name = list(data['tag'].keys())[1]

# 打印结果
print(f"name 字段的值为: {tag_name}")
