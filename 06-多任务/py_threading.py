import threading
import time

def jump():
    for i in range(5):
        print('---子线程01--- %d' % i)
        time.sleep(1)

def dance():
    for i in range(10):
        print('---子线程02--- %d' % i)
        time.sleep(1)

def main():
    t1 = threading.Thread(target=jump)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)

if __name__ == "__main__":
    main()