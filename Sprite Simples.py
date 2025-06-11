import pygame
class Jogador(object):
    
    def __init__(self):
        
        self.sprite=pygame.image.load("linkEx1.png")
        self.x = 0
        self.y = 0
    def handle_keys(self):
        key = pygame.key.get_pressed()
        distancia = 1
        if key[pygame.K_DOWN]: 
            self.y += distancia 
        elif key[pygame.K_UP]: 
            self.y -= distancia 
        if key[pygame.K_RIGHT]: 
            self.x += distancia 
        elif key[pygame.K_LEFT]: 
            self.x -= distancia 

    def draw(self, surface):
       surface.blit(self.sprite, (self.x, self.y))
        
   

pygame.init()


tela=pygame.display.set_mode((800,600))

jogador=Jogador()

rodar=True
while rodar:
    
    for controle in pygame.event.get():
        if controle.type==pygame.QUIT:
            rodar=False
        if controle.type == pygame.KEYDOWN and controle.key == pygame.K_ESCAPE:
            rodar=False

    
    tela.fill((255, 255, 255))

    jogador.draw(tela)
    jogador.handle_keys()
    pygame.display.update()

    
pygame.quit()
