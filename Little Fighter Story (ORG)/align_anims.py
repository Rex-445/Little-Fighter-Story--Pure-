import pygame, sys, pickle, pyglet
from pygame.locals import *
from button import Button



pygame.init()

class Align_Characters():
    def __init__(self):
        self.sprite = pygame.image.load("sys/Rex_0.bmp")
        self.shadow = pygame.image.load("sys/shadow.png").convert()
        self.head = pygame.image.load("sys/luke_f.bmp")
        self.defualt = ["sys/Bonu_0.bmp", "sys/Davis_1.bmp", "sys/Davis_1.bmp"]
        self.defualt2 = ["sys/Bonu_0_mirror.bmp", "sys/Davis_1_mirror.bmp", "sys/Rex_1_mirror.bmp"]

        self.width, self.height = (79, 79)

        #status of the character
        self.action = 1

        ################ Animations ###############
        #Standing
        self.frames1 = []

        #character frames
        self.cells = []
        self.flip = []
        self.targetCell = self.cells
        self.row = 0
        self.col = 0
        self.sounds = ["sounds/020.wav"]
        self.sndTimer = 1
        self.frame = 1
        self.direction = 1

        #Align On The X Axis
        self.alignX = [0,   0,    0,   0,   0,   0,   0,   0,   0,   -1,   -6,   11,   5,  -10,  -5,

                       13,   7,  -9,   0,   0,   3,   0,   3,   0,    0,    0,    2,   10,   0,  0,

                       3,    0,   0,   -5,  0,   0,   0,   0,   0,    0,    0,    0,    0,   0,  0,

                       0,    0,   0,    0,  0,   0,   0,   0,   0,    0,    0,    0,    0,   0,  0,

                       0,   0,   0,   0,   0,   0,   10,   13,   4,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   -1,   -2,   0,  -8,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   9,   0,   0,   0,  6,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0]

        #Align On The Y Axis
        self.alignY = [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   -1,   -1,   0,   0,   0,   0,   1,   1,   1,  0,  0,

                       5,   5,   10,   5,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0,

                       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0,  0]
        
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
        print(len(self.cells))

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


    def Update(self, wn):
        if self.sndTimer < 1:
            self.sndTimer += 0.05
        if self.action == 1:
            if self.direction == 1:
                self.x = self.rect.x + self.alignX[int(self.frame)]
                self.y = self.rect.y + self.alignY[int(self.frame)]
            if self.direction == -1:
                self.x = self.rect.x - self.alignX[int(self.frame)]
                self.y = self.rect.y + self.alignY[int(self.frame)]
            self.bdy = self.targetCell[int(self.frame)]
            wn.blit(self.bdy, (self.x, self.y))
        
        ############# Facing Right ############
        #standing
        if self.action == 0:
            if self.frame >= len(self.frames1):
                self.frame = 0
            if self.sndTimer >= 1 and self.bdy == self.cells[6]:
                snd = pygame.mixer.Sound(self.sounds[0])
                snd.set_volume(0.4)
                snd.play()
                self.sndTimer = 0
            if self.direction == 1:
                self.x = self.rect.x + self.alignX[self.frames1[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames1[int(self.frame)]]
            if self.direction == -1:
                self.x = self.rect.x - self.alignX[self.frames1[int(self.frame)]]
                self.y = self.rect.y + self.alignY[self.frames1[int(self.frame)]]
            self.bdy = self.targetCell[self.frames1[int(self.frame)]]
            wn.blit(self.bdy, (self.x, self.y))
            self.frame += 0.25




screen = pygame.display.set_mode((300,300))

character = Align_Characters()
character.__init__self__mirror__(character.defualt2[0], 80, 80, 70)
character.__init__self__mirror__(character.defualt2[1], 80, 80, 70)
character.__init__self__mirror__(character.defualt2[2], 80, 80, 50)
character.__init__self__(character.defualt[0], 80, 80, 70)
character.__init__self__(character.defualt[1], 80, 80, 70)
character.__init__self__(character.defualt[2], 80, 80, 50)
character.rect.x = 110
character.rect.y = 110


class Button:
    def __init__(self, pos=(0,0), wrd="Defualt", width=(60,20)):
        self.pos = list(pos)
        self.color = (0,10,50)
        self.word = wrd
        self.width = width
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width[0], self.width[1])

    def Update(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (100,10,50), self.rect, 1)
        text = pygame.font.Font(None, 20).render(self.word, True, (225,225,225), (self.color))
        screen.blit(text, (self.rect.x + 5, self.rect.y + self.rect.height / 2 - 7))
    def IsHover(self):
        mouse = pygame.mouse.get_pos()
        if mouse[0] > self.pos[0] and mouse[0] < self.pos[0] + self.rect.width:
            if mouse[1] > self.pos[1] and mouse[1] < self.pos[1] + self.rect.height:
                return True
        else:
            return False

buttons = []

left = Button(pos=(10, 250), wrd="Left")
right = Button(pos=(210, 250), wrd="Right")
capture = Button(pos=(10, 140), wrd="Capture")
animate = Button(pos=(230, 140), wrd="Animate")

up = Button(pos=(30, 30), wrd="^", width=(20,20))
down = Button(pos=(30, 60), wrd="v", width=(20,20))
leftArrow = Button(pos=(7, 44), wrd="<", width=(20,20))
rightArrow = Button(pos=(53, 44), wrd=">", width=(20,20))
save = Button(pos=(130, 44), wrd="Save")


buttons.append(left)
buttons.append(right)
buttons.append(capture)
buttons.append(animate)
buttons.append(up)
buttons.append(down)
buttons.append(leftArrow)
buttons.append(rightArrow)
buttons.append(save)

selectedChar = [character]

def Reload(type=-1):
    character.direction = type
    if type == -1:
        character.targetCell = character.flip
    if type == 1:
        character.targetCell = character.cells
def Save():
    data = [character.alignX, character.alignY]
    pickle.dump(data, open("data/Bonu.txt", "wb"))
    
data = pickle.load(open("data/Bonu.txt", "rb"))
character.alignX = data[0]
character.alignY = data[1]
while True:
    screen.fill(0)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        Reload(type=-1)
    if keys[pygame.K_d]:
        Reload(type=1)

    #Title    
    text = pygame.font.Font(None, 30).render("Frames And Animation", True, (255,255,255), (0,0,0))
    screen.blit(text, (50, 10))

    word = str("Frame: " + str(int(character.frame)))
    text = pygame.font.Font(None, 25).render(word, True, (255,255,255), (0,0,0))
    screen.blit(text, (110, 250))

    pygame.draw.rect(screen, (0,10,50), (character.rect.x - 35, character.rect.y - 35, 150,150), 0)
    pygame.draw.rect(screen, (100,10,50), (character.rect.x - 35, character.rect.y - 35, 150,150), 2)

    #####Buttons
    #Left Frame Button
    if left.IsHover():
        left.color = (0,100,200)
    else:
        left.color = (0,10,50)

    #Right Frame Button
    if right.IsHover():
        right.color = (0,100,200)
    else:
        right.color = (0,10,50)

    #Capture Frame Button
    if capture.IsHover():
        capture.color = (0,100,200)
    else:
        capture.color = (0,10,50)

    #Animate Frame Button
    if animate.IsHover():
        animate.color = (0,100,200)
    else:
        animate.color = (0,10,50)

    ############### Movement Buttons ##################
    #LeftArrow Button
    if leftArrow.IsHover():
        leftArrow.color = (0,100,200)
    else:
        leftArrow.color = (0,10,50)

    #Right Frame Button
    if rightArrow.IsHover():
        rightArrow.color = (0,100,200)
    else:
        rightArrow.color = (0,10,50)

    #Capture Frame Button
    if up.IsHover():
        up.color = (0,100,200)
    else:
        up.color = (0,10,50)

    #Animate Frame Button
    if down.IsHover():
        down.color = (0,100,200)
    else:
        down.color = (0,10,50)

    #Save AlignX and AlignY Button
    if save.IsHover():
        save.color = (0,100,200)
    else:
        save.color = (0,10,50)
    
    for b in buttons:
        b.Update(screen)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit(1)

        if events.type == pygame.MOUSEBUTTONDOWN:
            if left.IsHover():
                if character.frame > 0:
                    character.frame -= 1
            if right.IsHover():
                if character.frame < len(character.cells) - 1:
                    character.frame += 1
            if animate.IsHover():
                if character.action == 1:
                    character.action = 0
                    capture.word = "Reset"
            if capture.IsHover():
                if character.action == 1:
                    print("Added Frame: " + str(int(character.frame)))
                    character.frames1.append(character.frame)
                if character.action == 0:
                    character.action = 1
                    capture.word = "Capture"
                    character.frames1 = []
                
            if leftArrow.IsHover():
                character.alignX[character.frame] -= 1
            if rightArrow.IsHover():
                character.alignX[character.frame] += 1
                
            if up.IsHover():
                character.alignY[character.frame] -= 1
            if down.IsHover():
                character.alignY[character.frame] += 1
            if save.IsHover():
                Save()
                print("Saved Data")

    character.Update(screen)

    pygame.time.Clock().tick(100)
    pygame.display.update()
    






        
