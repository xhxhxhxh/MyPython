name_list = ['张三', '李四', '王五', '钱六']

# 删除元素
name_list.remove('张三')
name_list.pop() # 默认删除最后一个元素
item = name_list.pop(1) # 删除对应索引的元素，并返回
del name_list[0] # 将一个变量从内存中删除
name_list.clear() # 清空数组

print(name_list, item)