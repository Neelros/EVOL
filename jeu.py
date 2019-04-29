import pygame
from pygame.locals import *
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


def n1():
    pygame.display.set_caption("Jeu n1")
    font = pygame.font.Font(None,32)
    fond = pygame.image.load("noir.png").convert()
    fenetre.blit(fond,(0,0))
    text2 = font.render("1+1= ?",1,(205,200,177))
    fenetre.blit(text2, (450, 50))
    input_box = pygame.Rect(450, 100, 140,32)
    color_inactive = pygame.Color('cornsilk4')
    color_active = pygame.Color('cornsilk3')
    color=color_inactive
    active = False
    r1 = ''
    perso = pygame.image.load("pixel.png").convert_alpha()
    position_perso = perso.get_rect()
    fenetre.blit(perso, position_perso)
    s1 = pygame.mixer.Sound("son_fin_niv.wav")
    o1=pygame.image.load("o1.png").convert_alpha()
    o1.set_alpha(100)
    pygame.display.flip()
    continuer = 1
    pygame.key.set_repeat(400, 30)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    position_perso = position_perso.move(0,-3)
                elif event.key == K_DOWN:
                    position_perso = position_perso.move(0,3)
                elif event.key == K_RIGHT:
                    position_perso = position_perso.move(3,0)
                elif event.key == K_LEFT:
                    position_perso = position_perso.move(-3,0)
                fenetre.blit(fond, (0,0))
                fenetre.blit(perso, position_perso)
                pygame.display.flip()

            if event.type == MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(r1)
                    elif event.key == pygame.K_BACKSPACE:
                        r1 = r1[:-1]
                    else:
                        r1 += event.unicode
            if r1=='2': #REVOIR CONDITIONS (avec return attention pas transition)
                fenetre.blit(o1,(600,400))
                pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and 600<=event.pos[0]<=808 and 400<=event.pos[1]<=644:
                    print('oui')
                    s1.play()
                    t()

        fenetre.blit(fond, (0,0))
        fenetre.blit(text2, (450, 50))
        fenetre.blit(perso, position_perso)
        txt_surface = font.render(r1, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        fenetre.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(fenetre, color, input_box, 2)
        pygame.display.flip()



def t():
    pygame.display.set_caption("Transition...")
    fond = pygame.image.load("blanc.png").convert()
    fenetre.blit(fond, (0,0))
    pygame.display.update()
    continuer = 1
    pygame.key.set_repeat(400, 30)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 1<=event.pos[0]<=1200 and 1<=event.pos[1]<=800:
                print('yes')
                n2()
    fenetre.blit(fond,(0,0))
    pygame.display.flip()

def n2():
    pygame.display.set_caption("Jeu n2")
    fond = pygame.image.load("f2.png").convert()
    fenetre.blit(fond,(0,0))
    text3 = font.render("Comment dit au revoir un ion hydrogène?",1,(205,200,177))
    fenetre.blit(text3, (450, 50))
    input_box2 = pygame.Rect(450, 100, 140,32)
    color_inactive = pygame.Color('cornsilk4')
    color_active = pygame.Color('cornsilk3')
    color=color_inactive
    active = False
    r2 = ''
    iperso=["p2.png","p2h.png","p2g.png","p2d.png"]
    perso = pygame.image.load("p2.png").convert_alpha()
    position_perso = perso.get_rect()
    om=pygame.image.load("om1.png").convert_alpha()
    om.set_alpha(100)
    ob=pygame.image.load("ob.png").convert_alpha()
    ob.set_alpha(100)
    s2 = pygame.mixer.Sound("niv2.wav")
    s2.play()
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
    continuer = 1
    pygame.key.set_repeat(400, 30)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    perso = pygame.image.load(iperso[1]).convert_alpha()
                    position_perso = position_perso.move(0,-3)
                elif event.key == K_DOWN:
                    perso = pygame.image.load(iperso[0]).convert_alpha()
                    position_perso = position_perso.move(0,3)
                elif event.key == K_RIGHT:
                    perso = pygame.image.load(iperso[3]).convert_alpha()
                    position_perso = position_perso.move(3,0)
                elif event.key == K_LEFT:
                    perso = pygame.image.load(iperso[2]).convert_alpha()
                    position_perso = position_perso.move(-3,0)
            if event.type == MOUSEBUTTONDOWN:
                if input_box2.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(r2)
                    elif event.key == pygame.K_BACKSPACE:
                        r2 = r2[:-1]
                    else:
                        r2 += event.unicode
            if r2=='H+': #REVOIR CONDITIONS (avec return attention pas transition)
                fenetre.blit(om,(50,180))
                fenetre.blit(ob,(550,680))
                pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and 50<=event.pos[0]<=100 and 180<=event.pos[1]<=230:
                    print('ouim')
                    s2.stop()
                    n3m()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and 550<=event.pos[0]<=774 and 680<=event.pos[1]<=867:
                    print('ouib')
                    s2.stop()
                    n3b()

        fenetre.blit(fond, (0,0))
        fenetre.blit(text3, (450, 50))
        fenetre.blit(perso, position_perso)
        txt_surface = font.render(r2, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box2.w = width
        fenetre.blit(txt_surface, (input_box2.x+5, input_box2.y+5))
        pygame.draw.rect(fenetre, color, input_box2, 2)
        pygame.display.flip()


def n3m():
    pygame.display.set_caption("Jeu n3m")
    fond = pygame.image.load("f3m.png").convert()
    fenetre.blit(fond,(0,0))
    text4m = font.render("x et x² sont sur une barque, celle ci dérive et x tombe à l'eau. Qui reste-t-il?",1,(205,200,177))
    fenetre.blit(text4m, (450, 50))
    input_box3m = pygame.Rect(450, 100, 140,32)
    color_inactive = pygame.Color('cornsilk4')
    color_active = pygame.Color('cornsilk3')
    color=color_inactive
    active = False
    r3m = ''
    iperso=["p3m.png","p3mr.png"]
    perso = pygame.image.load("p3m.png").convert_alpha()
    position_perso = perso.get_rect()
    o3m=pygame.image.load("orbe feu.png").convert_alpha()
    o3m.set_alpha(100)
    s3m = pygame.mixer.Sound("niv3m.wav")
    s3m.play()
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
    continuer = 1
    pygame.key.set_repeat(400,30)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    perso = pygame.image.load(iperso[1]).convert_alpha()
                    position_perso = position_perso.move(0,-3)
                elif event.key == K_DOWN:
                    perso = pygame.image.load(iperso[0]).convert_alpha()
                    position_perso = position_perso.move(0,3)
                elif event.key == K_RIGHT:
                    perso = pygame.image.load(iperso[0]).convert_alpha()
                    position_perso = position_perso.move(3,0)
                elif event.key == K_LEFT:
                    perso = pygame.image.load(iperso[1]).convert_alpha()
                    position_perso = position_perso.move(-3,0)
            if event.type == MOUSEBUTTONDOWN:
                if input_box3m.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

            if event.type == KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(r3m)
                    elif event.key == pygame.K_BACKSPACE:
                        r3m = r3m[:-1]
                    else:
                        r3m += event.unicode
            if r3m=='2x': #REVOIR CONDITIONS (avec return attention pas transition)
                fenetre.blit(o3m,(700,20))
                pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and 700<=event.pos[0]<=878 and 20<=event.pos[1]<=150:
                    print('ouim')
                    s3m.stop()
                    n4m()

        fenetre.blit(fond, (0,0))
        fenetre.blit(text4m, (450, 50))
        fenetre.blit(perso, position_perso)
        txt_surface = font.render(r3m, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box3m.w = width
        fenetre.blit(txt_surface, (input_box3m.x+5, input_box3m.y+5))
        pygame.draw.rect(fenetre, color, input_box3m, 2)
        pygame.display.flip()

def n3b():
    pygame.display.set_caption("Jeu n3b")
    fond = pygame.image.load("f3b.png").convert()
    fenetre.blit(fond,(0,0))
    text4b = font.render("Pourquoi l'ours se dissout-il dans l'eau ?",1,(205,200,177))
    fenetre.blit(text4b, (450, 50))
    input_box3b = pygame.Rect(450, 100, 140,32)
    color_inactive = pygame.Color('cornsilk4')
    color_active = pygame.Color('cornsilk3')
    color=color_inactive
    active = False
    r3b = ''
    pygame.display.update()
    o3b=pygame.image.load("orbe glace.png").convert_alpha()
    o3b.set_alpha(100)
    perso = pygame.image.load("p3b.png").convert_alpha()
    position_perso = perso.get_rect()
    s3b = pygame.mixer.Sound("niv3b.wav")
    s3b.play()
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
    continuer = 1
    pygame.key.set_repeat(400, 30)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    position_perso = position_perso.move(0,-3)
                elif event.key == K_DOWN:
                    position_perso = position_perso.move(0,3)
                elif event.key == K_RIGHT:
                    position_perso = position_perso.move(3,0)
                elif event.key == K_LEFT:
                    position_perso = position_perso.move(-3,0)
            if event.type == MOUSEBUTTONDOWN:
                if input_box3b.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(r3b)
                    elif event.key == pygame.K_BACKSPACE:
                        r3b = r3b[:-1]
                    else:
                        r3b += event.unicode
            if r3b=='polaire': #REVOIR CONDITIONS (avec return attention pas transition)
                fenetre.blit(o3b,(700,600))
                pygame.display.flip()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 700<=event.pos[0]<=850 and 600<=event.pos[1]<=700:
                print('ouib')
                s3b.stop()
                n4b()

        fenetre.blit(fond, (0,0))
        fenetre.blit(text4b, (450, 50))
        fenetre.blit(perso, position_perso)
        txt_surface = font.render(r3b, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box3b.w = width
        fenetre.blit(txt_surface, (input_box3b.x+5, input_box3b.y+5))
        pygame.draw.rect(fenetre, color, input_box3b, 2)
        pygame.display.flip()

def n4m():
    pygame.display.set_caption("Jeu n4m")
    fond = pygame.image.load("f4m.png").convert()
    fenetre.blit(fond,(0,0))
    text5m = font.render("Que dit un canard subatomique ?",1,(205,200,177))
    fenetre.blit(text5m, (450, 50))
    input_box4m = pygame.Rect(450, 100, 140,32)
    color_inactive = pygame.Color('cornsilk4')
    color_active = pygame.Color('cornsilk3')
    color=color_inactive
    active = False
    r4m = ''
    pygame.display.update()
    o4m=pygame.image.load("orbe desert.png").convert_alpha()
    o4m.set_alpha(100)
    perso = pygame.image.load("p4m.png").convert_alpha()
    position_perso = perso.get_rect()
    s3b = pygame.mixer.Sound("niv3b.wav")
    s3b.play()
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
    continuer = 1
    pygame.key.set_repeat(400, 30)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    position_perso = position_perso.move(0,-3)
                elif event.key == K_DOWN:
                    position_perso = position_perso.move(0,3)
                elif event.key == K_RIGHT:
                    position_perso = position_perso.move(3,0)
                elif event.key == K_LEFT:
                    position_perso = position_perso.move(-3,0)
            if event.type == MOUSEBUTTONDOWN:
                if input_box4m.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(r4m)
                    elif event.key == pygame.K_BACKSPACE:
                        r4m = r4m[:-1]
                    else:
                        r4m += event.unicode
            if r4m=='quark': #REVOIR CONDITIONS (avec return attention pas transition)
                fenetre.blit(o4m,(600,700))
                pygame.display.flip()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 600<=event.pos[0]<=806 and 700<=event.pos[1]<=923:
                print('ouib')
                s3b.stop()
                n5m()

        fenetre.blit(fond, (0,0))
        fenetre.blit(text5m, (450, 50))
        fenetre.blit(perso, position_perso)
        txt_surface = font.render(r4m, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box4m.w = width
        fenetre.blit(txt_surface, (input_box4m.x+5, input_box4m.y+5))
        pygame.draw.rect(fenetre, color, input_box4m, 2)
        pygame.display.flip()

def n4b():
    pygame.display.set_caption("Jeu n4b")
    fond = pygame.image.load("f4b.png").convert()
    fenetre.blit(fond,(0,0))
    text5b = font.render("Quel est le nombre le plus laid?",1,(205,200,177))
    fenetre.blit(text5b, (450, 50))
    input_box4b = pygame.Rect(450, 100, 140,32)
    color_inactive = pygame.Color('cornsilk4')
    color_active = pygame.Color('cornsilk3')
    color=color_inactive
    active = False
    r4b = ''
    pygame.display.update()
    o4b=pygame.image.load("orbe rose.png").convert_alpha()
    o4b.set_alpha(100)
    perso = pygame.image.load("p4b.png").convert_alpha()
    position_perso = perso.get_rect()
    s3b = pygame.mixer.Sound("niv3b.wav")
    s3b.play()
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
    continuer = 1
    pygame.key.set_repeat(400, 30)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    position_perso = position_perso.move(0,-3)
                elif event.key == K_DOWN:
                    position_perso = position_perso.move(0,3)
                elif event.key == K_RIGHT:
                    position_perso = position_perso.move(3,0)
                elif event.key == K_LEFT:
                    position_perso = position_perso.move(-3,0)
            if event.type == MOUSEBUTTONDOWN:
                if input_box4b.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(r4b)
                    elif event.key == pygame.K_BACKSPACE:
                        r4b = r4b[:-1]
                    else:
                        r4b += event.unicode
            if r4b=='-1': #REVOIR CONDITIONS (avec return attention pas transition)
                fenetre.blit(o4b,(600,700))
                pygame.display.flip()
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and 600<=event.pos[0]<=806 and 700<=event.pos[1]<=923:
                print('ouib')
                s3b.stop()
                n5b()

        fenetre.blit(fond, (0,0))
        fenetre.blit(text5b, (450, 50))
        fenetre.blit(perso, position_perso)
        txt_surface = font.render(r4b, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box4b.w = width
        fenetre.blit(txt_surface, (input_box4b.x+5, input_box4b.y+5))
        pygame.draw.rect(fenetre, color, input_box4b, 2)
        pygame.display.flip()


def n5m():
    pygame.display.set_caption("Jeu n5m")
    fond = pygame.image.load("f5m.png").convert()
    fenetre.blit(fond,(0,0))
    perso = pygame.image.load("p5m.png").convert_alpha()
    position_perso = perso.get_rect()
    s3b = pygame.mixer.Sound("niv3b.wav")
    s3b.play()
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
    continuer = 1
    pygame.key.set_repeat(400, 30)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    position_perso = position_perso.move(0,-3)
                elif event.key == K_DOWN:
                    position_perso = position_perso.move(0,3)
                elif event.key == K_RIGHT:
                    position_perso = position_perso.move(3,0)
                elif event.key == K_LEFT:
                    position_perso = position_perso.move(-3,0)

        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, position_perso)
        pygame.display.flip()

def n5b():
    pygame.display.set_caption("Jeu n5b")
    fond = pygame.image.load("f5b.png").convert()
    fenetre.blit(fond,(0,0))
    perso = pygame.image.load("p5b.png").convert_alpha()
    position_perso = perso.get_rect()
    s3b = pygame.mixer.Sound("niv3b.wav")
    s3b.play()
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
    continuer = 1
    pygame.key.set_repeat(400, 30)
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    position_perso = position_perso.move(0,-3)
                elif event.key == K_DOWN:
                    position_perso = position_perso.move(0,3)
                elif event.key == K_RIGHT:
                    position_perso = position_perso.move(3,0)
                elif event.key == K_LEFT:
                    position_perso = position_perso.move(-3,0)

        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, position_perso)
        pygame.display.flip()


fenetre = pygame.display.set_mode((1024,1024))
pygame.display.set_caption("Jeu")
#Chargement et collage du fond
fond = pygame.image.load("noir.png").convert()
fenetre.blit(fond,(0,0))
s0 = pygame.mixer.Sound("g.wav")
font=pygame.font.Font(None, 24)
text0 = font.render("Bienvenue. Vos choix influeront sur votre aventure. Déplacez votre personnage, choisissez une orbe...",1,(255,255,255))
fenetre.blit(text0, (100, 100))
text1 = font.render("Cliquez pour continuer.",2,(255,255,255))
fenetre.blit(text1, (300, 120))
#Rafraîchissement de l'écran
pygame.display.flip()
#BOUCLE INFINIE
continuer = 1
pygame.key.set_repeat(400, 30)
while continuer:
    for event in pygame.event.get(): #Attente des événements
        if event.type == QUIT:
            continuer = 0
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and 0<=event.pos[0]<=1024 and 0<=event.pos[1]<=1024:
            print('o')
            s0.play()
            n1()

#Re-collage
fenetre.blit(fond, (0,0))
fenetre.blit(text0, (100, 100))
fenetre.blit(text1, (300, 120))
#Rafraichissement
pygame.display.flip()




#canard subatomique quark quark
#diffifulxcté: blit refresh mal clignote set alpha 100, mettre fond
