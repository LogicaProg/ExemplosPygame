import pygame

class Wall(object):
    
     def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 30, 30)
pygame.init()
walls=[]
level1 = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                  W       K           W", 
"W   W     WWWWWW   W WWWWWWWWWWWWWWWWWWW",
"W   W           W                 W    W",
"W   W         WWW         WW     W     W",
"WWWWW  WWWWWWWWWWWW                    W",
"W   W     W        WWWWWWWWWWWWWWWWWWWWW",
"W   W     W   WWW                      W",
"W   WWW WWW   W W       WWWWWWWWWW     W",
"W         W   W W     W       WWWWWWWW W",
"WWWWW W       W W     W                W",
"WW      WW      W  WWWWWWWWWWWWWWWWWWW W",
"W WWWW WWWW   WWW                      W",
"W     W        WWWWWWWWWWWWWWWWWWWWWW  W",                                      
"W     W                                W",
"W     WWWWWWWWWWWWWWWWW                W",
"W                        WWWWW     WW  W",
"W     WWWWWWWWWWWWWWWWWWW              W",
"W                         WW           W",
"W  WWWWWWWWWWWW               WWWWWWWWWW",
"W              WWWWWWWWWWWWWWWWWWW     W",
"W                                     W",
"WWWWWWWWWWWWWWWWW      WWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
]
screen=pygame.display.set_mode((1200,700))
def st1(level,):
 screen.fill((0,0,0))
 x = y = 0
 for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
       
     
        x += 30
    y +=30 
    x = 0
 
st1(level1)
for wall1 in walls:
                 pygame.draw.rect(screen, ("blue"), wall1.rect)
pygame.display.update()
