# 时间复杂度： O(n²)
# 空间复杂度：O(1)
# 稳定性   ：不稳定
def shell_sort(arr):
    n = len(arr)
    # 步长
    gap = n // 2

    # gap 变化到 0 之前，插入算法的次数
    while gap > 0:
        # 插入算法 ，步长替换原有的 1
        for i in range(gap, n):
            j = i
            # 从右到左从列表中去出第一个元素，和前一个对比，直到小于左边元素时，插入
            while j > 0 and j - gap >= 0:
                jv = arr[j]
                jv_gap = arr[j - gap]
                if jv < jv_gap:
                    arr[j], arr[j - gap] = arr[j - gap], arr[j]
                    j -= gap
                else:
                    break
            # print(arr)
        # 缩短步长
        print("步长：%d，列表：%s" % (gap, str(arr)))
        gap //= 2


list = [41, 23, 56, 34, 10, 69, 92, 88, 76, 5]

print(list)

shell_sort(list)

print(list)
