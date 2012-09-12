import pygame
import sys
pygame.init()

window=pygame.display.set_mode([640,480])
pygame.display.set_caption("accp GANGNAM -...")
font=pygame.font.Font("freesansbold.ttf",32)
#font2=pygame.font.Font("LATINWD.ttf",50)

def TitleScreen(window,font):
    textColor=pygame.Color(255,255,255)
    text=font.render("GANGNAM STYLE:",False,textColor)
    text2=font.render("GABRIEL A. SAPITULA",False,textColor)
    text3=font.render("CHRISTIAN JOY VENTURA",False,textColor)
    text4=font.render("FERDINAND F. MABALOT",False,textColor)
    window.blit(text,[0,0])
    window.blit(text2,[0,40])
    window.blit(text3,[0,80])
    window.blit(text4,[0,120])


while True:
    TitleScreen(window,font)
    events=pygame.event.get()
    for event in events:
        if(event.type==pygame.QUIT):
            pygame.quit()
            sys.exit()
    pygame.display.update()
