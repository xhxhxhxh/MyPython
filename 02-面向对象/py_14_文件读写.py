# 打开文件
file = open("README", 'a')

# 读取文件
# file.write('hello')
text = file.read()
print(text)

# 关闭文件
file.close()