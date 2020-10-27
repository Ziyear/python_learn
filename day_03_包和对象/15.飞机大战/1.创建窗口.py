import time

import pygame
from pygame.locals import *
import random


# 主角飞机
class HeroPlane(object):

    def __init__(self, screen):
        self.x = 200
        self.y = 720
        self.image = pygame.image.load("./feiji/hero1.png")
        self.screen = screen
        self.bullet_list = []
        self.key_left_status = False
        self.key_right_status = False
        self.key_up_status = False
        self.key_down_status = False

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        del_list = []
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                del_list.append(bullet)
        for del_item in del_list:
            self.bullet_list.remove(del_item)

    def move(self):
        if self.key_right_status:
            if self.x <= 370:
                self.x += 10
        if self.key_left_status:
            if self.x >= 10:
                self.x -= 10
        if self.key_down_status:
            if self.y <= 710:
                self.y += 10
        if self.key_up_status:
            if self.y >= 10:
                self.y -= 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class EnemyPlane(object):
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("./feiji/enemy0.png")
        self.screen = screen
        self.bullet_list = []
        self.right = True

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        del_list = []
        if self.bullet_list:
            for bullet in self.bullet_list:
                bullet.display()
                bullet.move()
                if bullet.judge():
                    del_list.append(bullet)
            for del_item in del_list:
                self.bullet_list.remove(del_item)

    def move(self):
        if self.x > 430:
            self.right = False
        elif self.x < 0:
            self.right = True

        if self.right:
            self.x += 5
        else:
            self.x -= 5

    def fire(self):
        if random.randint(1, 50) == 30:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class Bullet(object):
    def __init__(self, screen, feiji_x, feiji_y):
        self.x = feiji_x + 40
        self.y = feiji_y - 20
        self.image = pygame.image.load("./feiji/bullet.png")
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 10

    def judge(self):
        return self.y <= 0


class EnemyBullet(object):
    def __init__(self, screen, feiji_x, feiji_y):
        self.x = feiji_x + 25
        self.y = feiji_y + 40
        self.image = pygame.image.load("./feiji/bullet1.png")
        self.screen = screen

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 10

    def judge(self):
        return self.y > 852


def key_control(hero):
    for event in pygame.event.get():
        if event.type == QUIT:
            print("bye")
            exit()
        elif event.type == KEYDOWN:
            # 检测a或者left
            if event.key == K_a or event.key == K_LEFT:
                hero.key_left_status = True
            elif event.key == K_d or event.key == K_RIGHT:
                hero.key_right_status = True
            elif event.key == K_w or event.key == K_UP:
                hero.key_up_status = True
            elif event.key == K_s or event.key == K_DOWN:
                hero.key_down_status = True
            elif event.key == K_SPACE:
                hero.fire()
        elif event.type == KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                hero.key_left_status = False
            elif event.key == K_d or event.key == K_RIGHT:
                hero.key_right_status = False
            elif event.key == K_w or event.key == K_UP:
                hero.key_up_status = False
            elif event.key == K_s or event.key == K_DOWN:
                hero.key_down_status = False


def main():
    # 创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    # 创建一个背景图
    background = pygame.image.load("./feiji/background.png")
    # 主角飞机
    hero = HeroPlane(screen)
    # 敌机
    enemy = EnemyPlane(screen)
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        hero.move()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == '__main__':
    main()
