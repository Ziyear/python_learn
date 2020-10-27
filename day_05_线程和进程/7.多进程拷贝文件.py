from multiprocessing import Pool, Manager
import os

source_path = "C:\\Users\\ZIYEAR\\Desktop\\TeleReport\\"
target_path = "C:\\Users\\ZIYEAR\\Desktop\\TeleReport_copy\\"


# 递归获取路径下所有文件名1
def listdir(path):  # 传入存储的list
    list_name = []
    listdir_(path, list_name)
    return list_name


def listdir_(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir_(file_path, list_name)
        else:
            global source_path
            file_path = file_path.replace(source_path, "")
            list_name.append(file_path)


def copyFileTask(file_name, source_path, target_path, queue):
    fr = open(source_path + file_name, "rb")
    new_file_path = target_path + file_name
    new_file_dir = new_file_path[:new_file_path.rindex("\\")]
    # 如果新文件所在目录不存在，则创建
    if not os.path.exists(new_file_dir):
        os.makedirs(new_file_dir)
    fw = open(new_file_path, "wb")
    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()
    queue.put(file_name)


def main():
    # 1.创建一个文件夹
    global target_path, source_path
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    # 2.获取source文件夹所有文件名 文件全路径去除目录路径后的文件名
    file_names = listdir(source_path)
    # 3.使用多进程方式，将源文件夹所有文件拷贝到新文件夹
    po = Pool(5)

    queue = Manager().Queue()
    for name in file_names:
        po.apply_async(copyFileTask, args=(name, source_path, target_path, queue))
    po.close()
    num = 0
    allNum = len(file_names)
    while num < allNum:
        queue.get()
        num += 1
        copy_rate = num / allNum
        print("\r copy... %.2f%%" % (copy_rate * 100), end="")
    po.join()


if __name__ == '__main__':
    main()
