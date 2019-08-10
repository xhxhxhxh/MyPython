import pygame
from py_plane_sprites import *

# 屏幕尺寸
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 游戏帧率
FRAME_RATE = 60

class PlaneGame(object):
    """飞机大战"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 设置时钟
        self.clock = pygame.time.Clock()

        # 创造精灵图像
        self.__create_sprites()

    def start_game(self):
        
        while True:
            self.clock.tick(FRAME_RATE)
    
            # 事件处理
            self.__handle_event()

            # 碰撞检测
            self.__check_collide()

            # 更新精灵图像
            self.__update_sprites()

            pygame.display.update()
    
    def __create_sprites(self):
        background1 = Background('./images/background.png')
        background2 = Background('./images/background.png', 1, 0, -SCREEN_RECT.height)
        # background2.rect.y = -background2.rect.height
        self.background_group = pygame.sprite.Group(background1, background2)

    def __handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.background_group.update()
        self.background_group.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()