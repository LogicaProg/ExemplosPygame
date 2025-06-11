import pygame
def texto(texto):
    white=(255,255,255)
    red=(255,0,0)
    
 
    font=pygame.font.Font('freesansbold.ttf', 60)
    text = font.render(texto, True, red, white)
   

    textRect = text.get_rect()

    textRect.center = (400,300)
    tela.blit(text, textRect)
    pygame.display.flip()
    

pygame.init()
tela=pygame.display.set_mode((800,600))
tela.fill((0,0,0,))
rodar=True
while rodar:
    for controle in pygame.event.get():
        if controle.type==pygame.QUIT:
            rodar=False
        if controle.type == pygame.KEYDOWN and controle.key == pygame.K_ESCAPE:
            rodar=False
    texto('Exemplo')

pygame.display.update()
pygame.quit()
