import re

ret = re.match(r'(12){3}', '121212')
print(ret.group())