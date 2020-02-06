import pygame, sys, pickle, random
from pygame.locals import *


pygame.init()


class Characters(pygame.sprite.Sprite):
    def __init__(self, name="Rex", pos=(0,0)):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.sprite = pygame.image.load("sys/firzen_0.bmp")
        self.shadow = pygame.image.load("sys/shadow.png")
        self.head = pygame.image.load("sys/Rex_f.bmp")
        self.defualt = ["sys/aiden_0.bmp"]

        self.frame = 1
        self.width, self.height = (79, 79)

        #status of the character
        self.action = 0
        self.direction = 1
        self.s_pos = [17, 75]
        self.targetObject = None
        self.name = name
        self.pos = list(pos)
        self.points = [self.pos[0], self.pos[0] + random.randint(500,1400)]
        self.targetPos = pygame.Rect(self.points[1], self.pos[1], 20,20)
        self.timer = 0
        self.isPatrol = False

        ################ Animations ###############
        #Standing
        self.frames1 = [0, 1, 2, 3, 2, 1, 0]
        #Walking
        self.frames2 = [4, 5, 6, 7, 6, 5, 4]
        #Running
        self.frames3 = [10, 11, 12, 11, 10]
        #Stance
        self.frames4 = [23, 23]
        #Skill
        self.frames5 = [141, 142, 143, 144, 146, 147, 148, 149, 144, 150, 151, 152]
        #Lying
        self.frames6 = [34]
        
        #Standing2
        self.frames1_b  = [9, 8, 7, 6, 7, 8, 9]
        #Walking2
        self.frames2_b  = [5, 4, 3, 2, 3, 4, 5]
        #Running
        self.frames3_b = [17, 18, 19, 18, 17]
        #Stance
        self.frames4_b = [25, 25]
        #Lying
        self.frames6_b = [34]


        self.FTPS = 0

        #sounds
        self.sounds = []

        #character frames
        self.cells = []
        self.flip = []
        self.targetCell = self.cells
        self.row = 0
        self.col = 0

        self.alignX = []
        self.alignY = []
        self.x = 0
        self.y = 0

        data = pickle.load(open("data/" + str(self.name) + ".txt", "rb"))
        self.alignX = data[0]
        self.alignY = data[1]
        self.targetFrame = []
              
    #determine the amount of frames the GameObject would require
    def load_image_frames(self, amount, maxRowSize):
        self.row = 0
        for n in range(amount + 6):
            rect = pygame.Rect(self.row, self.col, self.width, self.height)
            if rect.x < maxRowSize:
                self.image = pygame.Surface(rect.size)
                self.image.blit(self.sprite, (0,0), rect)
                self.alpha = self.image.get_at((0,0))
                self.image.set_colorkey(self.alpha)
                self.cells.append(self.image)
                self.row += self.width
            else:
                self.row = 0
                self.col += self.height
        self.col = 0
        self.row = 0
        self.targetCell = self.cells

    #function was made to make GameObject's Initilization easier       
    def __init__self__(self, image, row, col, amountOfFrames):
        self.sprite = pygame.image.load(image)
        self.width = row
        self.height = col
        self.load_image_frames(amountOfFrames, self.sprite.get_rect().width)
        self.bdy = self.cells[0]
        self.rect = self.bdy.get_rect()
        
    #function was made to make GameObject's Initilization easier       
    def __init__self__mirror__(self, image, row, col, amountOfFrames):
        self.sprite = pygame.image.load(image)
        self.width = row
        self.height = col
        self.load_image_frames_mirror(amountOfFrames, self.sprite.get_rect().width)
                
    #determine the amount of frames the GameObject would require
    def load_image_frames_mirror(self, amount, maxRowSize):
        self.row = maxRowSize - self.width
        for n in range(amount):
            rect = pygame.Rect(self.row, self.col, self.width, self.height)
            if rect.x > 0:
                self.image = pygame.Surface(rect.size)
                self.image.blit(self.sprite, (0,0), rect)
                self.alpha = self.image.get_at((0,0))
                self.image.set_colorkey(self.alpha)
                self.flip.append(self.image)
                self.row -= self.width
            else:
                self.row = maxRowSize - self.width
                self.image = pygame.Surface(rect.size)
                self.image.blit(self.sprite, (0,0), rect)
                self.alpha = self.image.get_at((0,0))
                self.image.set_colorkey(self.alpha)
                self.flip.append(self.image)
                self.col += self.height
        self.col = 0
        self.row = 0

    def Patrol(self):
        if self.timer >= 50:
            self.action = 1
        self.rec = self.bdy.get_rect()
        self.rec.x = self.pos[0]
        self.rec.y = self.pos[1]
        
        if self.timer < 50 and self.rec.colliderect(self.targetPos) == False:
            self.timer += 1
        if self.rec.colliderect(self.targetPos):
            self.action = 0
            self.timer = 0
            if self.targetPos.x <= self.points[0]:
                self.targetPos.x = self.points[1]
                self.direction = 1
                return
            if self.targetPos.x >= self.points[1]:
                self.targetPos.x = self.points[0]
                self.direction = -1

        
    ###### Update Called Once Per Frame ######
    def Update(self, stagePosX):
        if self.isPatrol:
            self.Patrol()
        pos = [self.pos[0] - stagePosX, self.pos[1]]
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        if self.action == 0:
            if self.targetObject != None:
                if self.targetObject.rect.x > self.rect.x:
                    self.direction = 1
                if self.targetObject.rect.x < self.rect.x:
                    self.direction = -1
        
        ############# Facing Right ##############
        if self.direction == 1:
            self.targetCell = self.cells
        if self.direction == -1:
            self.targetCell = self.flip
        if self.direction == 1:
            #standing
            if self.action == 0:
                self.x = self.pos[0] + self.alignX[self.frames1[int(self.frame)]]
                self.y = self.pos[1] + self.alignY[self.frames1[int(self.frame)]]
                self.bdy = self.cells[int(self.frames1[int(self.frame)])]
                self.frame += 0.15
                if self.frame >= len(self.frames1) - 1:
                    self.frame = 0
                
            #walking
            if self.action == 1:
                self.pos[0] += 2
                self.x = self.rect.x + self.alignX[self.frames2[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames2[int(self.frame)]]
                self.bdy = self.cells[int(self.frames2[int(self.frame)])]
                self.frame += 0.2
                if self.frame >= len(self.frames2) - 1:
                    self.frame = 0
                
            #running
            if self.action == 2:
                self.pos[0] += 5
                self.x = self.rect.x + self.alignX[self.frames3[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames3[int(self.frame)]]
                self.bdy = self.cells[int(self.frames3[int(self.frame)])]
                self.frame += 0.2
                if self.frame >= len(self.frames3) - 1:
                    self.frame = 0
                
            #stance_idle
            if self.action == 3:
                if int(self.frame) >= len(self.frames4) - 1:
                    self.frame = 0
                self.x = self.rect.x + self.alignX[self.frames4[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames4[int(self.frame)]]
                self.bdy = self.cells[int(self.frames4[int(self.frame)])]
                self.frame += 0.2
                
            #stance_idle
            if self.action == 4:
                if self.frame >= len(self.frames5) - 1:
                    self.frame = 0
                self.x = self.rect.x + self.alignX[self.frames5[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames5[int(self.frame)]]
                self.bdy = self.cells[int(self.frames5[int(self.frame)])]
                self.frame += 0.2
                
            #stance_idle
            if self.action == 5:
                self.x = self.rect.x + self.alignX[self.frames6[0]]
                self.y = self.rect.y + self.alignY[self.frames6[0]]
                self.bdy = self.cells[int(self.frames6[0])]
                self.frame += 0.2

        ############# Facing Left ################
        if self.direction == -1:
            #standing
            if self.action == 0:
                self.x = self.rect.x - self.alignX[self.frames1[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames1[int(self.frame)]]
                self.bdy = self.flip[int(self.frames1[int(self.frame)])]
                self.frame += 0.15
                if self.frame >= len(self.frames1) - 1:
                    self.frame = 0
                
            #walking
            if self.action == 1:
                self.pos[0] += -2
                self.x = self.rect.x - self.alignX[self.frames2[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames2[int(self.frame)]]
                self.bdy = self.flip[int(self.frames2[int(self.frame)])]
                self.frame += 0.2
                if self.frame >= len(self.frames2) - 1:
                    self.frame = 0
                
            #running
            if self.action == 2:
                self.pos[0] += -5
                self.x = self.rect.x - self.alignX[self.frames3[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames3[int(self.frame)]]
                self.bdy = self.flip[int(self.frames3[int(self.frame)])]
                self.frame += 0.2
                if self.frame >= len(self.frames3) - 1:
                    self.frame = 0
                
            #stance_idle
            if self.action == 3:
                if int(self.frame) >= len(self.frames4) - 1:
                    self.frame = 0
                self.x = self.rect.x - self.alignX[self.frames4[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames4[int(self.frame)]]
                self.bdy = self.flip[int(self.frames4[int(self.frame)])]
                self.frame += 0.2
                
            #stance_idle
            if self.action == 4:
                if self.frame >= len(self.frames5) - 1:
                    self.frame = 0
                self.x = self.rect.x - self.alignX[self.frames5[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames5[int(self.frame)]]
                self.bdy = self.flip[int(self.frames5[int(self.frame)])]
                self.frame += 0.2
                
            #stance_idle
            if self.action == 5:
                self.x = self.rect.x + self.alignX[self.frames6_b[0]]
                self.y = self.rect.y + self.alignY[self.frames6_b[0]]
                self.bdy = self.cells[int(self.frames6[0])]
                self.frame += 0.2



##screen = pygame.display.set_mode((300,300))
        
character = Characters()
character.__init__self__(character.defualt[0], 80, 80, 8)
character.rect.x = 20
character.rect.y = 110

character2 = Characters()
character2.__init__self__("sys/freeze_0.bmp", 80, 80, 8)
character2.rect.x = 200
character2.rect.y = 110


characters = []
characters.append(character)
characters.append(character2)


selectedChar = [character]
##while True:
##    screen.fill(0)
##    text = pygame.font.Font(None, 30).render("VS", True, (200,200,200), (0,0,0))
##    screen.blit(text, (135, 150))
##    for events in pygame.event.get():
##        if events.type == pygame.QUIT:
##            pygame.quit()
##            sys.exit(1)
##
##    for selChar in characters:
##        selChar.Update()
##        screen.blit(selChar.bdy, selChar.rect)
##
##    pygame.display.update()
##    pygame.time.Clock().tick(60)
    






        
