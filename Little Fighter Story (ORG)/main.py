import pygame, sys, math, time
from char_anims import Characters
from story_manager import StoryManager


pygame.init()


screen = pygame.display.set_mode((900, 384))
screen.fill(0)
screen.blit(pygame.font.Font(None, 30).render("Loading...", True, (150,150,150), (0,0,0)), (400, 300))
pygame.display.update()


time.sleep(8)

###### Rex ######
rex = Characters()
rex.__init__self__("sys/Rex_0.bmp", 80, 80, 30)
rex.__init__self__mirror__("sys/Rex_0_mirror.bmp", 80, 80, 30)
rex.pos[0] = 300
rex.pos[1] = 200
rex.action = 0
rex.direction = 1
rex.s_pos = [20, 72]
rex.frames4 = [23, 23]
rex.frames4_b = [26, 26]

###### Davis ######
davis = Characters(name="Davis")
davis.__init__self__("sys/davis_0.bmp", 80, 80, 70)
davis.__init__self__("sys/davis_1.bmp", 80, 80, 70)
davis.__init__self__("sys/davis_2.bmp", 80, 80, 40)
davis.__init__self__mirror__("sys/davis_0_mirror.bmp", 80, 80, 70)
davis.__init__self__mirror__("sys/davis_1_mirror.bmp", 80, 80, 70)
davis.__init__self__mirror__("sys/davis_2_mirror.bmp", 80, 80, 40)
davis.pos[0] = 100
davis.pos[1] = 200
davis.s_pos = [22, 73]
#Create All His Unique Animation Frames
#Running
davis.frames3 = [20, 21, 22, 21, 20]
davis.action = 1

davis.direction = 1
davis.name = "Davis"
davis.head = pygame.image.load("sys/davis_f.bmp")


####### Noren #######
noren = Characters(name="Noren")
noren.__init__self__("sys/dennis_0.bmp", 80, 80, 70)
noren.__init__self__("sys/dennis_1.bmp", 80, 80, 70)
noren.__init__self__("sys/dennis_2.bmp", 80, 80, 50)
noren.__init__self__mirror__("sys/dennis_0_mirror.bmp", 80, 80, 70)
noren.__init__self__mirror__("sys/dennis_1_mirror.bmp", 80, 80, 70)
noren.__init__self__mirror__("sys/dennis_2_mirror.bmp", 80, 80, 50)
noren.pos[0] = 1000
noren.pos[1] = 200
noren.s_pos = [22, 73]
noren.action = 0
noren.direction = -1
#Create All His Unique Animation Frames
#Running
noren.frames3 = [20, 21, 22, 21, 20]
noren.frames3_b = [27, 28, 29, 28, 27]
#Stance
noren.frames4 = [13, 13]
noren.frames4_b = [16, 16]

noren.name = "Noren"
noren.head = pygame.image.load("sys/dennis_f.bmp")


#### Enemies ####

########## Bonu ###########
bonu = Characters(name="Bonu")
bonu.__init__self__("sys/bonu_0.bmp", 80, 80, 35)
bonu.__init__self__mirror__("sys/bonu_0_mirror.bmp", 80, 80, 30)
bonu.pos[0] = 1900
bonu.pos[1] = 200
bonu.s_pos = [23, 73]
#Create All His Unique Animation Frames
#Running
bonu.frames3 = [20, 21, 22, 21, 20]
bonu.frames3_b = [26, 27, 28, 27, 26]
#Stance
bonu.frames4 = [19, 19]
bonu.frames4_b = [10, 10]
bonu.action = 0

bonu.direction = 1
bonu.name = "BanditLeader"
bonu.head = pygame.image.load("sys/bonu_f.bmp")

characters = []
characters.append(rex)
characters.append(davis)
characters.append(noren)
characters.append(bonu)

bandits = []

screen.fill(0)
screen.blit(pygame.font.Font(None, 30).render("Spawning Enemies", True, (150,150,150), (0,0,0)), (400, 300))
pygame.display.update()

def Load_Bandits(x=2200, y=30):
    x = x
    y = y
    for i in range(24):
        bandits.append(Characters())
        ########## Bandit ###########
        bandits[i].__init__self__("sys/bandit_0.bmp", 80, 80, 35)
        bandits[i].__init__self__mirror__("sys/bandit_0_mirror.bmp", 80, 80, 30)
        y += 60
        if y >= 300:
            x += 70
            y = 100
        bandits[i].pos[0] = x
        bandits[i].pos[1] = y
        bandits[i].s_pos = [23, 73]
        #Create All His Unique Animation Frames
        #Running
        bandits[i].frames3 = [20, 21, 22, 21, 20]
        bandits[i].frames3_b = [26, 27, 28, 27, 26]
        #Stance
        bandits[i].frames4 = [19, 19]
        bandits[i].frames4_b = [10, 10]
        bandits[i].action = 0

        bandits[i].direction = 1
        bandits[i].name = "Bandit"
        bandits[i].head = pygame.image.load("sys/bandit_f.bmp")
Load_Bandits()

monks = []

screen.fill(0)
screen.blit(pygame.font.Font(None, 30).render("Spawning Supports", True, (150,150,150), (0,0,0)), (400, 300))
pygame.display.update()

def Load_Monks(x=1900, y=100):
    x = x
    y = y
    for i in range(4):
        monks.append(Characters("Monk", (x,y)))
        ########## Bandit ###########
        monks[i].__init__self__("sys/monk_0.bmp", 80, 80, 35)
        monks[i].__init__self__mirror__("sys/monk_0_mirror.bmp", 80, 80, 30)
        y += 60
        if y >= 400:
            x += 70
            y = 100
        monks[i].s_pos = [23, 73]
        #Create All His Unique Animation Frames
        #Running
        monks[i].frames3 = [20, 21, 22, 21, 20]
        monks[i].frames3_b = [26, 27, 28, 27, 26]
        #Stance
        monks[i].frames4 = [19, 19]
        monks[i].frames4_b = [10, 10]
        monks[i].action = 0

        monks[i].direction = 1
        monks[i].name = "Monk"
        monks[i].head = pygame.image.load("sys/monk_f.bmp")
Load_Monks(x=100)

#StoryManager
stagePosX = 0
storyManager = StoryManager(characters)
storyManager.monks = monks
storyManager.banditsRed = bandits

storyManager.bg = pygame.image.load("bg/sp_dragon_fighters.png").convert()

a = 0
fade = pygame.Surface((900, 384)).convert()
fade.fill((0,0,0))
def EndScene():
    global a
EndScene()  
stageWidth = storyManager.bg.get_rect().width


screen.fill(0)
screen.blit(pygame.font.Font(None, 30).render("Initilizing Camera", True, (150,150,150), (0,0,0)), (400, 300))
pygame.display.update()

def Follow(target):
    global stagePosX
    if stagePosX < target - 400 and stagePosX < stageWidth * 9 - 215:
        stagePosX += math.sqrt(math.pow(stagePosX - target + 400, 2)) / 100
        
    if stagePosX > target - 400 and stagePosX > 0:
        target = target - 400
        stagePosX -= math.sqrt(math.pow(stagePosX - target, 2)) / 120

gate = pygame.image.load("bg/sp-forest.bmp").convert()
def BackGround():
    for i in range(10):
        screen.blit(storyManager.bg, (i * storyManager.bg.get_rect().width - stagePosX, 0))
    if storyManager.ACT == 2:
        screen.blit(gate, (0 - stagePosX, 0))

def ToBeContinued():
    screen.fill(0)
    time.sleep(1)
    for i in range(255):
        screen.fill(0)
        screen.blit(pygame.font.Font(None, 30).render("To Be Continued", True, (i,i,i), (0,0,0)), (370, 200))
        pygame.display.update()
    time.sleep(2)
    for i in range(255):
        screen.fill(0)
        screen.blit(pygame.font.Font(None, 30).render("To Be Continued", True, (255 - i, 255 - i,255 - i), (0,0,0)), (370, 200))
        pygame.display.update()
    time.sleep(2)
    pygame.quit()
        
    
    

all_sprites = pygame.sprite.LayeredUpdates()
for enemyChar in bandits:
    all_sprites.add(enemyChar)
for enemyChar in monks:
    all_sprites.add(enemyChar)
for enemyChar in characters:
    all_sprites.add(enemyChar)
    
screen.fill(0)
screen.blit(pygame.font.Font(None, 30).render("Adding Characters Sprites", True, (150,150,150), (0,0,0)), (400, 300))
pygame.display.update()
while True:
    targetObject = storyManager.targetObject
    Follow(storyManager.camFocus.pos[0])
    for chars in all_sprites:
        all_sprites.change_layer(chars, chars.rect.bottom)
    screen.fill(0)
    BackGround()
    
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            sys.exit(1)

    for selChar in characters:
        selChar.Update(stagePosX)
        selChar.targetObject = targetObject
        screen.blit(selChar.shadow, (selChar.pos[0] + selChar.s_pos[0] - stagePosX, selChar.pos[1] + selChar.s_pos[1]))
        
    for enemChar in bandits:
        enemChar.Update(stagePosX)
        enemChar.action = storyManager.enemiesAction
        screen.blit(enemChar.shadow, (enemChar.pos[0] + enemChar.s_pos[0] - stagePosX, enemChar.pos[1] + enemChar.s_pos[1]))
        enemChar.targetObject = targetObject
        
    for heroChar in monks:
        heroChar.Update(stagePosX)
##        heroChar.action = storyManager.herosAction
##        if heroChar.isPatrol:
##            pygame.draw.line(screen, (255,0,0), (heroChar.pos[0] + 50 - stagePosX, heroChar.pos[1] + 40), (heroChar.targetPos[0] - stagePosX, heroChar.targetPos[1]))
##            pygame.draw.rect(screen, (255,0,255), [heroChar.targetPos.x - stagePosX, heroChar.targetPos.y, heroChar.targetPos.width, heroChar.targetPos.height], 1)
        screen.blit(heroChar.shadow, (heroChar.pos[0] + heroChar.s_pos[0] - stagePosX, heroChar.pos[1] + heroChar.s_pos[1]))
##        heroChar.targetObject = targetObject
        
    all_sprites.update()
    all_sprites.draw(screen)
        
    ### Update Scenes Fade-In-Out ###
    if storyManager.sceneEnd == True:
        a += 2
        fade.set_alpha(a)
        screen.blit(fade, (0,0))
        pygame.display.update()
        if int(a) >= 255:
            a = 0
            storyManager.timer = 0
            storyManager.sceneEnd = False
            
    if storyManager.TBC == True:
        ToBeContinued()
        storyManager.TBC = False
    
    #Story_Manager UI_Update
    if storyManager.isScene == True:
        pygame.draw.rect(screen, (0,0,0,0), storyManager.boarder, 0)
        pygame.draw.rect(screen, (50,50,50,100), (10,5, 600, 130), 3)
        screen.blit(storyManager.head, (15,10))
        screen.blit(storyManager.text, (140, 15))
    storyManager.Update()
    
    pygame.display.update()

    pygame.time.Clock().tick(70)
