import pygame, sys
from paddle import Paddle
from ball import Ball
from score import Score

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
fontName = "Arial.ttf"
fontSize = 35
scoreColor1 = (220,0,0)
scoreColor2 = (0,0,220)

def redraw(paddleSpeeds):
    score1.update()
    score2.update()
    paddle1.update(paddleSpeeds[0])
    paddle2.update(paddleSpeeds[1])
    ball.update()

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
#pygame.draw.rect(screen,fgColor,pygame.Rect(0,0,BORDER,HEIGHT))
pygame.draw.rect(screen,fgColor,pygame.Rect(0,HEIGHT-BORDER,WIDTH,BORDER))

#creating objects
displayVariables = [screen,fgColor,bgColor,WIDTH,HEIGHT,BORDER]
textVariables = [screen,fgColor,bgColor,fontName,fontSize]

clock = pygame.time.Clock()

score1 = Score(textVariables,[WIDTH//4*3,BORDER],scoreColor1)
score2 = Score(textVariables,[WIDTH//4,BORDER],scoreColor2)
scores = [score1,score2]

paddle1 = Paddle(displayVariables,WIDTH,HEIGHT)
paddle1.show(fgColor)
paddle2 = Paddle(displayVariables,20,HEIGHT)
paddle2.show(fgColor)
paddles = [paddle1,paddle2]

ball = Ball(displayVariables,-VELOCITY_X,-VELOCITY_Y, paddles,scores)
ball.show(fgColor)

#Gameplay loop
while True:
    #Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()    
    if key[pygame.K_DOWN]:
        paddleSpeed1 = 7
    elif key[pygame.K_UP]:
        paddleSpeed1 = -7
    elif key[pygame.K_w]:
        paddleSpeed2 = 7
    elif key[pygame.K_UP]:
        paddleSpeed2 = -7
    else:
        paddleSpeed1 = 0
        paddleSpeed2 = 0
    paddleSpeeds = [paddleSpeed1,paddleSpeed2]  
    redraw(paddleSpeeds)
    pygame.display.flip()
    clock.tick(FRAMERATE)

