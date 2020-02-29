from pygame import * #imports important modules I use
from random import *
import os
init() #initiates pygame

size = width, height = 1000, 600 #Sets screen size
screen = display.set_mode(size)

BLACK = (0,0,0)
RED = (255,0,0)    #preset colours I use
GREEN = (0,255,0)
WHITE = (255,255,255)

life = 3 #initial amount of lives

MAIN = 0 #starting main value

enemylistx = [315.5, 381.5, 447.5, 513.5, 579.5, 645.5] #all possible x values enemies can have

score = 0
gold = 0 #empty variables to change later
orriggold = 0

enemyx = choice(enemylistx)
enemyx2 = choice(enemylistx) #randomizes the x coordinate of enemies
enemyx3 = choice(enemylistx)
enemyx4 = choice(enemylistx)

enemyy = randint(-500,-200)
enemyy2 = randint(-500,-200) #randomizes the y coordinate of enemies
enemyy3 = randint(-500,-200)
enemyy4 = randint(-500,-200)

addlifex = choice(enemylistx) #randomizes the x and y coordinate of a drop
addlifey  = randint(-100000,-5000)

coinx = choice(enemylistx) #randomizes the x and y coordinate of a drop
coiny = randint(-5000,-1000)

rockx = randint(800,900) #randomizes the x and y coordinate of terrain
rocky = randint(-1000,0)

alienx = randint(0,100) ##randomizes the x and y coordinate of a little alien on the side of the road
alieny = randint(-1000,0)

signx = randint(700,800) #randomizes the x and y coordinate of a road sign
signy = randint(-10000,0)

enemy_speed = 10 #speed of the enemy

clock = time.Clock() #to cap fps

font = font.SysFont("Calibri", 20) #font used for text
 
running  = True #while true, the game runs

carx = 516 #initial starting position for player
cary = 500

cary_change = 0
levelspeed = 0 #empty vars to be changed later

x = 0  #empty vars to be changed later
y = 0

mx = 0  #empty vars to be changed later
my = 0
button = 0

goldhit = False  #bools to manipulate drops
lifehit = False

onelife = False
onegold = False

skin1 = image.load('image/police.jpg').convert()
skin1.set_colorkey(WHITE)
skin2 = image.load('image/car6.png').convert()
skin2.set_colorkey(WHITE) #images
skin3 = image.load('image/car9.png').convert()
skin3.set_colorkey(WHITE) #images
original = image.load('image/car1.png').convert()
original.set_colorkey(WHITE)

playerImage = image.load('image/car1.png').convert()
playerImage.set_colorkey(WHITE)
car2 = image.load('image/truck.png').convert()
car2.set_colorkey(WHITE) #images
car3 = image.load('image/car3.png').convert()
car3.set_colorkey(WHITE)
car4 = image.load('image/car4.png').convert()
car4.set_colorkey(WHITE)
car5 = image.load('image/car5.png').convert()
car5.set_colorkey(WHITE)
shoulder = image.load('image/dirt.png')
road = image.load('image/Road.png')
rock = image.load('image/rock.png').convert()
rock.set_colorkey(WHITE) #images
alien = image.load('image/alien.png').convert()
alien.set_colorkey(WHITE)
startscreen = image.load('image/start screen.png')
coin = image.load('image/coin.png').convert()
coin.set_colorkey(WHITE)
addlife = image.load('image/life.png').convert()
addlife.set_colorkey(WHITE) #images
sign = image.load('image/sign.png').convert()
sign.set_colorkey(WHITE)
keys = image.load('image/keys1.png').convert()
keys.set_colorkey(WHITE)
keys2 = image.load('image/keys2.png').convert()
keys2.set_colorkey(WHITE) #images
caught = image.load('image/mafiacaught.jpg')
mafia = image.load('image/mafiadude.jpg')
phone = image.load('image/phone.png').convert()
phone.set_colorkey(WHITE)

def drawText(text, font, screen, x, y): #def command to make text easier
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)
    
def playerCar(carx,cary): #blits player car
    screen.blit(playerImage,(carx,cary))
    
def enemy(enemyx,enemyy): #blits all drop and enemy cars
    screen.blit(car3,(enemyx,enemyy))
    screen.blit(car4,(enemyx2,enemyy2))
    screen.blit(car5,(enemyx3,enemyy3))
    screen.blit(car2,(enemyx4,enemyy4))
    if lifehit == False:
        screen.blit(addlife,(addlifex,addlifey))
    if goldhit == False:
        screen.blit(coin,(coinx,coiny))
      
def terrain(): #blits all terrain
    screen.blit(rock,(rockx,rocky))
    screen.blit(alien,(alienx,alieny))  
    screen.blit(sign,(signx,signy))
    
def StartMenu(MAIN,button): #startmenu
    if MAIN == 0:
        if MAIN >= 0:
            mixer.music.load('music/Music.mp3') #plays music throughout the game
            mixer.music.play(-1)          
        screen.blit(startscreen,(0,0))
        listofrects = [Rect(200,200,600,100),Rect(200,325,600,100),Rect(200,450,600,100),Rect(20,20,120,50)] #list of button rects
        drawText('Play',font,screen,500,230)
        drawText('FEATURE NOT AVAILABLE',font,screen,500,370)
        drawText('Exit',font,screen,500,470)
        drawText('Trash Attack',font,screen,400,20)
        draw.rect(screen,BLACK,listofrects[0],5)  #draws buttons
        draw.rect(screen,BLACK,listofrects[1],5)
        draw.rect(screen,BLACK,listofrects[2],5)
        #draw.rect(screen,BLACK,listofrects[3],5)
        if listofrects[0].collidepoint(mx,my):
            draw.rect(screen,WHITE,listofrects[0],5)  #checks if they are clicked and performs designated action
            if button == 1:
                MAIN = 1
        if listofrects[1].collidepoint(mx,my):
            draw.rect(screen,WHITE,listofrects[1],5) #checks if they are clicked and performs designated action
            if button == 1:
                MAIN = 4
                button = 0
        if listofrects[2].collidepoint(mx,my):
            draw.rect(screen,WHITE,listofrects[2],5) #checks if they are clicked and performs designated action
            if button == 1:
                MAIN = -1
        #if listofrects[3].collidepoint(mx,my):
            #draw.rect(screen,WHITE,listofrects[3],5)
            #if button == 1:
                #MAIN = 2  
                #button = 0
    return MAIN,button

#def Shop(MAIN):
    #if MAIN == 2:
        #screen.blit(startscreen,(0,0))
        #drawText('Shop',font,screen,400,20)
        #rects = [Rect(100,100,350,150),Rect(550,100,350,150),Rect(100,300,350,150),Rect(550,300,350,150),Rect(20,20,120,50)]
        #draw.rect(screen,BLACK,rects[0],5)
        #draw.rect(screen,BLACK,rects[1],5)
        #draw.rect(screen,BLACK,rects[2],5)  
        #draw.rect(screen,BLACK,rects[3],5) 
        #draw.rect(screen,BLACK,rects[4],5)
    #return MAIN

def story(MAIN,button): #writes the story
    if MAIN == 4:
        draw.rect(screen,BLACK,(0,0,1000,600))
        drawText('It is the year 2100. Humans have colonized Mars. However,',font,screen,20,70)
        drawText('They have forgotten how to recycle their phones the proper',font,screen,20,100)
        drawText('way. You (the enlightened one), started an underground',font,screen,20,130)
        drawText('mafia to recycle the phones but now the police has put',font,screen,20,160)
        drawText('a bounty on your head.',font,screen,20,190)
        drawText('Now you are running away from the cops in your',font,screen,550,320)
        drawText('gravity-defying car filled with cellphones. Whether',font,screen,550,350)
        drawText('you crash into the evening traffic and get caught',font,screen,550,380) 
        drawText('or you thread the needle and make your stealthy',font,screen,550,410)  
        drawText('escape, that\'s up to you to decide. Good Luck',font,screen,550,440)  
        drawText('You Legendary Capo!',font,screen,550,470) 
        screen.blit(mafia,(150,270))
        screen.blit(phone,(620,80))
        draw.rect(screen,WHITE,Rect(780,540,200,40),2)
        drawText('Main Menu',font,screen,835,553) 
        if Rect(780,540,200,40).collidepoint(mx,my):
            draw.rect(screen,WHITE,Rect(780,540,200,40),5)
            if button == 1:
                MAIN = 0 #button to go back 
                button = 0
    return MAIN,button

def instructions(): #displayed at the start of each game till the score of 300
    if score < 300:  
        screen.blit(keys,(800,10,100,68))
        drawText('Moves The Car Horizontally',font,screen,750,85)
        screen.blit(keys2,(800,120,100,68))
        drawText('Moves The Car Vertically',font,screen,753,195)
        screen.blit(addlife,(832.5,230,35,35))
        drawText('Gives Random Extra Lives',font,screen,750,272) #blits instructions
        screen.blit(coin,(832.5,298,35,35))
        drawText('Collect Just For Fun',font,screen,750,340)
        drawText('Flee From The Cops For As Long As',font,screen,710,400)
        drawText('You Can!',font,screen,820,420)
        drawText('Good Luck!',font,screen,810,440)
    
def Game(MAIN,button,carx,cary,cary_change,x,y,life,enemyx,enemyy,enemyx2,enemyx3,enemyx4,score,levelspeed,gold,orriggold,enemyy2,enemyy3,enemyy4,rockx,rocky,alienx,alieny,coinx,coiny,addlifex,addlifey,signx,signy,goldhit,lifehit,onegold,onelife): #MAIN GAME
    if MAIN == 1:
        button = 0
        if not os.path.exists("data/save.dat"): #adds score to a database
            f=open("data/save.dat",'w')
            f.write(str(zero))
            f.close()   
        v=open("data/save.dat",'r') 
        topScore = int(v.readline())
        v.close()    
        
        #if not os.path.exists("data/gold.dat"):
            #g = open("data/gold.dat",'w')
            #g.write(str(zero))
            #g.close()
        #b = open("data/gold.dat",'r')
        #gold = int(b.readline())
        #origgold = gold
        
        levelspeed += 0.01 #increases 
        score += 1
        carx_change = 0        
        draw.rect(screen,BLACK,(0,0,1000,600))
        
        for i in range(-450, 451, 150):
            screen.blit(shoulder,Rect(0,y+i,150,150))
            screen.blit(shoulder,Rect(150,y+i,150,150)) #DRAWS THE BACKGROUND AND ANIMATES IT
            screen.blit(road,Rect(300,y+i,400,275))
            screen.blit(shoulder,Rect(700,y+i,150,150))
            screen.blit(shoulder,Rect(850,y+i,150,150))
        y += 8 + levelspeed
        if y >= 300: #resets the background
            y = 0  
        
        terrain()
        enemy(enemyx,enemyy) #spawns cars
        playerCar(carx,cary)
        
        enemyRect = Rect(enemyx,enemyy,35,79)
        enemyRect2 = Rect(enemyx2,enemyy2,35,79)
        enemyRect3 = Rect(enemyx3,enemyy3,35,79)
        enemyRect4 = Rect(enemyx4,enemyy4,35,79)
        playerRect = Rect(carx,cary,35,79) #rects that define the cars
        coinRect = Rect(coinx,coiny,35,35)
        addlifeRect = Rect(addlifex,addlifey,35,35)
            
        cary += cary_change
        if cary >= 520:
            cary = 520 #does not allow user to go off screen
        elif cary <= 0:
            cary = 0
            
        enemyy += enemy_speed + levelspeed
        enemyy2 += enemy_speed + levelspeed
        enemyy3 += enemy_speed + levelspeed
        enemyy4 += enemy_speed + levelspeed #increases the speed of everything with the speed of the background
        rocky += enemy_speed + levelspeed
        alieny += enemy_speed + levelspeed
        coiny += enemy_speed + levelspeed
        addlifey += enemy_speed + levelspeed
        signy += enemy_speed + levelspeed
        
        
        if carx > 700 or carx < 300:
            if life <= 1:
                MAIN = 3    
                score = 0 #if the player goes off the road, a life is lost
                button = 0
                orriggold = 0
                life = 4
                y = 0
            life -= 1
            carx = 516
            enemyy = randint(-500,-200)
            enemyy2 = randint(-500,-200)
            enemyy3 = randint(-500,-200)  
            enemyy4 = randint(-500,-200) 
            if score >= 1000:
                levelspeed -= 5
            time.wait(1000)
            if score > topScore:
                g=open("data/save.dat",'w')
                g.write(str(score))
                g.close()            
            
        if playerRect.colliderect(enemyRect) == True or playerRect.colliderect(enemyRect2) == True or playerRect.colliderect(enemyRect3) == True or playerRect.colliderect(enemyRect4) == True:        
            if life <= 1:
                MAIN = 3  
                button = 0
                score = 0 #if the player collides with anything, a life is lost
                life = 4
                #orriggold = 0
                y = 0
            life -= 1
            carx = 516
            enemyy = randint(-500,-200)
            enemyy2 = randint(-500,-200)
            enemyy3 = randint(-500,-200)  
            enemyy4 = randint(-500,-200) 
            if score >= 1000:
                levelspeed -= 5
            time.wait(1000)
            if score > topScore:
                g=open("data/save.dat",'w')
                g.write(str(score))
                g.close()
                
        if playerRect.colliderect(coinRect) == True:
            onegold = True
            if onegold == True:
                orriggold += 50
            onegold = False
            goldhit = True
            
        if playerRect.colliderect(addlifeRect) == True:
            onelife = True
            if onelife == True: #adds random amount of lives if powerup is picked up
                life += 1
            onelife = False
            lifehit = True
            
        if playerRect.colliderect(addlifeRect) == False and addlifey > 600 or playerRect.colliderect(addlifeRect) == False and addlifey < 0:
            lifehit = False #makes powerup disappear once you've hit it
             
        if playerRect.colliderect(coinRect) == False and coiny > 600 or playerRect.colliderect(coinRect) == False and coiny < 0:
            goldhit = False        
            
        if enemyy > 600:
            enemyy = 0 - 80
            enemyy = randint(-500,-200)  #resets object y coor
            enemyx = choice(enemylistx)
            
        if enemyy2 > 600: #resets object y coor
            enemyy2 = -80
            enemyy2 = randint(-500,-200)
            enemyx2 = choice(enemylistx)
            
        if enemyy3 > 600: #resets object y coor
            enemyy3 = 0 - 80
            enemyx3 = choice(enemylistx)
            enemyy3 = randint(-500,-200) 
            
        if enemyy4 > 600: #resets object y coor
            enemyy4 = 0 - 80
            enemyx4 = choice(enemylistx)
            enemyy4 = randint(-500,-200)             
            
        if rocky > 600: #resets object y coor
            rocky = 0 - 80
            rockx = randint(700,900)
            rocky = randint(-1000,0)     
            
        if alieny > 600: #resets object y coor
            alieny = 0 - 80
            alienx = randint(0,100)
            alieny = randint(-1000,0)
            
        if coiny > 600: #resets object y coor
            coiny = 0 - 80
            coinx = choice(enemylistx)
            coiny = randint(-5000,-1000)  
            
        if addlifey > 600: #resets object y coor
            addlifey = 0 - 80
            addlifex = choice(enemylistx)
            addlifey  = randint(-100000,-5000)
            
        if signy > 600: #resets object y coor
            signy = 0 - 80
            signx = randint(700,800)
            signy = randint(-10000,0)  
            
        #if orriggold > 0:
            #gold  = int(orriggold)
            #a = open("data/gold.dat",'w')
            #a.write(str(gold))
            #a.close()
        
        if enemyRect.colliderect(enemyRect2):
            enemyy2 -= 350 #makes sure enemies don't spawn on top of each other
        if enemyRect.colliderect(enemyRect3):
            enemyy3 -= 350 #makes sure enemies don't spawn on top of each other
        if enemyRect.colliderect(enemyRect4):
            enemyy -= 350   #makes sure enemies don't spawn on top of each other      
        if enemyRect2.collid erect(enemyRect3):
            enemyy3 -= 350
        if enemyRect2.colliderect(enemyRect4):
            enemyy4 -= 350
        if enemyRect3.colliderect(enemyRect4):
            enemyy3 -= 350    
            
            carx = 516
            enemyy = randint(-500,-200)
            enemyy2 = randint(-500,-200) #assigns new x coord
            enemyy3 = randint(-500,-200) 
            enemyy4 = randint(-500,-200) 
            time.wait(1000)            
            
        drawText('Score: %s' % (score), font, screen, 128, 0)
        drawText('Top Score: %s' % (topScore), font, screen, 128, 20)
        drawText('Lives: %s' % (life), font, screen, 128, 40)    #draws scoreboard
        #drawText('Gold Earned: %s' % (orriggold), font, screen, 128, 60) 
        #drawText('Gold In Total: %s' % (gold), font, screen, 128, 80) 
        
        instructions()
    return MAIN,button,carx,cary,cary_change,x,y,life,enemyx,enemyy,enemyx2,enemyx3,enemyx4,score,levelspeed,gold,orriggold,enemyy2,enemyy3,enemyy4,rockx,rocky,alienx,alieny,coinx,coiny,addlifex,addlifey,signx,signy,goldhit,lifehit,onegold,onelife
    
def gameover(MAIN,mx,my,button):
    if MAIN == 3:
        rects = [Rect(20,420,960,50),Rect(20,480,960,50)]
        screen.blit(caught,(0,0,1000,700))  
        draw.rect(screen,GREEN,rects[0])
        draw.rect(screen,RED,rects[1])
        drawText('GAME OVER',font,screen, 440, 295) #writes gameover
        drawText('PLAY AGAIN',font,screen, 445, 435)
        drawText('MAIN MENU',font,screen, 445, 495)
        if rects[0].collidepoint(mx,my):
            draw.rect(screen,GREEN,rects[0],5)
            if button == 1:
                MAIN = 1
        if rects[1].collidepoint(mx,my):
            draw.rect(screen,RED,rects[1],5)
            if button == 1:
                MAIN = 0 
                button = 0
    return MAIN,mx,my,button
   
while running: 
    display.set_caption("Trash Attack")       
    for evnt in event.get():             # checks all events that happen
        if evnt.type == QUIT or MAIN == -1:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            mx, my = evnt.pos          
            button = evnt.button         #main game loop checking for input
        if evnt.type == MOUSEMOTION:
            mx, my = evnt.pos
            
        if MAIN == 1:
            if evnt.type == KEYDOWN:
                if evnt.key == K_LEFT:
                    carx += -66
                elif evnt.key == K_RIGHT:
                    carx += 66
                elif evnt.key == K_UP:
                    cary_change = -5
                elif evnt.key == K_DOWN:
                    cary_change = 5
            
            if evnt.type == KEYUP:
                if evnt.key == K_UP or evnt.key == K_DOWN:
                    cary_change = 0    
        
    MAIN,button = StartMenu(MAIN,button)
    #MAIN = Shop(MAIN)
    MAIN,button = story(MAIN,button)
    MAIN,button,carx,cary,cary_change,x,y,life,enemyx,enemyy,enemyx2,enemyx3,enemyx4,score,levelspeed,gold,orriggold,enemyy2,enemyy3,enemyy4,rockx,rocky,alienx,alieny,coinx,coiny,addlifex,addlifey,signx,signy,goldhit,lifehit,onegold,onelife = Game(MAIN,button,carx,cary,cary_change,x,y,life,enemyx,enemyy,enemyx2,enemyx3,enemyx4,score,levelspeed,gold,orriggold,enemyy2,enemyy3,enemyy4,rockx,rocky,alienx,alieny,coinx,coiny,addlifex,addlifey,signx,signy,goldhit,lifehit,onegold,onelife)
    MAIN,mx,my,button = gameover(MAIN,mx,my,button) #call all functions to main loop
    display.flip()
    clock.tick(60)
    print(button)
quit()
    




