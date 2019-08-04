# 打开文件
file = open("README")
file_copy = open("README[复件]", 'w')

# 读取文件
text = file.read()
file_copy.write(text)

# 关闭文件
file.close()
file_copy.close()