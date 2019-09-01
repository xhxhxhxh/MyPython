import multiprocessing
import time

def jump():
    for i in range(5):
        print('---进程01--- %d' % i)
        time.sleep(1)

def dance():
    for i in range(10):
        print('---进程02--- %d' % i)
        time.sleep(1)

def main():
    p1 = multiprocessing.Process(target=jump)
    p2 = multiprocessing.Process(target=dance)
    p1.start()
    p2.start()
   

if __name__ == "__main__":
    main()