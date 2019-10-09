import re

ret = re.match(r'(12){3}', '121212')
print(ret.group())

# html标签匹配
ret2 = re.match(r'<(\w*)>.*</\1>', '<h2>12</h2>')
print(ret2.group())