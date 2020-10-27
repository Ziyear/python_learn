class Person(object):
    """人"""

    def __init__(self, name):
        self.name = name
        self.gun = None
        self.hp = 100

    def anzhuang_zidan(self, danjia, zidan):
        """把子弹安装到弹夹中"""
        danjia.baocun_zidan(zidan)

    def anzhuang_danjia(self, gun, danjia):
        """把弹夹安装到抢中"""
        gun.anzhuang_danjia(danjia)

    def naqiang(self, gun):
        self.gun = gun

    def __str__(self):
        if self.gun:
            return "%s 的血量为：%d，枪的信息：%s" % (self.name, self.hp, str(self.gun))
        else:
            return "%s 的血量为：%d，他没有枪" % (self.name, self.hp)

    def biubiubiu(self, diren):
        # 发射子弹
        self.gun.fire(diren)
        pass


class Gun(object):
    """抢"""

    def __init__(self, name):
        self.name = name  # 用来记录抢的类型
        self.danjia = None

    def anzhuang_danjia(self, danjia):
        self.danjia = danjia

    def fire(self, diren):
        # 从弹夹获取子弹，击中敌人
        zi_dan = self.danjia.pop_zi_dan()
        if zi_dan:
            zi_dan.dazhong(diren)
        else:
            print("没有子弹了。。。")

    def __str__(self):
        if self.danjia:
            return "枪的名字:%s,弹夹信息:%s" % (self.name, str(self.danjia))
        else:
            return "枪的名字:%s,这把枪没有弹夹" % self.name


class DanJia(object):
    """弹夹"""

    def __init__(self, max_num):
        self.max_num = max_num  # 用来记录弹夹的最大容量
        self.zidan_list = []  # 记录子弹的引用

    def baocun_zidan(self, zidan):
        """保存子弹"""
        self.zidan_list.append(zidan)
        pass

    def pop_zi_dan(self):
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None

    def __str__(self):
        return "容量:%d/%d" % (len(self.zidan_list), self.max_num)


class ZiDan(object):
    """子弹"""

    def __init__(self, weili):
        self.weili = weili  # 用来记录子弹的威力

    def dazhong(self, person):
        person.hp -= self.weili


def main():
    # 1.创建老王
    laowang = Person("老王")
    # 2.创建一个抢
    ak47 = Gun("AK-47")
    # 3.创建一个弹夹
    danjia = DanJia(35)
    # 4.创建一个子弹
    for i in range(35):
        zidan = ZiDan(10)
        # 5.老王把子弹安装到弹夹
        laowang.anzhuang_zidan(danjia, zidan)
    # 6.老王把弹夹安装到抢上
    laowang.anzhuang_danjia(ak47, danjia)
    # 7.老王拿枪
    laowang.naqiang(ak47)
    print(laowang)
    # 8.创建一个敌人
    gebi_laosong = Person("隔壁老宋")
    print(gebi_laosong)
    # 9.老王打敌人
    laowang.biubiubiu(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.biubiubiu(gebi_laosong)
    print(laowang)
    print(gebi_laosong)
    laowang.biubiubiu(gebi_laosong)
    print(laowang)
    print(gebi_laosong)

if __name__ == '__main__':
    main()
