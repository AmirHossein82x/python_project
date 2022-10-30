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
zombie_image_fast_cold = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'fast_zombie_cold.png')), (80, 80))
zombie_image_slow_cold = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'slow_zombie_cold.png')), (80, 80))
zombie_image_home = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'zombie_home-modified.png')), (140, 140))
tower_image = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'tower-modified.png')), (90, 90))
cold_tower_image = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'cold_tower.png')), (120, 120))
hole_image = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'hole-modified.png')), (120, 120))
bullet_image = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'bullet-modified.png')), (40, 40))
cold_bullet_image = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'snow_ball.png')), (40, 40))
field_image = pygame.transform.scale(pygame.image.load(os.path.join('tower_defence_assets', 'field.jpg')), (700, 700))

COIN_FONT = pygame.font.SysFont('comicsans', 40)
HEALTH_FONT = pygame.font.SysFont('comicsans', 10)
end_game_FONT = pygame.font.SysFont('comicsans', 100)
coin = 600
HEALTH = 100
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BORDER = pygame.Rect(700//2 - 5, 0, 10, 700)
dead_zombie = 0

class ZombieHome:
    def __init__(self):
        self.__x = 0
        self.__y = 520
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
        global HEALTH
        for zombie in self.zombie_list:
            if 0<=zombie.x<=40 and 0<=zombie.y<=40:
                if str(zombie) == 'fast_zombie':
                    HEALTH -= 5
                elif str(zombie) == 'slow_zombie':
                    HEALTH -= 10
                self.zombie_list.remove(zombie)
                

    def check_dead_zombie(self):
        global coin
        for zombie in self.zombie_list:
            if zombie.health <= 0:
                if str(zombie) == 'slow_zombie':
                    coin += 200
                elif str(zombie) == 'fast_zombie':
                    coin += 300
                self.zombie_list.remove(zombie)
                return 1
        return 0
                
        
class Zombie(ABC):
    def __init__(self):
        self.x = 0
        self.y = 570
        self.speed = 0
        self.image = None
        self.is_hitted_by_snow_ball = False


    def move(self):
        if self.y == 570 and self.x < 600:
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
        self.image = zombie_image_fast

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def __str__(self):
        return 'fast_zombie'


class SlowZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.health = 200
        self.image = zombie_image_slow

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def __str__(self):
        return 'slow_zombie'

    
class Bullet(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.damage = 5
        self.speed = 4
        self.image = None

    def move_bullet_down(self):
        self.y += self.speed

    def move_bullet_right(self):
        self.x += self.speed
    
    def move_bullet_up(self):
        self.y -= self.speed

    def draw_bullet(self, win):
        win.blit(self.image, (self.x, self.y))

    def __str__(self):
        return 'bullet'

class DamageBulllet(Bullet):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = bullet_image

    def __str__(self):
        return 'damage_bullet'

class ColdBullet(Bullet):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.damage = 0.25
        self.image = cold_bullet_image  

    def __str__(self):
        return 'cold_bullet'

class BaseTower:
    TOWER_LIST = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullets = []
        self.image = tower_image
        
    @classmethod
    def create_tower(cls, x, y):
        BaseTower.TOWER_LIST.append(cls(x, y))

    def draw_tower(self, win):
        win.blit(self.image, (self.x, self.y))

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

    def __str__(self):
        return 'base_tower'

class BulletTower(BaseTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = tower_image
 
    def __str__(self):
        return 'bullet_tower'

    def shoot(self, zombie):
        self.bullets.append(DamageBulllet(self.x + 30, self.y + 30))

class SnowTower(BaseTower):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = cold_tower_image
    
    def shoot(self, zombie):
        if not zombie.is_hitted_by_snow_ball:
            self.bullets.append(ColdBullet(self.x + 30, self.y + 30))

    def __str__(self):
        return 'snow_tower'

def end_game():
    global run
    end_game_text = end_game_FONT.render('Game Over', 1,RED)
    win.blit(end_game_text, (150, 300))
    pygame.display.update()
    pygame.time.delay(2000)
    run = False

def win_game():
    global run
    win_game_text = end_game_FONT.render('You Won', 1,GREEN)
    win.blit(win_game_text, (150, 300))
    pygame.display.update()
    pygame.time.delay(2000)
    run = False

zombie_home = ZombieHome()
cold_tower = SnowTower(0, 0)
bullet_tower = BulletTower(0, 0)
base_tower = BaseTower(0, 0)
bullet_tower.create_tower(500, 150)
cold_tower.create_tower(500, 300)

YELLOW = (255, 255, 0)
GREEN = (102,205,0)

def draw_game():

    win.blit(field_image, (0, 0))
    
    zombie_home.draw_zombies(win)

    zombie_home.draw(win)

    for towerz in base_tower.TOWER_LIST:
        towerz.draw_tower(win)

    for tower in BaseTower.TOWER_LIST:
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
            bullet_tower.create_tower(x-50, y-50)
            coin -= 500

    if coin >= 1000:
        if pygame.mouse.get_pressed()[2]:
            x, y = pygame.mouse.get_pos()
            cold_tower.create_tower(x-50, y-40)
            coin -= 1000

    for tower2 in BaseTower.TOWER_LIST:
        if len(tower2.bullets) < 1:
            for zombie in zombie_home.zombie_list:
                if 0<tower2.x - zombie.x<100 and 0<zombie.y - tower2.y<110 and tower2.x > zombie.x:
                    tower2.shoot(zombie)

                if 0< zombie.x - tower2.x <200 and 0<zombie.y - tower2.y<100 and  zombie.x >tower2.x :
                    tower2.shoot(zombie)

                if 0< zombie.x - tower2.x <100 and 0< tower2.y - zombie.y<110 and  zombie.y < tower2.y :
                    tower2.shoot(zombie)


    for tower in BaseTower.TOWER_LIST:
            for zombie in zombie_home.zombie_list:
                for bullet in tower.bullets:
                    if -30<=zombie.x - bullet.x<=30 and -30<=zombie.y - bullet.y<=30:
                        if str(bullet) == 'damage_bullet':
                            zombie.health -= bullet.damage
                        if str(bullet) == 'cold_bullet' and zombie.speed >= 0.75:
                            zombie.speed -= bullet.damage
                            zombie.is_hitted_by_snow_ball = True
                            if str(zombie) == 'fast_zombie':
                                zombie.image = zombie_image_fast_cold
                            elif str(zombie) == 'slow_zombie':
                                zombie.image = zombie_image_slow_cold
                                
                                         
    for tower1 in tower.TOWER_LIST:
        if tower1.y > 470:
            tower1.move_bullet_down()
        if 130< tower1.y <= 470:
            tower1.move_bullet_right()
        if tower1.y <= 130:
            tower1.move_bullet_up()   
            
    zombie_home.zombie_handle_movement()

    for tower in BaseTower.TOWER_LIST:
        tower.bullet_handle_out()

    zombie_home.zombie_wins()
    

    dead_zombie += zombie_home.check_dead_zombie()

    if HEALTH <= 0:
        end_game()

    if dead_zombie == 15:
        win_game()
    draw_game()
