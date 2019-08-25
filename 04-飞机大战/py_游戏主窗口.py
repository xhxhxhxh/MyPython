import pygame
from py_plane_sprites import *

pygame.init()

scree = pygame.display.set_mode((480, 700))

# 加载元素
background = pygame.image.load('./images/background.png')
player = pygame.image.load('./images/me1.png')

# 绘制图像
scree.blit(background, (0, 0))
scree.blit(player, (200, 500))

# 创建敌机
enemy = GameSprite('images/enemy1.png')

enemy_group = pygame.sprite.Group(enemy)

# 设置时钟
clock = pygame.time.Clock()

# 改变player位置
player_rect = pygame.Rect(200, 500, 102, 126)

# 更新画面
pygame.display.update()

while True:
    clock.tick(60)

    # 退出游戏事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    player_rect.y -= 1

    # 重置player位置
    if player_rect.y <= 0:
        player_rect.y = 700

    scree.blit(background, (0, 0))
    scree.blit(player, player_rect)

    # 更新敌机位置
    enemy_group.update()
    enemy_group.draw(scree)
    
    pygame.display.update()
    pass

pygame.quit()