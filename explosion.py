import pygame
import os

WIDTH = 640
HEIGHT = 480
FPS = 15

pygame.init()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "explosion");

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Explosion")
clock = pygame.time.Clock()

frames = []
for i in range(90):
    filename = "explosion1_{:04d}.png".format(i+1)
    frame = pygame.image.load(os.path.join(img_folder, filename))
    frames.append(frame)

running = True
frame_index = 0
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    if frame_index < 90:
        rect = frames[frame_index].get_rect()
        screen.blit(frames[frame_index], rect)
        frame_index += 1

    pygame.display.flip()

pygame.quit()
