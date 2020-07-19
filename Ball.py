class Ball:
    RADIUS = 20

    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.RADIUS=RADIUS

    def set_Radius(self,newRadius):
        self.RADIUS = newRadius

    def get_Radius(self):
        return RADIUS

    def show(self,color):
        global screen
        pygame.draw.circle(screen,color,(self.x,self.y),self.RADIUS)

    def update(self):
        global bgColor,fgColor

        newX = self.x + self.vx
        newY = self.y + self.vy

        if newX < BORDER+self.RADIUS:
            score.add_point()
            self.vx = -self.vx
        elif newY < BORDER+self.RADIUS or newY > HEIGHT-BORDER-self.RADIUS:
            self.vy = -self.vy
        elif newX+Ball.RADIUS > WIDTH-Paddle.WIDTH and abs(newY-paddle.y) < Paddle.HEIGHT//2:
            self.vx = -self.vx
        elif newX+Ball.RADIUS > WIDTH:
            score.reset_point()
            self.vx = -self.vx
        else:
            self.show(bgColor)
            self.x += self.vx
            self.y += self.vy
            self.show(fgColor)