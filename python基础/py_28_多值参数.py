def measure(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


# measure(1,2,3,4,name='张三',age=20)
# 拆包
num = 1
args = (1,2,3)
kwargs = {'name': '张三', 'age': 20}
# measure(num, *args, **kwargs)
measure()