import pygame
import sys
import math
from draw import draw_img,draw_img_c,draw_text
from randomizer import shuffle_add, count_score



pygame.init()


WIDTH,HEIGHT=1920,1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")

left_click_active=False
deck=[]

balance=1000
bet=0

shuffle_add(deck)
shuffle_add(deck)
print(deck)
def draw_deck(x,y,deck,size):
    print("yes")
    for i in range(0,len(deck)):
        print("Cards/"+deck[i]+".png")
        draw_img(screen,("Cards/"+deck[i]+".png"),x+i*200,y,size)





#main loop
mouse_pos = pygame.mouse.get_pos()
state=1
running =True
while running:
    mouse_pos = pygame.mouse.get_pos()
    left_button=False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running=False

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not left_click_active:
                left_button=True
                left_click_active= True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button ==1: 
                left_click_active = False
                

    ##############################
    # TITL SCREEN
    ##############################
    if state == 0:
        play_rect=draw_img(screen, "Images/play.png", 860, 750, 1,True)
        draw_img(screen,"Images/background.jpg",0,0,0.7)
        draw_img_c(screen,"Images/blackjack_main.png",WIDTH,HEIGHT,1)
        if play_rect.collidepoint(mouse_pos):
            draw_img(screen,"Images/play.png",870,755,0.9)
        else:
            draw_img(screen,"Images/play.png",860,750,1)
        # change state
        if left_button and play_rect.collidepoint(mouse_pos):
            state=1

    ##############################
    # BETTING SCREEN
    ##############################
    if state == 1:
        draw_img(screen,"Images/background.jpg",0,0,0.6)
        draw_img_c(screen,"Images/wide_board.png",WIDTH,HEIGHT,1)
        draw_deck(500,690,deck,1)
        draw_deck(500,140,deck,1)
        draw_img(screen,"Images/wide_board.png",1420,410,0.7)

        draw_text(screen,"Current bet:",855,542,200,60,74, 37, 16,24)
        draw_text(screen,str(bet)+"$",855,500,200,60,240,240,240,64)
        draw_text(screen,str(balance)+"$",1420,420,280,70,250,250,250,54)
        draw_text(screen,"Make Your bet",855,584,200,60,204, 176, 114,18)

        rect_allin=pygame.Rect(1420, 500, 280, 40)
        rect_allout=pygame.Rect(1420, 550, 135, 40)
        rect_half=pygame.Rect(1565, 550, 135, 40)
        rect_plus100=pygame.Rect(1420, 600, 135, 40)
        rect_minus100=pygame.Rect(1565, 600, 135, 40)
        button_rgb=(125, 81, 11)
        howerbutton_rgb=(115, 71, 11)
        txt_r, txt_g, txt_b = 59, 42, 16
        #all in------------------#
        if rect_allin.collidepoint(mouse_pos):
            pygame.draw.rect(screen,howerbutton_rgb,rect_allin,0,10)
            if left_button:
                bet +=balance
                balance=0
        else:
            pygame.draw.rect(screen,button_rgb,rect_allin,0,10)
        draw_text(screen,"All In",1420, 500, 280, 40,txt_r,txt_g,txt_b,24)
        #all out------------------#
        if rect_allout.collidepoint(mouse_pos):
            pygame.draw.rect(screen,howerbutton_rgb,rect_allout,0,10)
            if left_button:
                balance+=bet
                bet=0
        else:
            pygame.draw.rect(screen,button_rgb,rect_allout,0,10)
        draw_text(screen,"All Out",1420, 550, 135, 40,txt_r,txt_g,txt_b,24)
        # half------------------#
        if rect_half.collidepoint(mouse_pos):
            pygame.draw.rect(screen,howerbutton_rgb,rect_half,0,10)
            if left_button:
                delta=math.ceil(balance/2)
                bet+=delta
                balance-=delta
        else:
            pygame.draw.rect(screen,button_rgb,rect_half,0,10)
        draw_text(screen,"Half",1565, 550, 135, 40,txt_r,txt_g,txt_b,24)
        # plus 100------------------#
        if rect_plus100.collidepoint(mouse_pos):
            pygame.draw.rect(screen,howerbutton_rgb,rect_plus100,0,10)
            if left_button and balance>=100:
                bet+=100
                balance-=100
        else:
            pygame.draw.rect(screen,button_rgb,rect_plus100,0,10)
        draw_text(screen,"+100",1420, 600, 135, 40,txt_r,txt_g,txt_b,24)
        # minus 100------------------#
        if rect_minus100.collidepoint(mouse_pos):
            pygame.draw.rect(screen,howerbutton_rgb,rect_minus100,0,10)
            if left_button and bet>=100:
                bet-=100
                balance+=100
        else:
            pygame.draw.rect(screen,button_rgb,rect_minus100,0,10)
        draw_text(screen,"-100",1565, 600, 135, 40,txt_r,txt_g,txt_b,24)

        # hit button
        if draw_img(screen,"Images/wood_button_hit.png",230,690,1,True).collidepoint(mouse_pos):
            draw_img(screen,"Images/wood_button_hit_d.png",230,690,1)
        else:
            draw_img(screen,"Images/wood_button_hit.png",230,690,1)
        # stand button
        if draw_img(screen,"Images/wood_button_stand.png",230,830,1,True).collidepoint(mouse_pos):
            draw_img(screen,"Images/wood_button_stand_d.png",230,830,1)
        else:
            draw_img(screen,"Images/wood_button_stand.png",230,830,1)



    pygame.display.flip()

pygame.quit()
sys.exit()
