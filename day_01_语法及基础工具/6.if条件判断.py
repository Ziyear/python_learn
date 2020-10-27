you = input("你去吗？")
youWife = input("你老婆去吗？")

if you == '去' and youWife == '去':
    print("你们都去")

if you == '去' or youWife == '去':
    print("你们至少有一个人去")

age = int(input("请输入你的年龄："))

if not (age > 0 and age < 50):
    print("你的年龄不在 0-50 中间")
else:
    print("你的年龄在 0-50 中间")

sex = input("请输入你的性别")

if "男" == sex:
    print("你是男性，可以留胡子呢")
elif "女" == sex:
    print("你是女性，可以穿裙子呢")
else:
    print("性别未知，请重新输入！！！！")
