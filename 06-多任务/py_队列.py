import multiprocessing

def save(q):
    # 设置数据
    data = [1, 2, 3, 4, 5]

    # 存放数据
    for item in data:
        q.put(item)
    
    print('数据存放完毕')
   
def get(q):
    data = []
    while True:
        data.append(q.get())

        if q.empty():
            break
    
    print(data)
    

def main():
    # 创建一个队列
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=save, args=(q,))
    p2 = multiprocessing.Process(target=get, args=(q,))
    p1.start()
    p2.start()
   

if __name__ == "__main__":
    main()