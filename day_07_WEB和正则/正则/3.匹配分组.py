# |             匹配左右任意一个表达式
# (ab)          将括号中字符作为一个分组
# \num          引用分组num匹配到的字符
# (?P<name>)    分组起别名
# (?P=name)     引用别名为name的分组匹配到字符串
import re


def match_mail(source):
    """ 匹配邮箱 """
    ret = re.match(r"(^\w+)@(163|126|gmail|qq)\.(com|cn|net)$", source)
    if ret:
        print("%s:匹配" % source)
        print("匹配的分组信息:%s" % ret.group(1))
    else:
        print("%s:不匹配" % source)


def match_HTML():
    """ \num (?P<name>)  应用 """
    source = "<html><h1>ziyear</h1></html>"
    # ret = re.match(r"<.+><.+>.*</.+></.+>", source)
    # ret = re.match(r"<(.+)><(.+)>.*</\2></\1>", source)
    ret = re.match(r"<(?P<key1>.+)><(?P<key2>.+)>.*</(?P=key2)></(?P=key1)>", source)
    if ret:
        print("%s:匹配" % source)
    else:
        print("%s:不匹配" % source)


def match_H1(source):
    """ ‘(ab)’ 的应用"""
    ret = re.match(r"<h1>(.*)</h1>", source)

    if ret:
        print("%s:匹配" % source)
        print("匹配的分组信息:%s" % ret.group(1))
    else:
        print("%s:不匹配" % source)


def match_0_100(source):
    """ ‘|’ 的应用"""
    ret = re.match(r"[1-9]\d?$|0$|100$", source)
    if ret:
        print("%s:匹配" % source)
    else:
        print("%s:不匹配" % source)


def main():
    match_0_100("100")
    match_H1("<h1>我是一级标题</h1>")
    match_HTML()
    match_mail("1369090@qq.com")


if __name__ == '__main__':
    main()
