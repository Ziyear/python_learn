# 时间复杂度： O(n²)
# 空间复杂度：O(1)
# 稳定性   ：稳定
def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        # 从右到左从列表中去出第一个元素，和前一个对比，直到小于左边元素时，插入
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


list = [41, 23, 56, 34, 10, 69, 92, 88, 76, 5]

print(list)

insert_sort(list)

print(list)
