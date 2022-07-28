import random, pygame, sys
# pygame setup
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1100,800))
pygame.display.set_caption('TIME RUNNER')
fps = pygame.time.Clock() # fps value in last lines


'''FUNCTIONS & CLASSES'''
class Button(pygame.sprite.Sprite):
    def __init__(self,posX,posY,OnIMGpath,OffIMGpath,soundPath):
        super().__init__()
        self.OnIMG = pygame.image.load(OnIMGpath)
        self.OffIMG = pygame.image.load(OffIMGpath)
        self.rect = self.OffIMG.get_rect(topleft = (posX,posY))
        self.image = self.OnIMG
        self.sound = pygame.mixer.Sound(soundPath)
        self.soundPlayed = False
    def update(self):
        self.mousePos = pygame.mouse.get_pos()
        if self.rect.collidepoint(self.mousePos):
            self.image = self.OnIMG
            if not self.soundPlayed:
                self.sound.play()
                self.soundPlayed = True
        else:
            self.image = self.OffIMG
            self.soundPlayed = False
        
buttonSprites = pygame.sprite.Group()
buttonGO = Button(750,280,'images/menu/button GO! on.png','images/menu/button GO! off.png','audio/button_select.mp3')
buttonSprites.add(buttonGO)

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #closing window
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if buttonGO.rect.collidepoint(mousePos):
                print('clicked')

    screen.fill((200,200,200))
    buttonSprites.draw(screen)
    buttonSprites.update()

    pygame.display.update() #updating display
    fps.tick(60)