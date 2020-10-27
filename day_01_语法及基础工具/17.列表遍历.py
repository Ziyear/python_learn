nums = [1, 2, 3, 4, 5, 6]

# size = len(nums)
# i = 0
# while i < size:
#     print(nums[i])
#     i += 1

for i in nums:
    print(i)

# for中else

for i in nums:
    if i == 5:
        print("走到break后else不会执行")
        break
else:
    print("break===================")

for i in nums:
    if i != 0:
        print("走到continue")
        continue
else:
    print("continue===================")

for i in nums:
    a = 1 / 0
else:  # 异常也不会走到else
    print("continue===================")
