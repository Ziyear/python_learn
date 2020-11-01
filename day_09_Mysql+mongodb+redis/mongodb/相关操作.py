from pymongo import *

# 创建连接
client = MongoClient('mongodb://ali.ziyear.com:27017/')
# 切换数据库
db_py = client.py
# 获取集合
stu = db_py.stu

# 增加
for i in range(10):
    stu.insert_one({"name": "zhang" + str(i), "age": i + 9})

# 修改
# stu.update_one({"name": "张三丰"}, {'$set': {"name": "abc"}})

# 删除
# stu.delete_one({"name": "abc"})
#
# 查询
all = stu.find()

for item in all:
    print(str(item))

print("############")
cursor = stu.find({'age': {'$gt': 15}}).sort('age', -1).skip(1).limit(2)
for item in cursor:
    print(str(item))
