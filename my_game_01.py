import pygame

# ширина и высота игрового экрана
WIDTH = 640
HEIGHT = 480

# класс для корабля игрока
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

# инициализация библиотеки pygame
pygame.init()

# создание игрового экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# смена залоголовка окна
pygame.display.set_caption("My Game")

# все спрайты будут храниться здесь
sprites = pygame.sprite.Group()
sprites.add(PlayerShip())

# очистка фона и рисование спрайтов
screen.fill((0, 0, 80))
sprites.draw(screen)

# переключение буферов
pygame.display.flip()

# ждем нажатия клавиши Enter, чтобы окно не закрылось
input()

# завершение работы библиотеки pygame
pygame.quit()
