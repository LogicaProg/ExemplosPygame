import pygame 
pygame.init() 

tela = pygame.display.set_mode((500, 500)) 
pygame.display.set_caption("Movimentar um retângulo") 

x = 200
y = 200

largura = 20
altura = 20

velocidade = 10
rodar = True


while rodar: 
	pygame.time.delay(10) 
	
	for evento in pygame.event.get(): 
		if evento.type == pygame.QUIT: 
			rodar = False
	tecla = pygame.key.get_pressed() 
	
	if tecla[pygame.K_LEFT] and x>0: 
		x -= velocidade 
		
	if tecla[pygame.K_RIGHT] and x<500-largura: 
		x += velocidade 
		
	if tecla[pygame.K_UP] and y>0: 
		y -= velocidade 
		
	if tecla[pygame.K_DOWN] and y<500-altura: 
		y += velocidade 
		
	tela.fill((0, 0, 0)) 
	pygame.draw.rect(tela, (255, 0, 0), (x, y, largura, altura)) 
	pygame.display.update() 

pygame.quit()

