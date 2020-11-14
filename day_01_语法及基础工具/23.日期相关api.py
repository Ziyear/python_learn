import time

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

print('获取完整年份:' + time.strftime('%Y', time.localtime()))  # 获取完整年份
print('获取简写年份:' + time.strftime('%y', time.localtime()))  # 获取简写年份
print('获取月:' + time.strftime('%m', time.localtime()))  # 获取月
print('获取日:' + time.strftime('%d', time.localtime()))  # 获取日
print('获取年-月-日:' + time.strftime('%Y-%m-%d', time.localtime()))  # 获取年-月-日
print('获取时，24小时制:' + time.strftime('%H', time.localtime()))  # 获取时，24小时制
print('获取时，12小时制:' + time.strftime('%I', time.localtime()))  # 获取时，12小时制
print('获取分:' + time.strftime('%M', time.localtime()))  # 获取分
print('获取秒:' + time.strftime('%S', time.localtime()))  # 获取秒
print('获取时:分:秒:' + time.strftime('%H:%M:%S', time.localtime()))  # 获取时:分:秒
print('本地简化星期:' + time.strftime('%a', time.localtime()))  # 本地简化星期
print('本地完整星期:' + time.strftime('%A', time.localtime()))  # 本地完整星期
print('本地简化月份:' + time.strftime('%b', time.localtime()))  # 本地简化月份
print('本地完整月份:' + time.strftime('%B', time.localtime()))  # 本地完整月份
print('本地日期和时间表示:' + time.strftime('%c', time.localtime()))  # 本地日期和时间表示
print('一年中的第几天:' + time.strftime('%j', time.localtime()))  # 一年中的第几天
print('P.M等价符:' + time.strftime('%p', time.localtime()))  # P.M等价符
print('一年中的第几个星期，星期天为星期的开始:' + time.strftime('%U', time.localtime()))  # 一年中的第几个星期，星期天为星期的开始
print('星期几,星期天为星期的开始:' + time.strftime('%w', time.localtime()))  # 星期几,星期天为星期的开始
print('一年中的第几个星期，星期一为星期的开始:' + time.strftime('%W', time.localtime()))  # 一年中的第几个星期，星期一为星期的开始
print('本地日期表示:' + time.strftime('%x', time.localtime()))  # 本地日期表示
print('本地时间表示:' + time.strftime('%X', time.localtime()))  # 本地时间表示
print('当前时区:' + time.strftime('%Z', time.localtime()))  # 当前时区
print('输出%本身:' + time.strftime('%%', time.localtime()))  # 输出%本身
print('完整日期，时间，星期，时区:' + time.strftime('%Y-%m-%d %H:%M:%S %w-%Z', time.localtime()))  # 完整日期，时间，星期，时区

from datetime import datetime

print('当前时间:' + str(datetime.now()))
