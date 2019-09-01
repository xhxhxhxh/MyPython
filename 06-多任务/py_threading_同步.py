import threading
import time

g_num = 0
mutex = threading.Lock()
def jump(nums):
    global g_num
    
    for i in range(nums):
        mutex.acquire()  # 上锁 
        g_num += 1
        mutex.release()  # 解锁
    print('---子线程01--- %d' % g_num)


def dance(nums):
    global g_num

    for i in range(nums):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print('---子线程02--- %d' % g_num)

def main():
    t1 = threading.Thread(target=jump, args=(1000000,))
    t2 = threading.Thread(target=dance, args=(1000000,))
    t1.start()
    t2.start()
    
    time.sleep(2)
    print('---最终值--- %d' % g_num)

if __name__ == "__main__":
    main()