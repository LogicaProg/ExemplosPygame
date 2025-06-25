import pygame


pygame.init()

screen=pygame.display.set_mode((1200,700))
X=1200
Y=700
x=400
y=430

def Menu():
    
    screen.fill((0,0,0))
    font = pygame.font.Font('freesansbold.ttf', 40)
    fonte = pygame.font.Font('freesansbold.ttf', 90)
    fontCredito = pygame.font.Font('freesansbold.ttf', 15)

    textm = font.render('Iniciar Jogo', True, "white")

    textRectm = textm.get_rect()
 
    textRectm.center = (X // 2,450)
    screen.blit(textm, textRectm)
    texts = font.render('Selecionar Nível', True, "white")


    textRects = texts.get_rect()
 

    textRects.center = (X // 2,550)
    screen.blit(texts, textRects)
    texttt = fonte.render('JOGO A', True, "Pink")


    textRecttt = texttt.get_rect()
 

    textRecttt.center = (X // 2,250)
    screen.blit(texttt, textRecttt)
    texttt3 = fontCredito.render('[Aperte Space]', True, "Pink")


    textRecttt3 = texttt3.get_rect()
 

    textRecttt3.center = (1100,650)
    screen.blit(texttt3, textRecttt3)
   
    textttc = fontCredito.render('By Autor (2025)', True, "lightBlue")


    textRectttc = textttc.get_rect()
 

    textRectttc.center = (X // 2,650)
    screen.blit(textttc, textRectttc)

    
    
    pygame.display.flip()
    
running=True
while rodar:
    Menu()
    pygame.draw.rect(screen, "pink", (x,y, 30,30))
    for e in pygame.event.get():
            if e.type == pygame.QUIT:
              running = False
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
              running = False
              pygame.quit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP :
               x=400
               y=430
            
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN  :
               x=400
               y=530
    pygame.display.flip()
