import card_tool
operate_num = ''

while True:
    card_tool.show_menu_main()
    operate_num = int(input('请选择操作功能：'))
    print('您选择的功能是【%d】' % operate_num)
   
    if operate_num == 1:
        card_tool.new_card()
    elif operate_num == 2:
        card_tool.show_cards()
    elif operate_num == 3:
        card_tool.find_card()
    elif operate_num == 0:
        print('下次再回!')
        break
    else:
       print('您的操作有误，请重新输入!')

