# 1.打印目录
def show_menu():
    print("=" * 50)
    print("     名字管理系统 V1.0")
    print(" 1、查询所有名片")
    print(" 2、查询一个名片")
    print(" 3、添加一个名片")
    print(" 4、修改一个名片")
    print(" 5、删除一个名片")
    print(" 6、保存信息")
    print(" 0、退出系统")
    print("=" * 50)


def isNumber(c):
    return c >= '0' and c <= '9'


def add(card_infos):
    new_name = input("请输入一个名字：")
    new_age = input("请输入年龄：")
    new_sex = input("请输入性别：")
    new_mobile = input("请输入手机号码：")

    new_card = {}
    new_card["id"] = str(len(card_infos) + 1)
    new_card["name"] = new_name
    new_card["age"] = new_age
    new_card["sex"] = new_sex
    new_card["mobile"] = new_mobile
    card_infos.append(new_card)


# 用来存储名片信息
card_infos = []


def show_all(card_infos):
    print("id\t姓名\t年龄\t性别\t电话")
    for temp in card_infos:
        print("%s\t%s\t%s\t\t%s\t\t%s\t" % (temp["id"], temp["name"], temp["age"], temp["sex"], temp["mobile"]))


def show_by_nam(card_infos):
    name = input("请输入你要查询的姓名：")
    show_items = []
    for item in card_infos:
        if item["name"] == name:
            show_items.append(item)
    if len(show_items) != 0:
        show_all(show_items)


def update(card_infos):
    show_all(card_infos)
    id = input("请输入你要修改的学生的id：")
    is_update = False
    for item in card_infos:
        if item["id"] == id:
            new_name = input("请输入一个名字：")
            new_age = input("请输入年龄：")
            new_sex = input("请输入性别：")
            new_mobile = input("请输入手机号码：")
            item["name"] = new_name
            item["age"] = new_age
            item["sex"] = new_sex
            item["mobile"] = new_mobile
            is_update = True
    if not is_update:
        print("您输入的id：%s 不存在！" % id)
    show_all(card_infos)


def delete(card_infos):
    show_all(card_infos)
    id = input("请输入你要删除的学生id：")
    for item in card_infos:
        if item["id"] == id:
            card_infos.remove(item)
    show_all(card_infos)


def continue_buf():
    input("按任意键继续")


def save_2_file():
    f = open("backup.data", "w")
    f.write(str(card_infos))
    f.close()


def read_2_file():
    try:
        f = open("backup.data")
        global card_infos
        card_infos = eval(f.read())
        f.close()
    except Exception:
        pass


def main():
    read_2_file()
    while True:
        show_menu()
        num = input("请输入你要使用的功能序号：")
        if isNumber(num):
            num = int(num)
        else:
            print("您的输入：%s 有误! 请重新输入！" % num)
            continue_buf()
            continue
        if num == 1:
            show_all(card_infos)
            continue_buf()
        elif num == 2:
            show_by_nam(card_infos)
            continue_buf()
        elif num == 3:
            add(card_infos)
            continue_buf()
        elif num == 4:
            update(card_infos)
            continue_buf()
        elif num == 5:
            delete(card_infos)
            continue_buf()
        elif num == 6:
            save_2_file()
        elif num == 0:
            print("bye")
            break
        else:
            print("您的输入有误! 请重新输入！")
            continue_buf()
            continue


if __name__ == '__main__':
    main()
