import pygame, sys, Ball.py, Paddle.py

#Variables
WIDTH = 900
HEIGHT = 600
BORDER = 20
VELOCITY_X = 5
VELOCITY_Y = 7
FRAMERATE = 60
fs_toggle = 0
fgColor = pygame.Color("white")
bgColor = pygame.Color("black")

class Score:
    SCORE = 0
    score_color = (220,0,0)

    def __init__(self):
        self.show(self.score_color)

    def add_point(self):
        self.show(bgColor)
        self.SCORE += 1
        self.show(self.score_color)
    
    def reset_point(self):
        self.show(bgColor)
        self.SCORE = 0
        self.show(self.score_color)

    def show(self, color):
        score_char = str(self.SCORE)
        score_font = pygame.font.SysFont('Arial.ttf', 35)
        text = score_font.render('Score:',False,color)
        screen.blit(text,((WIDTH//2)-30,BORDER))
        text = score_font.render('{0}'.format(score_char),False,color)
        screen.blit(text,(WIDTH//2,BORDER+20))

    def update(self):
        self.show(self.score_color)    

#TODO Fullscreen
def toggle_fullscreen():
    if fs_toggle == 0:
        pygame.display.set_mode((1920,1080),pygame.FULLSCREEN)
        pygame.draw.rect(screen,fgColor,pygame.Rect((0,0),(1920,BORDER)))
        pygame.draw.rect(screen,fgColor,pygame.Rect(0,0,BORDER,1080))
        pygame.draw.rect(screen,fgColor,pygame.Rect(0,1080-BORDER,1920,BORDER))
        fs_toggle = 1
    elif fs_toggle == 1:
        pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.draw.rect(screen,fgColor,pygame.Rect((0,0),(WIDTH,BORDER)))
        pygame.draw.rect(screen,fgColor,pygame.Rect(0,0,BORDER,HEIGHT))
        pygame.draw.rect(screen,fgColor,pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))
        fs_toggle = 0

#Scenario init
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong")

#Background
screen.fill(bgColor)

#Walls
pygame.draw.rect(screen,fgColor,pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen,fgColor,pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen,fgColor,pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))

#creating objects
ball = Ball(WIDTH-Ball.RADIUS-Paddle.WIDTH,HEIGHT//2,-VELOCITY_X,-VELOCITY_Y)
ball.show(fgColor)

paddle = Paddle(HEIGHT//2)
paddle_speed = 0
paddle.show(fgColor)

score = Score()

clock = pygame.time.Clock()

#Gameplay loop
while True:
    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 #       if event.type == pygame.KEYDOWN:
 #           if event.key == pygame.K_DOWN:
  #              paddle_speed = 7
   #         if event.key == pygame.K_UP:
    #            paddle_speed = -7
     #   if event.type == pygame.KEYUP:
      #      if event.key == pygame.K_DOWN:
       #         paddle_speed = -7
        #    if event.key == pygame.K_UP:
         #       paddle_speed = 7

    pygame.display.flip()
    clock.tick(FRAMERATE)
    score.update()
    paddle.update()
    ball.update()