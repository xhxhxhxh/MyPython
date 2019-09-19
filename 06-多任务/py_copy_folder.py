import multiprocessing
import os, time, random

def copy_file(folder_name, new_folder_name, file_name, q):
    old_path = folder_name + '/' + file_name
    new_path = new_folder_name + '/' + file_name

    time.sleep(random.random() * 2)

    # 读取旧文件
    old_file = open(old_path, 'rb')
    old_file_content = old_file.read()
    old_file.close()

    # 写入新文件
    new_file = open(new_path, 'wb')
    new_file.write(old_file_content)
    new_file.close()
    q.put(new_folder_name)

    
def main():
    # 获取要复制的文件夹名称
    folder_name = input('请输入复制的文件夹')
    new_folder_name = folder_name + '复件'

    # 创建新文件夹
    try:
        os.mkdir(new_folder_name)
    except:
        pass

    # 获取文件数
    file_count = os.listdir(folder_name)

    # 创建进程
    multiprocessing_count = 5
    if len(file_count) < 5:
        multiprocessing_count = file_count
    
    po = multiprocessing.Pool(multiprocessing_count)

    # 创建队列
    q = multiprocessing.Manager().Queue()

    for file_name in file_count:
        # 添加进程
        po.apply_async(copy_file, args=(folder_name, new_folder_name, file_name, q))

    po.close() # 关闭进程池
    # po.join() # 等待进程池所有程序执行完毕

    # 已完成拷贝文件数
    file_finished_file_count = 0
    while True:
        file_name = q.get()
        file_finished_file_count += 1
        print('\r文件拷贝进度 %.2f %%' % (file_finished_file_count / len(file_count) * 100), end='')
        if file_finished_file_count >= len(file_count):
            break

    


if __name__ == "__main__":
    main()