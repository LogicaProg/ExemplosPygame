import pygame
pygame.init()
tela=pygame.display.set_mode((600,600))
tela.fill("blue")
musica = pygame.mixer.Sound("menubgm by Nagumorizu.mp3")
musica.set_volume(0.40)
musica.play(-1, 0, 1000)

running = True
while running:
    
   
    
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            musica.stop()
            
            
    pygame.display.update()
pygame.quit()
