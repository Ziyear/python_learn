import re


def print_match_result(ret):
    if ret:
        print("匹配 : %s" % ret.group())
    else:
        print("不匹配")


# 查找
ret = re.search(r"\d+", "阅读量 999")
print_match_result(ret)

# 查找全部
ret = re.findall(r"\d+", "python = 97 c = 88 ,java=99")

print(ret)

# 替换
ret = re.sub(r"\d+", "100", "python = 97 c = 88 ,java=99")

print(ret)


def replace(result):
    print(result.group())
    return str(int(result.group()) + 50)


# 函数过滤替换
ret = re.sub(r"\d+", replace, "python = 97 c = 88 ,java=99")
print(ret)
