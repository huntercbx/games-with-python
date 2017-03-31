import pygame
import os
import random

# ширина и высота игрового экрана
WIDTH = 640
HEIGHT = 480
# частота кадров
FPS = 60

# путь к изображениям
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images")
snd_folder = os.path.join(game_folder, "sound")
music_folder = os.path.join(game_folder, "music")

# класс для корабля игрока
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "player_ship.png")).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.centery = HEIGHT / 2
        self.last_shot = pygame.time.get_ticks()

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > 250:
            self.last_shot = now
            laser = Laser(self.rect.right, self.rect.centery)
            lasers.add(laser)
            sprites.add(laser)

    def update(self):
        # обработка нажатия клавиш
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.rect.y -= 8
        if keystate[pygame.K_DOWN]:
            self.rect.y += 8
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 8
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 8
        if keystate[pygame.K_SPACE]:
            self.shoot()

        # проверка выхода за границы экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_image
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = WIDTH
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speedx = random.randint(-10, -3)

    def update(self):
        self.rect.left += self.speedx
        
        # удалить метеор после выхода за границы экрана
        if self.rect.right < -10:
            self.kill()

# класс для вражеского корабля
class EnemyShip(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_ship_image
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = -5
        
    def update(self):
        self.rect.left += self.speedx
        if self.rect.right < -10:
            self.kill()

# класс для выстрела
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = laser_image
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.centery = y
        self.speedx = 10
        self.speedy = 0
        laser_sound.play()

    def update(self):
        self.rect.left += self.speedx
        self.rect.top += self.speedy
        
        # удалить выстрел после выхода за границы экрана
        if self.rect.left > WIDTH + 10:
            self.kill()


# класс для выстрела
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_list[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.index = 0
        self.last_shot = pygame.time.get_ticks()
        explosion_sound.play()


    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > 100:
            self.index += 1        
            if self.index >= len(explosion_list):
                self.kill()
            else:
                self.image = explosion_list[self.index]

def create_wave_1():
    for i in range(1,4):
        meteor = Meteor()
        meteors.add(meteor)
        sprites.add(meteor)

def create_wave_2():
    enemy_list = []
    enemy_list.append(EnemyShip(WIDTH, 100))
    enemy_list.append(EnemyShip(WIDTH + 100, 200))
    enemy_list.append(EnemyShip(WIDTH, 300))
    for enemy in enemy_list:
        meteors.add(enemy)
        sprites.add(enemy)

# инициализация библиотеки pygame
pygame.init()
pygame.mixer.init(buffer=256)

# создание объекта для отслеживания времени
clock = pygame.time.Clock()

# создание игрового экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# смена залоголовка окна
pygame.display.set_caption("My Game")

# загрузка ресурсов для игры
explosion_list = []
for i in range(1,9):
    filename = "explosion_{:d}.png".format(i)
    image = pygame.image.load(os.path.join(img_folder, filename)).convert()
    image.set_colorkey((0, 0, 0))
    explosion_list.append(image)

background = pygame.image.load(os.path.join(img_folder, "background.png")).convert()
background_rect = background.get_rect()

enemy_ship_image = pygame.image.load(os.path.join(img_folder, "enemy_ship.png")).convert()
meteor_image = pygame.image.load(os.path.join(img_folder, "meteor.png")).convert()
laser_image = pygame.image.load(os.path.join(img_folder, "laser.png")).convert()

laser_sound = pygame.mixer.Sound(os.path.join(snd_folder, "laser.wav"))
explosion_sound = pygame.mixer.Sound(os.path.join(snd_folder, "explosion.wav"))

pygame.mixer.music.load(os.path.join(music_folder, "main_theme.ogg"))
pygame.mixer.music.set_volume(0.3)

# все спрайты будут храниться здесь
sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
lasers = pygame.sprite.Group()
player = PlayerShip()
sprites.add(player)

pygame.mixer.music.play()

# цикл событий
running = True
tick = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # увеличение счетчика
    tick += 1
    if tick/FPS == 3:
        create_wave_1()
    elif tick / FPS == 5:
        create_wave_2()

    # изменение движения
    sprites.update()

    # обнаружение столкновений
    hits = pygame.sprite.groupcollide(meteors, lasers, True, True)
    if hits:
        for hit in hits:
            explosion = Explosion(hit.rect.centerx, hit.rect.centery)
            sprites.add(explosion)
            print(hit)
    
    hits = pygame.sprite.spritecollide(player, meteors, False)
    if hits:
        player_explosion = Explosion(player.rect.centerx, player.rect.centery)
        sprites.add(player_explosion)
        player.kill()

    # определяем окончание игры
    if not player.alive() and not player_explosion.alive():
        running = False

    # очистка фона и рисование спрайтов
    screen.fill((0, 0, 0))
    
    screen.blit(background, background_rect)
    
    sprites.draw(screen)

    # переключение буферов
    pygame.display.flip()

    # задает частоту запуска цикла
    clock.tick(FPS)

# завершение работы библиотеки pygame
pygame.quit()
