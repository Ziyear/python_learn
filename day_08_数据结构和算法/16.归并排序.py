# 时间复杂度： O(nlog2n)
# 空间复杂度： O(n)
# 稳定性   ：稳定
def merge_sort(list):
    # 获取数组长度
    n = len(list)
    if n <= 1:
        return list
    mid = n // 2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    # 将两个有序的子序列合并成一个整体
    left_pointer, right_pointer = 0, 0
    result = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result += left[left_pointer:]
    result += right[right_pointer:]
    return result


if __name__ == '__main__':
    li = [19, 27, 11, 39, 58, 76, 31]

    sort = merge_sort(li)
    print(li)
    print(sort)
