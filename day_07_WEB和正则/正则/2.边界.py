# ^   字符串开始
# $   字符串结尾
# \b  匹配一个单词的边界
# \B  匹配非单词边界
import re

print(re.match(r"^1[35678]\d{9}$", "18000000000"))

print(re.match(r"^\w+ve", "hover"))

# ve 不在单词边界
print(r"re.match(^\w+ve\b, hover):   " + str(re.match(r"^\w+ve\b", "hover")))
print(r"re.match(^\w+ve\B, hover):   " + str(re.match(r"^\w+ve\B", "hover")))

print(r"re.match(^\w+ve\b, love):   " + str(re.match(r"^\w+ve\b", "love")))
