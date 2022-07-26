import pygame
import random

#initialization
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
complete = False
color = (0, 0, 0)
height = 600
width = 600
screen= pygame.display.set_mode((height, width))
coins = ['h','t']
pygame.display.set_caption("game")
headf = pygame.image.load(r'head.png')
tailf = pygame.image.load(r'tail.png')
f1 = pygame.image.load(r'f1.png')
f2 = pygame.image.load(r'f2.png')
f3 = pygame.image.load(r'f3.png')
f4 = pygame.image.load(r'f4.png')
f5 = pygame.image.load(r'f5.png')
f6 = pygame.image.load(r'f6.png')
f7 = pygame.image.load(r'f7.png')
font = pygame.font.SysFont('comicsansms', 32)
frames = [f1, f2, f3, f4, f5, f6, f7]
class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.isanimating = False
        self.frames = frames
        self.currentframe = 0
        self.image =self.frames[self.currentframe]
        self.rect = self.image.get_rect()
        self.rect.topleft=[pos_x,pos_y]

    def animate(self):
        self.isanimating = True

    def update(self):
        if self.isanimating == True:
            self.currentframe += 1
            if self.currentframe >= len(self.frames):

                self.isanimating = False
                self.complete = True
                if flip == 'h':
                    self.frames.append(headf)
                elif flip == 't':
                    self.frames.append(tailf)

            self.image = self.frames[self.currentframe]

animation = pygame.sprite.Group()
coin = Coin(100,100)
animation.add(coin)
screen.fill(color)

def cointoss(x):

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_h:
            userin = 'h'
            coin.animate()
        if event.key == pygame.K_t:
            userin = 'T'
            coin.animate()
        if userin == flip:
            x += 50
        else:
            x -= 50
    return x

win = 0
wins = pygame.font.Font.render(font, 'you win', 1, 'white')
lose = pygame.font.Font.render(font, 'you lose', 1, 'white')

flip = random.choice(coins)
while True:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # allows a close button at corner of window
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                userin = 'h'
                coin.animate()
            if event.key == pygame.K_t:
                userin = 't'
                coin.animate()
            if userin == flip:
                win = 1
                complete = True
                print('you win')
                
            else:
                win = 2
                complete = True
                print('you lose')



    animation.draw(screen)
    animation.update()
    pygame.display.flip()
    if win == 1 and complete == True:
        screen.fill('black')
        pygame.Surface.blit(screen, wins, (0, 0))

    elif win == 2 and complete == True:
        screen.fill('black')
        pygame.Surface.blit(screen, lose, (0, 0))


    clock.tick(60)


