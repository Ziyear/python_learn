from pymongo import *

# 创建连接
client = MongoClient('mongodb://ali.ziyear.com:27017/')
# 切换数据库
db_py = client.py
# 获取集合
stu = db_py.stu

# 增加
# stu.insert_one({"name": "张三丰", "age": 19})

#修改
stu.update_one({"name": "张三丰"}, {'$set': {"name": "abc"}})
