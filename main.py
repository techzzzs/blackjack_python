import pygame
import sys
from draw import draw_img,draw_img_c
from randomizer import shuffle_add, count_score



pygame.init()


WIDTH,HEIGHT=1920,1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")

left_click_active=False
deck=[]
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
state=0
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
    # START SCREEN
    ##############################
    if state == 1:
        draw_img(screen,"Images/background.jpg",0,0,0.6)
        draw_deck(500,690,deck,1)

    pygame.display.flip()

pygame.quit()
sys.exit()
