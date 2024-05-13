import mysql.connector
import random
from datetime import datetime, timedelta

# 连接到 MySQL 数据库
mydb = mysql.connector.connect(
    host="192.168.11.196",
    user="root",
    password="1136623363Bx.",
    database="WATERMARK"
)


# 创建一个指向数据库的游标
mycursor = mydb.cursor()

# 随机生成数据并插入表中
for _ in range(100):  # 生成 100 条数据
    openId = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
    join_date = datetime.now() - timedelta(days=random.randint(0, 365))  # 365 天内的随机日期
    total_num = random.randint(1, 1000)
    last_use_time = datetime.now() - timedelta(days=random.randint(0, 30))  # 30 天内的随机时间

    # 插入数据
    sql = "INSERT INTO USER_INFO (openId, join_date, total_num, last_use_time) VALUES (%s, %s, %s, %s)"
    val = (openId, join_date, total_num, last_use_time)
    mycursor.execute(sql, val)

# 提交更改
mydb.commit()

# 打印插入的行数
print(mycursor.rowcount, "record(s) inserted.")
