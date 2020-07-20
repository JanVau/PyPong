import pygame

class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self,screenVariables,x,y):
        self.screen = screenVariables[0]
        self.fgColor = screenVariables[1]
        self.bgColor = screenVariables[2]
        self.screenHeight = screenVariables[4]
        self.screenBorder = screenVariables[5]
        self.x = x
        self.y = y//2

    def show(self,color):
        pygame.draw.rect(self.screen,color,pygame.Rect((self.x-self.WIDTH,self.y-self.HEIGHT//2),(self.WIDTH,self.HEIGHT)))

    def update(self,vy):
        newY = self.y+vy
        if newY-self.HEIGHT//2 > self.screenBorder and newY+self.HEIGHT//2 < self.screenHeight-self.screenBorder:
            self.show(self.bgColor)
            self.y = newY
        self.show(self.fgColor)    
