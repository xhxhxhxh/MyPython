name_list = ['张三', '李四', '王五', '钱六', '张三']
num_list = [1,2,3,4,2,32,3]

# 统计长度
length = len(name_list)
count = name_list.count('张三')

# 排序数组
# num_list.sort() # 升序
# num_list.sort(reverse=True) # 降序
num_list.reverse() # 翻转数组

print(name_list, length, count)
print(num_list)