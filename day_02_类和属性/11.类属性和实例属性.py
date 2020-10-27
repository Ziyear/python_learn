class Tool(object):
    # 类属性
    num = 0

    # 方法
    def __init__(self, name):
        # 实例属性
        self.name = name
        # 操作雷属性
        Tool.num += 1


tool1 = Tool("铁球")

tool2 = Tool("铁棒")

tool3 = Tool("铁锹")

print(Tool.num)
