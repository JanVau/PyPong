class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self,y):
        self.y = y
        self.WIDTH=WIDTH
        self.HEIGHT=HEIGHT

    def set_Width(self,newWidth):
        self.WIDTH=newWidth
    
    def set_Height(self,newHeight):
        self.HEIGHT=newHeight

    def get_Width(self):
        return self.WIDTH

    def get_Height(self):
        return self.HEIGHT

    def show(self,color):
        pygame.draw.rect(screen,color,pygame.Rect((WIDTH-self.WIDTH,self.y-self.HEIGHT//2),(self.WIDTH,self.HEIGHT)))

    def update(self, speed):
        global bgColor,fgColor
        newY = pygame.mouse.get_pos()[1]
        if newY-self.HEIGHT//2 > BORDER and newY+self.HEIGHT//2 < HEIGHT-BORDER:
            self.show(bgColor)
            self.y += newY
            self.show(fgColor)