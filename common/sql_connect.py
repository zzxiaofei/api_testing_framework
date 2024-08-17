import mysql.connector
from data.config import DB_host, DB_user, DB_passwd, DB_database

# 连接数据库
connection = mysql.connector.connect(
    host=DB_host,
    user=DB_user,
    passwd=DB_passwd,
    database=DB_database
)
cursor = connection.cursor()
# 插入测试数据
insert_query = ("INSERT INTO isTester (`id`, `uname`, `sex`, `birth`, `department`, `address`, `idoxu`) VALUES (15, "
                "'idoxu', '0', NULL, NULL, NULL, '2020');")

cursor.execute(insert_query)
connection.commit()

#测试完成清理数据
delete_query = "DELETE FROM isTester WHERE `id`=15;"
cursor.execute(delete_query)
connection.commit()

cursor.close()
connection.close()
