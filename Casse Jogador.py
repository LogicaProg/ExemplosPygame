import pygame
class Jogador(object):
    
    def __init__(self):
        
        self.rect = pygame.Rect(60, 60, 30, 30)
        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(1, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -1)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, 1)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 128), self.rect)
   

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
