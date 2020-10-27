# 时间复杂度： O(nlog2n)
# 空间复杂度： O(nlog2n)
# 稳定性   ：不稳定
def fast_sort(arr, first, last):
    if first >= last:
        return
    mid_value = arr[first]
    low = first
    high = last

    while low < high:
        # 右侧指针必须大于左侧 如果 右侧值小于中间值的情况下，退出循环，否则右侧指针减小
        while low < high and arr[high] >= mid_value:
            high -= 1
        # 将 小于中间值的放到左侧
        arr[low] = arr[high]

        # 右侧指针必须大于左侧 如果 左侧值大于中间值的情况下，退出循环，否则左侧指针增小
        while low < high and arr[low] < mid_value:
            low += 1
        # 将 大于中间值的放到右侧
        arr[high] = arr[low]
    # 将中间值给到最低位
    arr[low] = mid_value

    fast_sort(arr, first, low - 1)
    fast_sort(arr, low + 1, last)


list = [41, 23, 56, 34, 10, 69, 92, 88, 76, 5]

print(list)

fast_sort(list, 0, len(list) - 1)

print(list)
