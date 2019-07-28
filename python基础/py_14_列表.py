name_list = ['张三', '李四', '王五']

# 获取列表索引
print(name_list.index('王五'))

# 在末尾追加数据
name_list.append('赵六')

# 在指定索引处追加数据
name_list.insert(2, '钱二')

# 合并数组
name_list.extend(['孙悟空', '猪八戒'])
print(name_list)