try:
    num = int(input('请输入一个整数'))
    print(8 / num)
except ValueError:
    print('输入错误')
except ZeroDivisionError:
    print('0错误')
except Exception as result:
    print('未知错误%s' % result)
else:
    print('无异常时执行')
finally:
    print('无论是否异常都会执行')

