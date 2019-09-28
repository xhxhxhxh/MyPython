import gevent
import time
import random
from gevent import monkey

# 将所有的延时操作替换
monkey.patch_all()

def f(name):
    for n in range(10):
        print(name)
        time.sleep(random.random())

gevent.joinall([
    gevent.spawn(f, 'work1'),
    gevent.spawn(f, 'work2'),
    gevent.spawn(f, 'work3')
])