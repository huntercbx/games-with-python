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

    def checkCollision(self, rect):
        x_min = min(self.rect.left, rect.left)
        x_max = max(self.rect.right, rect.right)
        x_intersects = (x_max - x_min) < (self.rect.width + rect.width)
        y_min = min(self.rect.top, rect.top)
        y_max = max(self.rect.bottom, rect.bottom)
        y_intersects = (y_max - y_min) < (self.rect.height + rect.height)
        return x_intersects and y_intersects

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
    for m in meteors:
        running = running and not m.checkCollision(player.rect)

    # очистка фона и рисование спрайтов
    screen.fill((0, 0, 80))
    sprites.draw(screen)

    # переключение буферов
    pygame.display.flip()

    # задает частоту запуска цикла
    clock.tick(FPS)

# завершение работы библиотеки pygame
pygame.quit()
