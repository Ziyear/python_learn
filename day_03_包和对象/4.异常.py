try:
    open("xxxx.txt")
    num = 1 / 0
    print("----1----")
except ZeroDivisionError:
    print("捕捉到异常了,ZeroDivisionError")
except FileNotFoundError:
    print("捕捉到异常了,FileNotFoundError")

print("----2----")
