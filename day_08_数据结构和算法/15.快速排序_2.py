# 时间复杂度： O(n²)
# 空间复杂度：O(1)
# 稳定性   ：不稳定
def partition(A, l, r):
    pivot = A[r]  # 选取最后一个元素作为 pivot
    i = l - 1  # i 是慢指针
    for j in range(l, r):  # j 是快指针，终止位置在数组倒数第二位置
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A, l, r):
    if l < r:
        pivot_index = partition(A, l, r)
        quick_sort(A, l, pivot_index - 1)
        quick_sort(A, pivot_index + 1, r)


list = [41, 23, 56, 34, 10, 69, 92, 88, 76, 5]

print(list)

quick_sort(list, 0, len(list) - 1)

print(list)
