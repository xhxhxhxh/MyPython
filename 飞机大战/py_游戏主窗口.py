import pygame
pygame.init()

scree = pygame.display.set_mode((480, 700))

# 加载元素
background = pygame.image.load('./images/background.png')
player = pygame.image.load('./images/me1.png')

# 绘制图像
scree.blit(background, (0, 0))
scree.blit(player, (200, 500))

# 更新画面
pygame.display.update()

while True:
    pass

pygame.quit()