# *和+
print([1,2] * 5)
print([1,2] + [3,4])

# in
str = 'afaffgfhw'
print('f' in str)
print('z' not in str)

# 完整for循环
num = [1,2,3,5]
 
for n in num:
    print(n)
    if n == 3:
        break
else:
    print('执行结束')