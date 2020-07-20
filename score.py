import pygame

class Score:
    SCORE = 0

    def __init__(self, textVariables, textPosition, scoreColor):
        self.screen = textVariables[0]
        self.fgColor = textVariables[1]
        self.bgColor = textVariables[2]
        self.fontName = textVariables[3]
        self.fontSize = textVariables[4]
        self.x = textPosition[0]
        self.y = textPosition[1]
        self.scoreColor = scoreColor
        self.show(self.scoreColor)

    def add_point(self):
        self.show(self.bgColor)
        self.SCORE += 1
        self.show(self.scoreColor)
    
    def reset_point(self):
        self.show(self.bgColor)
        self.SCORE = 0
        self.show(self.scoreColor)

    def show(self, color):
        scoreChar = str(self.SCORE)
        scoreFont = pygame.font.SysFont(self.fontName, self.fontSize)
        text = scoreFont.render('Score:',False,color)
        self.screen.blit(text,(self.x,self.y))
        text = scoreFont.render('{0}'.format(scoreChar),False,color)
        self.screen.blit(text,(self.x,self.y+20))

    def update(self):
        self.show(self.scoreColor)   