import pygame
import os

# ширина и высота игрового экрана
WIDTH = 640
HEIGHT = 480
# частота кадров
FPS = 60

# путь к изображениям
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "images");

# класс для корабля игрока
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "player_ship.png")).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.centery = HEIGHT / 2

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.rect.y -= 8
        if keystate[pygame.K_DOWN]:
            self.rect.y += 8
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 8
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 8

class Meteor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "meteor.png")).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

    def update(self):
        self.rect.left -= 3
        
        # удалить метеор после выхода за границы экрана
        if self.rect.right < -10:
            self.kill()

# инициализация библиотеки pygame
pygame.init()

# создание объекта для отслеживания времени
clock = pygame.time.Clock()

# создание игрового экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# смена залоголовка окна
pygame.display.set_caption("My Game")

# все спрайты будут храниться здесь
sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()
player = PlayerShip()
sprites.add(player)

meteor = Meteor(WIDTH - 50, 40)
sprites.add(meteor)
meteors.add(meteor)
meteor = Meteor(WIDTH - 100, 200)
sprites.add(meteor)
meteors.add(meteor)

# цикл событий
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # изменение движения
    sprites.update()

    # обнаружение столкновений
    hits = pygame.sprite.spritecollide(player, meteors, False)
    if hits:
        running = False

    # очистка фона и рисование спрайтов
    screen.fill((0, 0, 80))
    sprites.draw(screen)

    # переключение буферов
    pygame.display.flip()

    # задает частоту запуска цикла
    clock.tick(FPS)

# завершение работы библиотеки pygame
pygame.quit()
