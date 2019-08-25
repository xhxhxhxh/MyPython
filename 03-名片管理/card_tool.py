menu_main = ['欢迎使用【名片管理系统】 V1.0', '', '1. 新增名片', '2. 显示全部', '3. 查询名片', '', '0. 退出系统']
card_list = [] # 定义存储名片的列表

def show_menu_main():
    """显示主菜单界面"""

    print('*' * 50)
    for n in menu_main:
        print(n)
    print('*' * 50)


def show_tips(message):
    """显示提示信息"""

    print('-' * 50)
    print(message)


def new_card():
    """新增名片"""

    show_tips('新增名片')
    name = input('请输入姓名：')
    age = input('请输入年龄：')
    phone = input('请输入手机号：')
    email = input('请输入邮箱：')
    id = 1
    
    # 获取card_list长度，以便得到其最后一个元素
    length = len(card_list)
    if length > 0:
        last_item = card_list[length - 1]
        id = last_item['id'] + 1

    card = {
        "id": id,
        "name": name,
        "age": age,
        "phone": phone,
        "email": email
    }
    card_list.append(card)

    print('添加%s名片成功' % name)
    print(card_list)


def show_cards():
    """显示所有名片"""

    show_tips('所有名片')

    if len(card_list) == 0:
        return print('未查询到符合条件的名片')

    for item in ['序号', '姓名', '年龄', '电话', '邮箱']:
        print(item, end = '\t\t\t')
    print('')
    print('=' * 100)
    num = 0

    for card in card_list:
        num += 1
        print('%d\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t' % (num, card['name'], card['age'], card['phone'], card['email']))


def find_card():
    """查询名片"""

    name = input('请输入要查询人的姓名：')

    while True: # 操作结束后依然停留在查询结果页面
        find_cards_list = []

        for card in card_list:
            if card['name'] == name:
                find_cards_list.append(card)
        
        length = len(find_cards_list)
        if length == 0:
            return print('未查询到符合条件的名片')
        else:
            for item in ['序号', '姓名', '年龄', '电话', '邮箱']:
                print(item, end = '\t\t\t')
            print('')
            print('=' * 100)
            num = 0

            for card in find_cards_list:
                num += 1
                print('%d\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t%s\t\t\t' % (num, card['name'], card['age'], card['phone'], card['email']))
            
            operate = int(input('请选择要执行的操作：【1】修改 | 【2】删除 | 【0】返回：'))
            if operate == 1:
                modify_card(find_cards_list)
            elif operate == 2:
                del_card(find_cards_list)
            elif operate == 0:
                break
            else:
                print('您的操作有误，请重新输入!')


def del_card(find_cards_list):
    """删除名片"""

    length = len(find_cards_list)
    if length > 1: # 处理有多条数据的情况
        while True:
            num = int(input('请输入要删除名片的序号：'))

            if num < 1 or num > length:
                print('输入有误，请重新输入')
                continue
            
            target_item = find_cards_list[num -1]
            find_cards_list.pop(num - 1)
            for item in card_list:
                if item['id'] == target_item['id']:
                    card_list.remove(item)
                    print('删除成功')
                    return
    else:
        target_item = find_cards_list[0]
        find_cards_list.pop(0)
        card_list.remove(target_item)
        print('删除成功')


def modify_card(find_cards_list):
    """修改名片"""

    length = len(find_cards_list)
    if length > 1: # 处理有多条数据的情况
        while True:
            num = int(input('请输入要修改名片的序号：'))

            if num < 1 or num > length:
                print('输入有误，请重新输入')
                continue
            
            target_item = find_cards_list[num -1]
            target_item['name'] = my_input(target_item['name'], '请输入姓名[不更改请按回车]：')
            target_item['age'] = my_input(target_item['age'], '请输入年龄[不更改请按回车]：')
            target_item['phone'] = my_input(target_item['phone'], '请输入电话[不更改请按回车]：')
            target_item['email'] = my_input(target_item['email'], '请输入邮箱[不更改请按回车]：')
            print('修改成功')
            return   
    else:
        target_item = find_cards_list[0]
        target_item['name'] = my_input(target_item['name'], '请输入姓名[不更改请按回车]：')
        target_item['age'] = my_input(target_item['age'], '请输入年龄[不更改请按回车]：')
        target_item['phone'] = my_input(target_item['phone'], '请输入电话[不更改请按回车]：')
        target_item['email'] = my_input(target_item['email'], '请输入邮箱[不更改请按回车]：')
        print('修改成功')


def my_input(obj, tip_message):
    """自定义input()返回值"""

    value = input(tip_message)
    if len(value) > 0:
        return value
    else:
        return obj


    