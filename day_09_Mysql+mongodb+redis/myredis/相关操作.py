from redis import *

r = StrictRedis(host='ali.ziyear.com', port=6379, password='ZIYEAR@123456')

# 写
pipe = r.pipeline()
pipe.set("py01", "hello")
pipe.set("py02", "python")
pipe.set("py03", "redis")
pipe.execute()

# 读
temp = r.get('py01')
print(temp)

