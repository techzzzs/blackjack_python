import pygame
import sys
import math
import random
from draw import draw_img,draw_img_c,draw_text
from randomizer import shuffle_add, count_score

open("User_data.txt", "a").close()
with open("User_data.txt") as file:
    balance=int(file.read())
    print(file.read())

bet=0
money_delt=False
female_counter=0


instruc=["","Make Your Bet (Confirm with hit)","Dealing cards","Hit or Stand?","Dealers Turn","Counting score","You Lost, haha","You Won","It's a draw"]
pygame.init()
pygame.mixer.init()

########### MUSIC##############
sounds = {}
def play(path):
    if path not in sounds:
        sounds[path] = pygame.mixer.Sound("Sounds/" + path)
    sounds[path].play()


pygame.mixer.music.load("Sounds/background_music.mp3")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.5)

hover_played = False
is_hovering=False

num_buttons = 10  # or however many buttons you have
buttons = [{"hovering": False, "hover_played": False} for _ in range(num_buttons)]
hover_sound = "woosh.mp3"  
##############################################

WIDTH,HEIGHT=1920,1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BlackJack")

left_click_active=False
first_hidden=False
deck=[]
ddeck=[]
timer=0






def draw_deck(x,y,deck,size):
    for i in range(0,len(deck)):
        draw_img(screen,("Cards/"+deck[i]+".png"),x+i*200,y,size)





clock = pygame.time.Clock()

#main loop
mouse_pos = pygame.mouse.get_pos()
state=0
running =True
while running:





    for btn in buttons:
        
        if btn["hovering"] and not btn["hover_played"]:
            play(hover_sound)       # play the sound once
            btn["hover_played"] = True

        if not btn["hovering"]:
            btn["hover_played"] = False  # reset so it can play again




    if timer>=10000:
        timer=0
    dt = clock.tick(120)
    fps = int(clock.get_fps())

    mouse_pos = pygame.mouse.get_pos()
    left_button=False

    player_score=count_score(deck)
    dealer_score=count_score(ddeck)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("demofile.txt", "w") as f:
                money=balance+bet
                f.write("Woops! I have deleted the content!")
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                with open("User_data.txt", "w") as f:
                    money=balance+bet
                    f.write(str(money))
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
            play("button.mp3")

    ##############################
    # BETTING SCREEN
    ##############################
    if state >=1:

        draw_img(screen,"Images/background.jpg",0,0,0.6)
        
        draw_img_c(screen,"Images/wide_board.png",WIDTH,HEIGHT,1)
        draw_img(screen,"Images/wide_board.png",1420,410,0.7)
        draw_deck(500,690,deck,1)
        draw_deck(500,140,ddeck,1)
        #dealer
        if draw_img(screen,"Images/dealer.png",220,130,1,True).collidepoint(mouse_pos) and left_button:
            play("haha" + str(random.choice(range(1, 17))) + ".mp3")
            female_counter+=1
        draw_img(screen,"Images/dealer.png",220,130,1)

        if female_counter>=20:
            balance=1000
            female_counter=0

        if first_hidden:
            draw_img(screen,"Cards/back2.png",500,140,1)


        draw_text(screen,fps,200,110,20,20,14, 64, 10,12)
        draw_text(screen,"Current bet:",855,542,200,60,74, 37, 16,24)
        draw_text(screen,str(bet)+"$",855,500,200,60,240,240,240,64)
        draw_text(screen,str(balance)+"$",1420,420,280,70,250,250,250,54)
        draw_text(screen,instruc[state],855,584,200,60,204, 176, 114,18)

        rect_allin=pygame.Rect(1420, 500, 280, 40)
        rect_allout=pygame.Rect(1420, 550, 135, 40)
        rect_half=pygame.Rect(1565, 550, 135, 40)
        rect_plus100=pygame.Rect(1420, 600, 135, 40)
        rect_minus100=pygame.Rect(1565, 600, 135, 40)
        button_rgb=(125, 81, 11)
        howerbutton_rgb=(115, 71, 11)
        txt_r, txt_g, txt_b = 59, 42, 16

        draw_img(screen,"Images/wood_board_score.png",1420,120,1)
        draw_img(screen,"Images/wood_board_score.png",1420,680,1)

        draw_text(screen,count_score(ddeck,first_hidden),1450,160,200,200,255, 228, 194,54)
        draw_text(screen,count_score(deck),1450,720,200,200,255, 228, 194,54)

        # pause button
        if draw_img(screen,"Images/pause.png",210,400,0.5,True).collidepoint(mouse_pos):
            draw_img(screen,"Images/pause.png",207,397,0.6)
            if left_button:
                play("button.mp3")
                pygame.mixer.music.pause()
        else:
            draw_img(screen,"Images/pause.png",210,400,0.5)
        # play button
        if draw_img(screen,"Images/continue.png",250,400,0.5,True).collidepoint(mouse_pos):
            draw_img(screen,"Images/continue.png",247,397,0.6)
            if left_button:
                play("button.mp3")
                pygame.mixer.music.unpause()
        else:
            draw_img(screen,"Images/continue.png",250,400,0.5)


        #all in------------------#
        if rect_allin.collidepoint(mouse_pos):
            pygame.draw.rect(screen,howerbutton_rgb,rect_allin,0,10)
            buttons[0]["hovering"] = True
            if left_button and state==1:
                play("coin_long.mp3")
                bet +=balance
                balance=0
        else:
            pygame.draw.rect(screen,button_rgb,rect_allin,0,10)
            buttons[0]["hovering"] = False
        draw_text(screen,"All In",1420, 500, 280, 40,txt_r,txt_g,txt_b,24)
        #all out------------------#
        if rect_allout.collidepoint(mouse_pos):
            pygame.draw.rect(screen,howerbutton_rgb,rect_allout,0,10)
            buttons[1]["hovering"] = True
            if left_button and state==1:
                play("coin_long.mp3")
                balance+=bet
                bet=0
        else:
            pygame.draw.rect(screen,button_rgb,rect_allout,0,10)
            buttons[1]["hovering"] = False
        draw_text(screen,"All Out",1420, 550, 135, 40,txt_r,txt_g,txt_b,24)
        # half------------------#
        if rect_half.collidepoint(mouse_pos):
            pygame.draw.rect(screen,howerbutton_rgb,rect_half,0,10)
            buttons[2]["hovering"] = True
            if left_button and state==1:
                play("coin_long.mp3")
                delta=math.ceil(balance/2)
                bet+=delta
                balance-=delta
        else:
            pygame.draw.rect(screen,button_rgb,rect_half,0,10)
            buttons[2]["hovering"] = False
        draw_text(screen,"Half",1565, 550, 135, 40,txt_r,txt_g,txt_b,24)
        # plus 100------------------#
        if rect_plus100.collidepoint(mouse_pos):
            pygame.draw.rect(screen,howerbutton_rgb,rect_plus100,0,10)
            buttons[3]["hovering"] = True
            if left_button and balance>=100 and state==1:
                play("coin_long.mp3")
                bet+=100
                balance-=100
        else:
            pygame.draw.rect(screen,button_rgb,rect_plus100,0,10)
            buttons[3]["hovering"] = False
        draw_text(screen,"+100",1420, 600, 135, 40,txt_r,txt_g,txt_b,24)
        # minus 100------------------#
        if rect_minus100.collidepoint(mouse_pos):
            pygame.draw.rect(screen,howerbutton_rgb,rect_minus100,0,10)
            buttons[4]["hovering"] = True
            if left_button and bet>=100 and state==1:
                play("coin_long.mp3")
                bet-=100
                balance+=100
        else:
            pygame.draw.rect(screen,button_rgb,rect_minus100,0,10)
            buttons[4]["hovering"] = False
        draw_text(screen,"-100",1565, 600, 135, 40,txt_r,txt_g,txt_b,24)

        # hit button
        if draw_img(screen,"Images/wood_button_hit.png",230,690,1,True).collidepoint(mouse_pos):
            draw_img(screen,"Images/wood_button_hit_d.png",230,690,1)
            buttons[5]["hovering"] = True
            if left_button:
                play("button.mp3")
                if state==1:
                    
                    state=2 #CHANGE STATE ################
                    first_dealt=False
                    timer=0

                if left_button and state==3:
                    play("card_take.mp3")
                    shuffle_add(deck)
                    
        else:
            draw_img(screen,"Images/wood_button_hit.png",230,690,1)
            buttons[5]["hovering"] = False



        if state==2:
            timer+=1
            if not first_dealt:
                if timer==20:
                    print("20 sec")
                    shuffle_add(deck)
                    play("card_take.mp3")
                if timer==40 and len(ddeck)<3:
                    first_hidden=True
                    shuffle_add(ddeck)
                    play("card_take.mp3")
                if timer==60:
                    shuffle_add(deck)
                    play("card_take.mp3")
                if timer==80 and len(ddeck)<3:
                    shuffle_add(ddeck)
                    play("card_take.mp3")
                    first_dealt=True
                    state=3

        


        # stand button
        if draw_img(screen,"Images/wood_button_stand.png",230,830,1,True).collidepoint(mouse_pos):
            draw_img(screen,"Images/wood_button_stand_d.png",230,830,1)
            buttons[6]["hovering"] = True
            if state==3 and left_button:
                play("button.mp3")
                state=4 #CHANGE STATE ##################
                first_hidden=False
                timer=0
        else:
            draw_img(screen,"Images/wood_button_stand.png",230,830,1)
            buttons[6]["hovering"] = False


        if player_score>=21 and state>=4:
            state=5 #count score
        ##############################
        # DEALERS TURN
        ##############################
        if state==4:
            timer+=1
            if dealer_score<=17:
                if timer >=200:
                    shuffle_add(ddeck)
                    play("card_take.mp3")
                    timer=0
            if dealer_score>17:
                state=5


        ##############################
        # SCORE CHECK
        ##############################
        if state==5:
            money_delt=False
            if player_score >21:
                state=6 # player lost
            if player_score <21:
                if dealer_score==player_score:
                    state=8 # draw
                if dealer_score>player_score and dealer_score<=21:
                    state=6 # player lost
                else:
                    state=7 # player won
            if player_score ==21:
                if dealer_score==21:
                    state=8 # draw
                else:
                    state=7 # player won

        ##############################
        # MONEY DEALING
        ##############################     
        if not money_delt and state>5:
            if state==6:
                bet=0
                # play("coin_light.mp3")
                money_delt=True
            if state==7 and not money_delt:
                balance+=bet*2
                bet=0
                play("coin_light.mp3")
                money_delt=True
            if state==8:
                balance+=bet
                bet=0
                play("coin_light.mp3")
                money_delt=True
        ######## RESET #########
        if state>5:
            if draw_img(screen,"Images/play_again.png",760,770,1,True).collidepoint(mouse_pos):
                draw_img(screen,"Images/play_again.png",740,766,1.1)
                if left_button:
                    play("button.mp3")
                    state=1
                    deck=[]
                    ddeck=[]
                    money_delt=False
                    first_hidden=False

            else:
                draw_img(screen,"Images/play_again.png",760,770,1)






    pygame.display.flip()

pygame.quit()
sys.exit()
