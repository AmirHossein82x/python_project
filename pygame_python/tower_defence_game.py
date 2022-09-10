import pygame
import os
from abc import ABC, abstractmethod
import random
from datetime import datetime

pygame.init()

win = pygame.display.set_mode((700, 700))
pygame.display.set_caption('tower defence')

zombie_image_fast = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'fast_zombie_2-modified.png')), (80, 80))
zombie_image_slow = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'slow_zombie-modified.png')), (80, 80))
zombie_image_home = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'zombie_home-modified.png')), (120, 120))
tower_image = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'tower-modified.png')), (90, 90))
hole_image = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'hole-modified.png')), (120, 120))
bullet_image = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'bullet-modified.png')), (40, 40))

COIN_FONT = pygame.font.SysFont('comicsans', 40)
HEALTH_FONT = pygame.font.SysFont('comicsans', 10)
coin = 600
HEALTH = 100


class ZombieHome:
    def __init__(self):
        self.__x = 0
        self.__y = 570
        self.zombie_list = []

    def draw(self, win):
        win.blit(zombie_image_home, (self.__x, self.__y))

    def make_zombie(self):
        if 0 <= len(self.zombie_list) <= 3:
            available_zombie = [FastZombie, SlowZombie]
            zombie = random.choice(available_zombie)
            self.zombie_list.append(zombie())


    def draw_zombies(self, win):
        for zombie in self.zombie_list:
            zombie.draw(win)

    def zombie_handle_movement(self):
        for zombie in self.zombie_list:
            zombie.move()

    def zombie_wins(self):
        for zombie in self.zombie_list:
            if 0<=zombie.x<=40 and 0<=zombie.y<=40:
                self.zombie_list.remove(zombie)
                return True
        return False

    def check_dead_zombie(self):
        for zombie in self.zombie_list:
            if zombie.health <= 0:
                self.zombie_list.remove(zombie)
                return True
        return False


class Zombie(ABC):
    def __init__(self):
        self.x = 0
        self.y = 600
        self.speed = 0


    
    def move(self):
        if self.y == 600 and self.x < 600:
            self.x += self.speed
        elif 25<self.y <= 600 and self.x == 600:
            self.y -= self.speed
        else:
            self.x -= self.speed


    @abstractmethod
    def draw(self, win):
        pass


class FastZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.health = 100

    def draw(self, win):
        win.blit(zombie_image_fast, (self.x, self.y))


class SlowZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.health = 200

    def draw(self, win):
        win.blit(zombie_image_slow, (self.x, self.y))


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 50
        self.speed = 4

    def move_bullet_down(self):
        self.y += self.speed

    def move_bullet_right(self):
        self.x += self.speed
    
    def move_bullet_up(self):
        self.y -= self.speed


    def draw_bullet(self, win):
        win.blit(bullet_image, (self.x, self.y))


class Tower:
    TOWER_LIST = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullets = []
        

    @classmethod
    def create_tower(cls, x, y):
        Tower.TOWER_LIST.append(cls(x, y))

    
    def draw_tower(win):
        for tower in Tower.TOWER_LIST:
            win.blit(tower_image, (tower.x, tower.y))

    # def make_bullet(self):
    #     self.bullets.append(Bullet(tower.x + 30, tower.y + 30))

    def draw_bullet(self, win):
        for bullet in self.bullets:
            bullet.draw_bullet(win)

    def move_bullet_down(self):
        for bullet in self.bullets:
            bullet.move_bullet_down()

    def move_bullet_right(self):
        for bullet in self.bullets:
            bullet.move_bullet_right()

    def move_bullet_up(self):
        for bullet in self.bullets:
            bullet.move_bullet_up()

    def bullet_handle_out(self):
        for bullet in self.bullets:
            if bullet.x > 650 or bullet.y > 650 or bullet.y < 10:
                self.bullets.remove(bullet)


zombie_home = ZombieHome()
tower = Tower(150, 50)
Tower.create_tower(500, 150)
Tower.create_tower(500, 300)

YELLOW = (255, 255, 0)
GREEN = (102,205,0)

def draw_game():

    win.fill((240,0,255))
    
    zombie_home.draw_zombies(win)

    zombie_home.draw(win)

    Tower.draw_tower(win)

    for tower in Tower.TOWER_LIST:
        tower.draw_bullet(win)

    win.blit(hole_image, (10, 10))

    coin_text = COIN_FONT.render(str(coin) + '$', 1,YELLOW)
    health_text = COIN_FONT.render(str(HEALTH), 1, GREEN)

    win.blit(coin_text, (300, 300))
    win.blit(health_text, (25, 100))

    pygame.time.delay(10)

    pygame.display.update()


run = True
while run:
    now = datetime.now()
    if int(now.strftime("%f")[:2]) % 50 == 0:
        zombie_home.make_zombie()
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if coin >= 500:
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            tower.create_tower(x-50, y-50)
            coin -= 500

    for tower2 in Tower.TOWER_LIST:
        if len(tower2.bullets) < 1:
            for zombie in zombie_home.zombie_list:
                if 0<tower2.x - zombie.x<100 and 0<zombie.y - tower2.y<200 and tower2.x > zombie.x:
                    tower2.bullets.append(Bullet(tower2.x + 30, tower2.y + 30))
                elif 0< zombie.x - tower2.x <200 and 0<zombie.y - tower2.y<100 and  zombie.x >tower2.x :
                    tower2.bullets.append(Bullet(tower2.x + 30, tower2.y + 30))

                elif 0< zombie.x - tower2.x <100 and 0< tower2.y - zombie.y<50 and  zombie.y < tower2.y :
                    tower2.bullets.append(Bullet(tower2.x + 30, tower2.y + 30))

    for tower, zombie in zip(Tower.TOWER_LIST, zombie_home.zombie_list):
        for bullet in tower.bullets:
            if -30<=zombie.x - bullet.x<=30 and -30<=zombie.y - bullet.y<=30:
                zombie.health -= 50


                    
    for tower1 in tower.TOWER_LIST:
        if tower1.y > 470:
            tower1.move_bullet_down()
        if 130< tower1.y <= 470:
            tower1.move_bullet_right()
        if tower1.y <= 130:
            tower1.move_bullet_up()   
            
    zombie_home.zombie_handle_movement()

    for tower in Tower.TOWER_LIST:
        tower.bullet_handle_out()

    if zombie_home.zombie_wins():
        HEALTH -= 10

    if zombie_home.check_dead_zombie():
        coin += 250

    draw_game()
    pygame.display.update()