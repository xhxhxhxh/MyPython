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

    # 重写update
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height
