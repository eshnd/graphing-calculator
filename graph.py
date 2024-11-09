import pygame, sys

eq = []

while True:
    eq.append(input("y = "))
    if (eq[-1] == "graph"):
        eq.remove("graph")
        break

pygame.init()
screenSize = 500
screen = pygame.display.set_mode((screenSize, screenSize))

def yy(y):
  return (-y + screenSize)

def px(x,y):
    screen.set_at((int(x), int(y)), (255, 255, 255))

def graph(i):
    for x in range(screenSize):
        y = eval(eq[i])
        px(x, yy(y))

while True:
    screen.fill((0, 0, 0))
    for i in range(len(eq)):
        graph(i)
    pygame.display.flip()
