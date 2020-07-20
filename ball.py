import pygame

class Ball:
    RADIUS = 20

    def __init__(self,screenVariables,vx,vy,paddles,score):
        self.screen = screenVariables[0]
        self.fgColor = screenVariables[1]
        self.bgColor = screenVariables[2]
        self.screenWidth = screenVariables[3]
        self.screenHeight = screenVariables[4]
        self.screenBorder = screenVariables[5]
        self.x = screenVariables[3]-self.RADIUS-20
        self.y = screenVariables[4]//2
        self.vx = vx
        self.vy = vy
        self.paddles = paddles
        self.score = score

    def show(self,color):
        pygame.draw.circle(self.screen,color,(self.x,self.y),self.RADIUS)

    def update(self):
        newX = self.x + self.vx
        newY = self.y + self.vy

        if newX < 0+self.RADIUS:
            self.score[0].add_point()
            self.vx = -self.vx
        elif newY < self.screenBorder+self.RADIUS or newY > self.screenHeight-self.screenBorder-self.RADIUS:
            self.vy = -self.vy
        elif newX+self.RADIUS > self.screenWidth-self.paddles[0].WIDTH and abs(newY-self.paddles[0].y) < self.paddles[0].HEIGHT//2:
            self.vx = -self.vx
        elif newX-self.RADIUS < 0+self.paddles[1].WIDTH and abs(newY-self.paddles[1].y) < self.paddles[1].HEIGHT//2:
            self.vx = -self.vx
        elif newX+self.RADIUS > self.screenWidth:
            self.score[1].add_point()
            self.vx = -self.vx
        else:
            self.show(self.bgColor)
            self.x += self.vx
            self.y += self.vy
            self.show(self.fgColor)
