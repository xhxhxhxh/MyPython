def create_num(total_num):
    a = 0
    b = 1
    count = 0
    while count < total_num:
        ret = yield a
        print('ret的值为：', ret)
        a, b = b, a + b

obj = create_num(10)
ret = next(obj)
print(ret)
ret = next(obj)
print(ret)

obj.send('哈哈哈')

ret = next(obj)
print(ret)
