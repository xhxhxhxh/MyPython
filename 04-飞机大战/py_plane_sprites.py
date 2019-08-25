import random
import pygame

# 屏幕尺寸
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

class GameSprite(pygame.sprite.Sprite):
    """飞机大战精灵"""

    def __init__(self, image_name, speed=1, *args):
        super().__init__()
        self.image = pygame.image.load(image_name)
        size = self.image.get_rect()

        # 根据是否传入args设置图像的坐标
        if len(args) > 0:
            self.rect = pygame.Rect(args[0], args[1], size.width, size.height)
        else:
            self.rect = size

        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class Background(GameSprite):
    """背景图"""

    # 重写update
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机"""

    def __init__(self):
        super().__init__('./images/enemy1.png')

        # 随机初始速度1-3
        self.speed = random.randint(1, 3)

        # 随机初始速度1-3
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.bottom = 0

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            # 使用自带的kill方法自动调用__del__方法
            self.kill()

    def __del__(self):
        print('敌机被销毁了')


class Hero(GameSprite):
    """玩家操控的飞机"""

    def __init__(self):
         super().__init__('./images/me1.png', 0)
         self.rect.centerx = SCREEN_RECT.centerx
         self.rect.bottom = SCREEN_RECT.bottom - 120

         # 创建子弹精灵组
         self.bullen_group = pygame.sprite.Group()
    
    def update(self):
        self.rect.x += self.speed

        # 限制英雄在屏幕的位置
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        """发射子弹"""

        for i in (0, 1, 2):
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            bullet.rect.bottom = self.rect.y - i * 20
            self.bullen_group.add(bullet)



class Bullet(GameSprite):

    def __init__(self):
        super().__init__('./images/bullet1.png', -2)

    def update(self):
        super().update()

        # 销毁子弹
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print('子弹被销毁了')


