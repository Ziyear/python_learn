import random


def get_zhaoshi(zhaoshi):
    if zhaoshi == 0:
        return "石头"
    elif zhaoshi == 1:
        return "剪刀"
    elif zhaoshi == 2:
        return "布"
    return "BUG"


while True:
    player = int(input("请出招 0:石头,1:剪刀,2:布 :"))

    computer = random.randint(0, 2)

    common = "您出的是{0},电脑出的是{1}".format(get_zhaoshi(player), get_zhaoshi(computer))
    if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 3 and computer == 0):
        isContinue = int(input("你赢了，{0},是否继续，继续请按 1".format(common)))
        if isContinue != 1:
            break
    elif player == computer:
        isContinue = int(input("平局，{0}是否继续，继续请按 1".format(common)))
        if isContinue != 1:
            break
    else:
        isContinue = int(input("你输了，{0}是否继续，继续请按 1".format(common)))
        if isContinue != 1:
            break
