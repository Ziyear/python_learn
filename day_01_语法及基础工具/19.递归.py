# 1! = 1
# 2! = 2*1
# 3! = 3*2*1
# 4! = 4*3*2*1


# 递归一定要有最简条件 也就是一定要有出口
def get_nums(num):
    if num > 1:
        return num * get_nums(num - 1)
    else:
        return num


print(get_nums(5))
