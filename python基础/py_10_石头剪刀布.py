# 导入随机数
import random

player = int(input('石头剪刀布 石头(1)/剪刀(2)/布(3):'))
computer = random.randint(1, 3)
print('玩家出的是%d, 电脑出的是%d' % (player, computer))

# 开始比较
if ((player == 1 and computer == 2) 
        or (player == 2 and computer == 3) 
        or (player == 3 and computer == 1)):
    print('玩家胜')
elif player == computer:
    print('平局')
else:
    print('电脑胜')