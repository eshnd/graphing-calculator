import pygame, sys

eq = input("y = ")

pygame.init()
screen_size = 500
screen = pygame.display.set_mode((screen_size, screen_size))

def px(x,y):
    screen.set_at((x, y), (255, 255, 255))

def graph():
    for x in range(screen_size):
        y = eval(eq)
        px(x,y)

while True:
    screen.fill((0, 0, 0))
    triRender(p1, p2, p3)
    pygame.display.flip()