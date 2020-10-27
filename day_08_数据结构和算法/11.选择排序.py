# 时间复杂度： O(n²)
# 空间复杂度：O(1)
# 稳定性   ：不稳定
def select_sort(list):
    n = len(list)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]


list = [41, 23, 56, 34, 10, 69, 92, 88, 76, 5]

print(list)

select_sort(list)

print(list)
