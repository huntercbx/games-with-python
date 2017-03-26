import pygame

# ширина и высота игрового экрана
WIDTH = 640
HEIGHT = 480

# инициализация библиотеки pygame
pygame.init()

# создание игрового экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# смена залоголовка окна
pygame.display.set_caption("My Game")

# очистка фона
screen.fill((0, 0, 80))

# переключение буферов
pygame.display.flip()

# ждем нажатия клавиши Enter, чтобы окно не закрылось
input()

# завершение работы библиотеки pygame
pygame.quit()
