# .     表示任意字符 不包括 \n
# []    匹配列举的字符
# \d    匹配数字 0-9
# \D    匹配非数字，既不是数字
# \s    匹配空白，即空格，tab 键
# \S    匹配非空白
# \w    匹配单词字符 即a-z A-Z 0-9 _
# \W    匹配非单词字符

import re

print("###########  单一字符  ###############")
print(".:" + str(re.match(".", "a")))
print("[a-z]:" + str(re.match('[a-z]', "de")))
print("[^123]:" + str(re.match('[^123]', "456")))
print("[^a-z]:" + str(re.match('[^a-z]', "123")))
print("\d:" + str(re.match("\d", "189")))
print("\D:" + str(re.match("\D", "haha")))
print("\s:" + str(re.match("\s", " ")))
print("\S:" + str(re.match("\S", "haha")))
print("\w:" + str(re.match("\w", "a_a")))
print("\W:" + str(re.match("\W", "-")))

print("###########  表示数量  ###############")

# *       可有可无
# +       至少有一次
# ？      一次或零次
# {m}     出现m次
# {m,}    至少出现m次
# {m,n}   出现m到n次

print("*    :" + str(re.match(".*", "hahhah")))
print("+    :" + str(re.match(".+", "123")))
print("？   :" + str(re.match(".?", "haha-ahahah")))
print("{m}  :" + str(re.match(".{2}", "hahha")))
print("{m.} :" + str(re.match(".{3,}", "nihao")))
print("{m,n}:" + str(re.match(".{3,5}", "ninininini")))

print("###########  转义字符  ###############")
print("\\nabc :" + str(re.match("\\\\nabc", "\\nabc")))
print("\\nabc :" + str(re.match(r"\\nabc", r"\nabc")))
