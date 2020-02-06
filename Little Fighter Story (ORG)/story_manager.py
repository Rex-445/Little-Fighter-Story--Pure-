import pygame
import math

pygame.init()



class StoryManager():
    def __init__(self, chars=[]):
        self.scene = 0
        self.ACT = 1

        ## StoryManager *UI
        self.head = None
        self.word = "This is a text \ This is the second line"
        self.text = pygame.font.Font(None, 25).render(self.word, True, (200,200,200), (0,0,0))
        self.boarder = pygame.Rect(10,5, 600,130)

        ## StoryManager *Sounds
        self.sounds = []
        self.sounds = ["sounds/message.wav"]

        ## StoryManager *Game Tools
        self.heads = chars
        self.head = self.heads[0].head
        self.targetObject = self.heads[1]
        self.bg = pygame.image.load("bg/sp_dragon_fighters.png").convert()

        ## StoryManager *Tools
        self.timer = 15
        self.isScene = False
        self.sceneEnd = False
        self.TBC = False
        self.enemiesAction = 0
        self.herosAction = 0
        self.camFocus = self.heads[0]

        ##StoryManager *Supports
        self.monks = []
        self.banditsRed = []
        self.banditsBlue = []

    def PlaySound(self, type=0):
        pygame.mixer.Sound(self.sounds[type]).play()

    def Update(self):
        self.timer -= 0.1
        if self.timer <= 0:
            self.NextPhase()
    def NextPhase(self):
        self.scene += 1
        self.PlaySound()
        if self.ACT == 1:
            #Phase 2
            if self.scene == 2:
                for monk in self.monks:
                    monk.isPatrol = True
                    monk.pos[0] = monk.points[0]
                self.isScene = True
                self.targetObject = self.heads[0]
                self.head = self.heads[0].head
                self.heads[1].action = 0
                self.word = "Uhhhhhhhh!!!!... So Freaking Bored"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 20
                
            #Phase 3
            if self.scene == 3:
                self.head = self.heads[1].head
                self.word = "...."
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 5

            #Phase 4
            if self.scene == 4:
                self.head = self.heads[1].head
                self.word = "Again With This?"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 5
            if self.scene == 5:
                self.head = self.heads[1].head
                self.word = "Why Always Looking For Action"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 20

            #Phase 6
            if self.scene == 6:
                self.head = self.heads[0].head
                self.word = "Dont't except you to UNDERSTAND"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 20

            #Phase 7
            if self.scene == 7:
                self.head = self.heads[1].head
                self.word = "Just saying, you care a lot about fights ( XD )"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.heads[2].action = 1
                self.heads[2].frame = 0
                self.heads[2].direction = -1
                self.timer = 25

            #Phase 8
            if self.scene == 8:
                self.targetObject = self.heads[2]
                self.camFocus = self.heads[2]
                self.heads[2].action = 0
                self.heads[2].direction = -1
                self.head = self.heads[2].head
                self.word = "Hey Guys Whats Going On"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10

            #Phase 9
            if self.scene == 9:
                self.head = self.heads[1].head
                self.word = "Nothing you?"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10

            #Phase 10
            if self.scene == 10:
                self.head = self.heads[2].head
                self.word = "The Usual"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 11
            if self.scene == 11:
                self.targetObject = self.heads[0]
                self.camFocus = self.heads[0]
                self.head = self.heads[0].head
                self.word = "I'm gonna go stick my head in an oven"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 12
            if self.scene == 12:
                self.head = self.heads[0].head
                self.word = "See if something good happens"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 13

            #Phase 13
            if self.scene == 13:
                self.head = self.heads[1].head
                self.word = "Or just go outside and explore nature"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 14
            if self.scene == 14:
                self.head = self.heads[0].head
                self.word = "Funny"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 9

            #Phase 15
            if self.scene == 15:
                self.head = self.heads[0].head
                self.word = "But I'll do it anyways"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10

            #Phase 16
            if self.scene == 16:
                self.head = self.heads[0].head
                self.word = "I'm desprate"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 13

            #Phase 17
            if self.scene == 17:
                self.head = self.heads[2].head
                self.word = "Later"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10

            #Phase 18
            if self.scene == 18:
                self.heads[0].action = 1
                self.head = self.heads[0].head
                self.word = "Not the first time you're happy to see me leave"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10

            #Phase 19
            if self.scene == 19:
                self.head = self.heads[1].head
                self.camFocus = self.heads[1]
                self.word = "Don't kill anyone"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10

            #Phase 20
            if self.scene == 20:
                self.head = self.heads[0].head
                self.word = "We'll see"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 20

            #Phase 21
            if self.scene == 21:
                self.isScene = True
                self.heads[0].action = 0
                self.isScene = False
                self.timer = 15

            #Phase 22
            if self.scene == 22:
                self.isScene = True
                self.head = self.heads[1].head
                self.word = "He's a true Warrior though"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 18

            #Phase 23
            if self.scene == 23:
                self.head = self.heads[2].head
                self.word = "No-one else thirsts for battle as he does"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 20

            #Phase 24
            if self.scene == 24:
                self.targetObject = self.heads[1]
                self.head = self.heads[2].head
                self.word = "His ambitions thrives him to move on"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 18

            #Phase 25
            if self.scene == 25:
                self.head = self.heads[1].head
                self.word = "Tis the reason Master Raul en-trusted him with a gate"
                self.text = pygame.font.Font(None, 22).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 18

            #Phase 26
            if self.scene == 26:
                self.head = self.heads[2].head
                self.word = "Hopefully it was'nt a mistake"
                self.text = pygame.font.Font(None, 22).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 27
            if self.scene == 27:
                self.head = self.heads[1].head
                self.word = "A.."
                self.text = pygame.font.Font(None, 22).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 8

            #Phase 28
            if self.scene == 28:
                self.head = self.heads[1].head
                self.word = "A 'Mistake' ?"
                self.text = pygame.font.Font(None, 22).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10

            #Phase 29
            if self.scene == 29:
                self.head = self.heads[2].head
                self.word = "About Guarding The Gate"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 12

            #Phase 30
            if self.scene == 30:
                self.head = self.heads[1].head
                self.word = "What are you talking about"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 31
            if self.scene == 31:
                self.head = self.heads[2].head
                self.word = "Remember the 'TOX War'"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 32
            if self.scene == 32:
                self.head = self.heads[1].head
                self.word = "The very battle that brought the Temple down"
                self.text = pygame.font.Font(None, 22).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 33
            if self.scene == 33:
                self.head = self.heads[1].head
                self.word = "But somehow we evaded Defeat"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 34
            if self.scene == 34:
                self.head = self.heads[1].head
                self.word = "Right"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 7

            #Phase 35
            if self.scene == 35:
                self.head = self.heads[2].head
                self.word = "Correct"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10

            #Phase 36
            if self.scene == 36:
                self.head = self.heads[2].head
                self.word = "Rex was told to guard the weapon base"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 37
            if self.scene == 37:
                self.head = self.heads[2].head
                self.word = "Where the very 'Sword of Dragon' was kept"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 38
            if self.scene == 38:
                self.head = self.heads[1].head
                self.word = "Oh.... that incident"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 39
            if self.scene == 39:
                self.head = self.heads[2].head
                self.word = "Sorry to bring it up."
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10

            #Phase 40
            if self.scene == 40:
                self.head = self.heads[2].head
                self.word = "But that little 'mistake' he made"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 41
            if self.scene == 41:
                self.head = self.heads[2].head
                self.word = "Could've brought down countless lives"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 42
            if self.scene == 42:
                self.head = self.heads[1].head
                self.word = "Well at least he fixed it"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 43
            if self.scene == 43:
                self.head = self.heads[2].head
                self.word = "Barely"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 44
            if self.scene == 44:
                self.head = self.heads[1].head
                self.word = "Yeah. I guess"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 45
            if self.scene == 45:
                self.head = self.heads[2].head
                self.word = "He did that once"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 46
            if self.scene == 46:
                self.head = self.heads[2].head
                self.word = "Lets hope it wou'nt happen again"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15

            #Phase 47
            if self.scene == 47:
                self.heads[0].action = 0
                self.heads[0].action = 2
                self.head = self.heads[1].head
                self.word = "(sigh)"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 8

            #Phase 48
            if self.scene == 48:
                self.heads[0].action = 3
                self.camFocus = self.heads[0]
                self.head = self.heads[0].head
                self.targetObject = self.heads[0]
                self.word = "Bar the doors!!"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 9

            #Phase 49
            if self.scene == 49:
                self.heads[0].action = 3
                self.head = self.heads[1].head
                self.camFocus = self.heads[1]
                self.word = "Whats wrong!?"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 8

            #Phase 50
            if self.scene == 50:
                self.head = self.heads[0].head
                self.heads[1].frame = 0
                self.heads[1].action = 3
                self.word = "Secure the perimeter!!"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10


            #Phase 51
            if self.scene == 51:
                self.heads[2].frame = 0
                self.heads[2].action = 3
                self.head = self.heads[2].head
                self.word = "Whats going on?!!"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10


            #Phase 52
            if self.scene == 52:
                self.head = self.heads[0].head
                self.camFocus = self.heads[0]
                self.word = "The Gate is under attack!!"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10


            #Phase 53
            if self.scene == 53:
                self.head = self.heads[1].head
                self.camFocus = self.heads[1]
                self.word = "WHAT!!!"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 5


            #Phase 54
            if self.scene == 54:
                self.head = self.heads[2].head
                self.camFocus = self.heads[2]
                self.word = "NO FREAKING WAY!!!!!"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10


            #Phase 55
            if self.scene == 55:
                self.head = self.heads[1].head
                self.camFocus = self.heads[1]
                self.word = "WHATS THE TREATH!!"
                self.text = pygame.font.Font(None, 25).render(self.heads[1].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                self.isScene = True


            #Phase 56
            if self.scene == 56:
                self.camFocus = self.heads[0]
                self.head = self.heads[0].head
                self.word = "Bandits"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10


            #Phase 57
            if self.scene == 57:
                self.head = self.heads[0].head
                self.word = "Don't know how they got here.."
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10


            #Phase 58
            if self.scene == 58:
                self.head = self.heads[0].head
                self.word = "But we have to move NOW!!!"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10


            #Phase 59
            if self.scene == 59:
                self.head = self.heads[0].head
                self.word = "IF THE GATE FALLS, SO DOES THE DRAGON TEMPLE!!"
                self.text = pygame.font.Font(None, 22).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10


            #Phase 60
            if self.scene == 60:
                self.head = self.heads[2].head
                self.word = "We should hurry then!!"
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10


            #Phase 61
            if self.scene == 61:
                self.targetObject = self.heads[0]
                self.heads[0].direction = 1
                self.heads[1].direction = 1
                self.heads[2].direction = 1
                self.heads[0].action = 2
                self.heads[1].action = 2
                self.heads[2].action = 2
                self.isScene = False
                self.sceneEnd = True
                self.timer = 10

            #End_Phase
            if self.scene == 62:
                self.isScene = False
                self.timer = math.inf
                self.scene = 0
                self.ACT = 2

        #Act 2
        if self.ACT == 2:
            #Phase 1
            if self.scene == 1:
                self.isScene = False
                self.bg = pygame.image.load("bg/forest-sp.png").convert()
                self.targetObject = self.heads[0]
                self.heads[0].pos[0] = 0
                self.heads[2].pos[0] = -100
                self.heads[1].pos[0] = -200
                
                self.heads[0].action = 2
                self.heads[1].action = 2
                self.heads[2].action = 2
                self.timer = 10
                for monk in self.monks:
                    monk.isPatrol = False
                    monk.pos[0] = monk.points[0]
                    monk.action = 0
                    monk.direction = 1
                
            #Phase 2
            if self.scene == 2:
                self.isScene = True
                self.heads[0].action = 0
                self.heads[1].action = 0
                self.heads[2].action = 0
                self.head = self.heads[0].head
                self.word = "There's the Leader"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 3
            if self.scene == 3:
                self.isScene = False
                self.camFocus = self.heads[3]
                self.heads[3].action = 1
                self.timer = 20
                
            #Phase 4
            if self.scene == 4:
                pygame.mixer.music.load('Sounds/intro.mp3')
                pygame.mixer.music.play(-1)
                self.heads[3].action = 0
                self.timer = 10
                
            #Phase 5
            if self.scene == 5:
                self.isScene = True
                self.head = self.heads[3].head
                self.word = "Wait..."
                self.text = pygame.font.Font(None, 25).render(self.heads[3].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 5
                
            #Phase 6
            if self.scene == 6:
                self.head = self.heads[3].head
                self.word = "Kids?!"
                self.text = pygame.font.Font(None, 25).render(self.heads[3].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 7
            if self.scene == 7:
                self.head = self.heads[3].head
                self.word = "Is This A Joke!"
                self.text = pygame.font.Font(None, 25).render(self.heads[3].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15
                
            #Phase 8
            if self.scene == 8:
                self.head = self.heads[0].head
                self.word = "Get To The Point"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 9
            if self.scene == 9:
                self.head = self.heads[3].head
                self.heads[3].action = 1
                self.word = "When I heard there were Three Heros for this Gate"
                self.text = pygame.font.Font(None, 20).render(self.heads[3].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15
                
            #Phase 10
            if self.scene == 10:
                self.word = "I was expecting more of a challange"
                self.text = pygame.font.Font(None, 25).render(self.heads[3].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 13
                
            #Phase 11
            if self.scene == 11:
                self.heads[3].action = 0
                self.word = "Not A Couple Of Trainees"
                self.text = pygame.font.Font(None, 25).render(self.heads[3].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 13
                
            #Phase 12
            if self.scene == 12:
                self.enemiesAction = 1
                self.head = self.heads[0].head
                self.camFocus = self.heads[0]
                self.word = "Looks can be decieving"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 13
            if self.scene == 13:
                self.head = self.heads[3].head
                self.word = "No matter"
                self.text = pygame.font.Font(None, 25).render(self.heads[3].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 14
            if self.scene == 14:
                self.camFocus = self.heads[3]
                self.word = "This only made my job much easier"
                self.text = pygame.font.Font(None, 25).render(self.heads[3].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15
                
            #Phase 15
            if self.scene == 15:
                self.word = "It only pains me to waste this army on you three"
                self.text = pygame.font.Font(None, 22).render(self.heads[3].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 25
                
            #Phase 16
            if self.scene == 16:
                self.enemiesAction = 0
                self.head = self.heads[0].head
                self.word = "//Crap//"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 17
            if self.scene == 17:
                self.camFocus = self.heads[2]
                self.head = self.heads[2].head
                self.word = " * I don't get it * "
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 18
            if self.scene == 18:
                self.head = self.heads[2].head
                self.word = " * Why would 'Bandits' want a Dragon Gate * "
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 15
                
            #Phase 19
            if self.scene == 19:
                self.heads[0].action = 1
                self.head = self.heads[2].head
                self.word = " * Unless * "
                self.text = pygame.font.Font(None, 25).render(self.heads[2].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 20
            if self.scene == 20:
                self.heads[0].action = 0
                self.camFocus = self.heads[0]
                self.head = self.heads[0].head
                self.word = "Does't matter what happens"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 21
            if self.scene == 21:
                self.head = self.heads[0].head
                self.word = "You're not getting through"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 22
            if self.scene == 22:
                self.head = self.heads[3].head
                self.word = "Thats it you impress me before you die"
                self.text = pygame.font.Font(None, 25).render(self.heads[3].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 23
            if self.scene == 23:
                self.head = self.heads[0].head
                self.word = "Lets finish this"
                self.text = pygame.font.Font(None, 25).render(self.heads[0].name + ": " + self.word, True, (200,200,200), (0,0,0))
                self.timer = 10
                
            #Phase 24
            if self.scene == 24:
                self.isScene = False
                self.sceneEnd = True
                self.timer = 30
                self.ACT = 3
                self.scene = 0


        #Act 3
        if self.ACT == 3:          
            #Phase 1
            if self.scene == 1:
                self.head = self.heads[0].head
                self.timer = math.inf
                self.TBC = True
                

        
