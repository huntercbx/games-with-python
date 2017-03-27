import pygame
import os

# ширина и высота игрового экрана
WIDTH = 640
HEIGHT = 480

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

# инициализация библиотеки pygame
pygame.init()

# создание игрового экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# смена залоголовка окна
pygame.display.set_caption("My Game")

# все спрайты будут храниться здесь
sprites = pygame.sprite.Group()
sprites.add(PlayerShip())
sprites.add(Meteor(WIDTH - 50, 40))
sprites.add(Meteor(WIDTH - 100, 200))

# очистка фона и рисование спрайтов
screen.fill((0, 0, 80))
sprites.draw(screen)

# переключение буферов
pygame.display.flip()

# ждем нажатия клавиши Enter, чтобы окно не закрылось
input()

# завершение работы библиотеки pygame
pygame.quit()
