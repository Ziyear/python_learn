class Game(object):
    # 类属性
    num = 0

    # 实例方法
    def __init__(self, name):
        # 实例属性
        self.name = name

    # 类方法
    @classmethod
    def add_num(cls):
        # 操作类属性
        cls.num += 1

    # 静态方法
    @staticmethod
    def print_menu():
        print("---------------------")
        print("     穿越火线V1.0.0")
        print(" 1.开始游戏")
        print(" 2.结束游戏")
        print("---------------------")


game = Game("LOL")
Game.add_num()
game.add_num()
print(Game.num)
print(game.num)

Game.print_menu()
game.print_menu()
