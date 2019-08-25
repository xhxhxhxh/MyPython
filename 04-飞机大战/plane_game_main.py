import pygame
from py_plane_sprites import *

# 屏幕尺寸
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 游戏帧率
FRAME_RATE = 60

# 定义定时器事件
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 定义发射子弹定时器事件
HREO_FIRE_EVENT = pygame.USEREVENT + 1

class PlaneGame(object):
    """飞机大战"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)

        # 设置时钟
        self.clock = pygame.time.Clock()

        # 创造精灵图像
        self.__create_sprites()

        # 设置定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HREO_FIRE_EVENT, 500)

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
        self.hero = Hero()
       
        self.background_group = pygame.sprite.Group(background1, background2)
        self.enemy_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group(self.hero)

    def __handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            
            if event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            
            if event.type == HREO_FIRE_EVENT:
                self.hero.fire()

        # 监听键盘变化
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif key_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0


    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullen_group, self.enemy_group, True, True)

        # 敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            self.hero.kill()
            self.__game_over()

    def __update_sprites(self):
        self.background_group.update()
        self.background_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullen_group.update()
        self.hero.bullen_group.draw(self.screen)

    @staticmethod
    def __game_over():
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()