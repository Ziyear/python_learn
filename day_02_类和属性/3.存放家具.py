class Home:
    def __init__(self, area, info, addr):
        self.area = area
        self.info = info
        self.addr = addr
        self.leftArea = area
        self.containItems = []

    def __str__(self):
        msg = "房子面积是：%d，可用面积是：%d，户型是：%s，地址是：%s " % (self.area, self.leftArea, self.info, self.addr)
        msg += " 当前房子里的物品有：%s" % self.containItems
        return msg

    def addItem(self, item):
        self.leftArea -= item.area
        self.containItems.append(item.name)


class Bed:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s占用的面积是：%d" % (self.name, self.area)


fangzi = Home(129, "三室一厅", "杭州")
print(fangzi)

bed1 = Bed("席梦思", 4)
print(bed1)
bed2 = Bed("三人床", 4)
print(bed2)

fangzi.addItem(bed1)
fangzi.addItem(bed2)
print(fangzi)
