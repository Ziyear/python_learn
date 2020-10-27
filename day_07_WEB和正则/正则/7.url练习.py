import re

sourcce = """
https://www.runoob.com/regexp/regexp-syntax.html
http://www.sojson.com/regex/generate
https://recomm.cnblogs.com/blogpost/13337486
https://fanyi.baidu.com/?aldtype=16047#auto/zh
https://www.zhihu.com/hot
"""
for s in sourcce.split("\r\n"):
    sub = re.sub(r"(http(s?)://.+?/).*", lambda x: x.group(1), s)
    print(sub)
