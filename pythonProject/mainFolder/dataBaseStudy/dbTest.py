# -*- coding: UTF-8 -*-


import pymysql#pymysql是包名


config = dict(host='47.94.251.62', user='root', password='root', database='standingBook')  # 构造函数
# 建立数据库连接
db = pymysql.connect(host=config['host'], user=config['user'], password=config['password'], database=config['database'])


try:
    cursor = db.cursor()
    # sql
    sql_so = "SELECT * FROM lr_base_invoice order by id"
    cursor.execute(sql_so)
    result = cursor.fetchall()
    for record in result:
        print(record)
except Exception:print("查询失败")

# 关闭数据库连接
db.close()
print('finish')
