# 时间复杂度: O(n²)
# 空间复杂度: O(1)
# 稳定性   ：稳定
def bubble_sort(list):
    n = len(list)
    for i in range(n - 1):
        count = 0
        for j in range(0, n - i - 1):
            jv = list[j]
            j_1_v = list[j + 1]
            if jv > j_1_v:
                list[j], list[j + 1] = list[j + 1], list[j]
                count += 1
        if count == 0:
            return


list = [41, 23, 56, 34, 10, 69, 92, 88, 76, 5]

bubble_sort(list)

print(list)
