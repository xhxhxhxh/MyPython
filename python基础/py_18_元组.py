# 元组
info_tuple = ('张三', '李四', '张三')

# 方法
print(info_tuple.count('张三'))
print(info_tuple.index('张三'))

print(type(info_tuple), info_tuple[1])

# 列表与元组的转换
num_list = tuple(info_tuple)
print(type(num_list))

num_info = list(num_list)
print(type(num_info))