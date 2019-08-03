def input_password():
    password = input('请输入密码:')

    if len(password) >= 8:
        return password
    
    ex = Exception('密码长度不能小于8')
    raise ex

try:
    print(input_password())
except Exception as result:
    print(result)