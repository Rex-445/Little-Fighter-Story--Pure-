import pygame


pygame.font.init()

class Button():
    def __init__(self, text="Button", color=(0,100,200), x=0, y=0, size=[150, 60], image=None):
        self.name = text
        self.font = pygame.font.Font(None, 30)
        self.text = self.font.render(self.name, True, (200,50,50), color)
        self.rect = (x,y, size[0], size[1])
        self.color = color
        self.newColor = (color[0] + 50, color[1] + 50, color[2] + 50)
        self.type = "menu"
        self.hasClicked = True
        self.oldColor = color

        self.buttonBlit = "Raw"
        self.image = image
        if self.image != None:
            self.rect = self.image.get_rect()

        self.size = size

        self.levelType = 0

        self.NAME = "LEVEL_NONE"
                

    def isHover(self, pos):
        if pos[0] > self.rect[0] and pos[0] < self.rect[0] + self.rect[2]:
            if pos[1] > self.rect[1] and pos[1] < self.rect[1] + self.rect[3]:
                return True
        return False
    def Update(self, wn, mouse):
        #Actual Button
        if self.buttonBlit == "Raw":
            pygame.draw.rect(wn, self.color, (self.rect),0)
        if self.buttonBlit == "Image":
            wn.blit(self.image, self.rect)
        #Button Outline
        pygame.draw.rect(wn, (0,100,255), (self.rect),3)
        wn.blit(self.text, (self.rect[0] + self.rect[2] / 3, self.rect[1] + self.rect[3] / 3))
        if self.isHover(mouse) and self.buttonBlit == "Raw":
            self.color = (50,50,50)
            self.text = self.font.render(self.name, True, (255,0,0), self.color)
        else:
            self.color = self.oldColor
            self.text = self.font.render(self.name, True, (150,150,150), self.oldColor)
