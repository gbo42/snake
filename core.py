import pygame

W = 25
Wpadded = W + 6
hor = 15
ver = 15
HEIGHT = hor * Wpadded
WIDTH = ver * Wpadded
finished = False

WHITE = (255, 255, 255)
GRAY = (51, 51, 51)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def makeGrid(x, y):
    grid = []
    for row in range(y):
        grid.append([])
        for column in range(x):
            grid[row].append(Block(column, row, GRAY))
    return grid

class Block:
    def __init__(self, x, y, color):
        self.actx = x
        self.acty = y
        self.x = Wpadded*x + 3
        self.y = Wpadded*y + 3
        self.color = color

    def updateXY(self, x, y):
        self.actx = x
        self.acty = y
        self.x = Wpadded*x + 3
        self.y = Wpadded*y + 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, W, W])

class Snake:
    def __init__(self, x, y):
        self.head = Block(x, y, WHITE)
        self.tail = []
        self.dir = (0, 0)

    def checkHit(self):
        for part in self.tail:
            if self.head.x == part.x and self.head.y == part.y:
                return True
        return False

    def move(self):
        x = self.dir[0]
        y = self.dir[1]

        if len(self.tail) > 0:
            for i in range(len(self.tail)-1, 0, -1):
                self.tail[i].updateXY(self.tail[i-1].actx, self.tail[i-1].acty)
            self.tail[0].updateXY(self.head.actx, self.head.acty)

        self.head.updateXY(self.head.actx + x, self.head.acty + y)

    def draw(self, screen):
        self.head.draw(screen)
        for part in self.tail:
            part.draw(screen)
