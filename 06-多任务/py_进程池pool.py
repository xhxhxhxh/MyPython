import multiprocessing
import os, time, random

def work(i):
    t_start = time.time()
    print('%s开始执行， 进程号为%d' % (i, os.getpid()))
    time.sleep(random.random() * 2)
    t_end = time.time()
    print('%s执行完毕， 耗时%0.2f' % (i, t_end - t_start))
    
def main():
    po = multiprocessing.Pool(3)

    for i in range(0, 10):
        # 添加十个进程
        po.apply_async(work, (i,))

    po.close() # 关闭进程池
    po.join() # 等待进程池所有程序执行完毕
    


if __name__ == "__main__":
    main()