space_str = '\n'
# 判断是否含有空格
print(space_str.isspace())

# 判断数字
num_str = '1'
print(num_str.isdecimal())

# 判断以指定字符串开头
hello_str = 'hello world'
print(hello_str.startswith('el'))
print(hello_str.endswith('rld'))

# 查找字符串，无内容时不会报错，会返回-1
print(hello_str.find('el'))

# 字符串替换，返回新的字符串
print(hello_str.replace('world', 'python'))