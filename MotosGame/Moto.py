import pygame


class Jogador(object):
    
    def __init__(self):
        x=60
        y=300
        self.rect = pygame.Rect(x, y, 30, 30)
        
    def handle_keys(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_LEFT]:
          
           if self.rect.x<0:
             self.rect.move_ip(1, 0)
           else:
              self.rect.move_ip(-1, 0)
           
        if key[pygame.K_RIGHT]:
           if self.rect.x>770:
             self.rect.move_ip(-1, 0)
           else:
             self.rect.move_ip(1, 0)
           
        if key[pygame.K_UP]:
           if self.rect.y>200: 
            self.rect.move_ip(0, -100)
         
        if self.rect.y<300 and not key[pygame.K_UP] : 
            self.rect.move_ip(0, 100)
        
    

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
   

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

