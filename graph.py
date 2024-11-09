import pygame, sys

eq = input("y = ")

pygame.init()
screen_size = 500
screen = pygame.display.set_mode((screen_size, screen_size))

def px(x,y):
    screen.set_at((int(x), int(y)), (255, 255, 255))

def yy(y):
    return (-y + screen_size)

def graph():
    for x in range(screen_size):
        y=eval(eq)
        px(x, yy(y))

while True:
    screen.fill((0, 0, 0))
    graph()
    pygame.display.flip()
