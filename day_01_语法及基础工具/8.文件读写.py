# 向文件写入 hahah

# f = open("test.txt", "w")
# f.write("hahhah")
# f.close()

# 读取文件

f = open("test.txt", "r")
content = f.read()
print(content)
f.close()

# 复制文件
# old_file = open("test.txt", "r")
# old_file_name = old_file.name
# position = old_file_name.rfind(".")
# new_file_name = old_file_name[:position] + " [附件]" + old_file_name[position:]
#
# new_file = open(new_file_name, "w")
#
# while True:
#     content = old_file.read(1024)
#
#     if len(content) == 0:
#         break
#     new_file.write(content)
#
# new_file.close()
# old_file.close()


# 修改目录下文件名
# import os
#
# file_dir_name = "D:\log"
# # 获取要重命名的文件夹
# listdir = os.listdir(file_dir_name)
#
# for name in listdir:
#     print(name)
#     old_file_name = file_dir_name + "\\" + name
#     new_file_name = file_dir_name + "\\[Ziyear]-" + name
#     os.rename(old_file_name, new_file_name)
