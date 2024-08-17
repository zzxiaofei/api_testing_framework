import mysql.connector
import requests
from data.config import DB_host, DB_user, DB_passwd, DB_database

"""
场景1：数据准备和清理
假设我们有一个接口用于查询用户的订单详情。为了测试该接口，我们需要数据库中存在一些订单记录。

"""

# 连接数据库
connection = mysql.connector.connect(
    host=DB_host,
    user=DB_user,
    password=DB_passwd,
    database=DB_database
)

cursor = connection.cursor()

# 插入测试数据
insert_query = ("INSERT INTO `hioc`.`isTester` (`id`, `uname`, `sex`, `birth`, `department`, `address`, `idoxu`) "
                "VALUES (15, 'idoxu', '0', NULL, NULL, NULL, '2020');")
cursor.execute(insert_query)
connection.commit()

# 运行接口测试
# ...（调用接口并验证响应）

# 测试完成后清理数据
delete_query = "DELETE FROM `hioc`.`isTester`where `id`=15;"
cursor.execute(delete_query)
connection.commit()

# 关闭连接
cursor.close()
connection.close()


"""
场景2：验证接口的实际影响

假设有一个接口用于更新订单的状态，我们希望确保接口调用后数据库中的状态更新正确。
"""

# 更新订单状态的接口
response = requests.post("http://api.example.com/update_order_status", json={
    "order_id": 1,
    "status": "shipped"
})

# 连接数据库
connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="test_db"
)

cursor = connection.cursor()

# 查询数据库，验证状态更新
select_query = "SELECT status FROM orders WHERE order_id = 1;"
cursor.execute(select_query)
result = cursor.fetchone()

# 验证数据库状态是否更新为 'shipped'
assert result[0] == "shipped", f"Expected status to be 'shipped', but got {result[0]}"

# 关闭连接
cursor.close()
connection.close()


"""
场景3：获取接口响应的预期结果

假设我们有一个接口返回用户的信息，我们需要确保响应的数据与数据库中的记录一致。
"""

# 获取用户信息的接口
response = requests.get("http://api.example.com/get_user_info", params={"user_id": 1001})
response_data = response.json()

# 连接数据库
connection = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="test_db"
)

cursor = connection.cursor()

# 查询数据库，获取预期的用户信息
select_query = "SELECT user_id, name, email FROM users WHERE user_id = 1001;"
cursor.execute(select_query)
db_data = cursor.fetchone()

# 验证接口响应与数据库数据一致
assert response_data['user_id'] == db_data[0], "User ID mismatch"
assert response_data['name'] == db_data[1], "Name mismatch"
assert response_data['email'] == db_data[2], "Email mismatch"

# 关闭连接
cursor.close()
connection.close()
