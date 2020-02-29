import random #Allows me to randomize certain aspects of my picture

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" %(0, 0) #Places screen to the top left corner

import pygame   
pygame.init()   # ALL pygame programs need to initialize the pygame engine
                # before they can use it


                
PALEYELLOW = (255, 255, 153) 
CRATERYELLOW = (255,255,51) # we use ALL CAPS for constants so we remember not to change them
BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,153,51)
BLUE = (51,153,255)         #Colours that will be used to create the visuals
GREEN = (34,139,34)
BROWN = (145,85,61)
DARKBLUE = (51,56,74)
NEONGREEN = (0,255,0)
PEACH = (255,228,181)        # Defining a colour constant(variables we should not be changing)
DARKPEACH = (208,182,138)
BRICKRED = (178,34,34)
FLOORPURPLE = (76,0,153)
GREY = (128,128,128)
FLOORRED = (102,0,0)
FLOORGREEN = (0,51,25)
FLOORBLUE = (0,0,51)
FLOORBROWN = (102,51,0)    #All colours used at some point during the code
FLOORLIGHTBLUE = (153,153,255)
FLOORDORANGE = (204,102,0)
STORMBLUE = (118,165,192)
LIGHTBLUE = (50,157,219)
DARKERBLUE = (46,94,121)
SKYORANGE = (155,92,20)
DORANGE = (233,87,43)
VERYYELLOW = (255,247,0)
DEMONICPURPLE = (11,0,105)
SKYRED = (255,102,102)
VIOLET = (153,0,153)
GRAVEBROWN = (139,69,19)



SIZE = (1000, 700)                 # Open a pygame window  
screen = pygame.display.set_mode(SIZE) #sets the screen size to 1000x700 pixels


def draw_sky(): #Function determines the colour of the sky
                colour = [STORMBLUE, LIGHTBLUE, DARKERBLUE, SKYORANGE, DORANGE, VERYYELLOW, DEMONICPURPLE, SKYRED, VIOLET] #Creates a list of colours to choose from
                pygame.draw.rect(screen, random.choice(colour), [0, 0, 1000, 600]) #Random.choice let's python pick a colour out of the list and use it as the colour of the sky
              
                
def draw_moon(): #Function determines the shape, colour and the location of the moon
                x = random.randint(0,1000) #Allows the moon to be positioned anywhere within a 1000x300 area
                y = random.randint(0,300)                
                pygame.draw.circle(screen,PALEYELLOW,(x, y), 50)
                pygame.draw.circle(screen,CRATERYELLOW,(x-5,y-10),10) #smaller circles are located inside the moon and placed all over the place to signify craters at the surface of the moon
                pygame.draw.circle(screen,CRATERYELLOW,(x-10,y+20),15)
                pygame.draw.circle(screen,CRATERYELLOW,(x+20,y-22),20)                         
                                        
                                        
def draw_stars(): #Function determines the shape, colour and the location and the amount of stars
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  #pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  is repeated 25 times in order to place 25 stars in random locations within a 1000x325 area 
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  
                pygame.draw.rect(screen, WHITE, [random.randint(0,1000), random.randint(0,325), 2, 2])  


def draw_ground(): #Function determines the colour of the ground
                colour = [FLOORGREEN, FLOORPURPLE, FLOORRED, GREEN, FLOORBLUE, FLOORBROWN, FLOORDORANGE, FLOORLIGHTBLUE] #Creates a list of colours to choose from
                pygame.draw.rect(screen, random.choice(colour), [0, 600, 1000, 100]) #Random.choice let's python pick a colour out of the list and use it as the colour of the ground
               
                
def draw_trees(): #Function places two pine trees on either side of the screen
                pygame.draw.rect(screen, BROWN, [60, 550, 30, 50]) #Trunk of the left tree
                pygame.draw.polygon(screen, GREEN, [[150, 550], [75, 400], [0, 550]])
                pygame.draw.polygon(screen, GREEN, [[140, 500], [75, 350], [10, 500]]) #Leaves of the left tree
                pygame.draw.rect(screen, BROWN, [910, 550, 30, 50]) #Trunk of the right tree
                pygame.draw.polygon(screen, GREEN, [[850, 550], [925, 400], [1000, 550]])
                pygame.draw.polygon(screen, GREEN, [[860, 500], [925, 350], [990, 500]]) #Leaves of the right tree


def draw_pumpkin(): #Function uses different shapes to make a pumpkin
                x = random.randint(600,1000) #Allows the pumpkins to be placed anywhere withing a 400x25 area
                y = random.randint(625,650)
                pygame.draw.ellipse(screen, ORANGE, (x,y,30,45))
                pygame.draw.ellipse(screen, ORANGE, (x-15,y,30,45)) #A combination of ellipses and a rectangle as a stem resemble a pumpkin
                pygame.draw.ellipse(screen, ORANGE, (x+15,y,30,45))
                pygame.draw.rect(screen, NEONGREEN, [x+13,y-10,5,12])
                
                
def draw_grave(): #Uses different shapes to make tombstones
                x = random.randint(0,500) #Allows the tombs to be placed anywhere withing a 500x25 area
                y = random.randint(625,650)
                pygame.draw.line(screen, GREY, (x+20,y+40), (x+20,y-15),8)
                pygame.draw.line(screen, GREY, (x,y-2), (x+40,y-2),8)
                pygame.draw.circle(screen, GRAVEBROWN, (x, y+40), 10) #Thick lines make tombstone, while brown circles represent the dirt around tomb
                pygame.draw.circle(screen, GRAVEBROWN, (x+18, y+40), 15)
                pygame.draw.circle(screen, GRAVEBROWN, (x+35, y+40), 10)
           
                   
def draw_house_foundation(): #Creates lower portion of the house
                pygame.draw.rect(screen, BLACK, [250, 575, 500, 25],2) 
                pygame.draw.rect(screen, BRICKRED, [250, 575, 500, 25]) #Big rectangle acts as foundation for house
                pygame.draw.rect(screen, WHITE, [470, 575, 60, 5])
                pygame.draw.rect(screen, WHITE, [460, 580, 80, 5])
                pygame.draw.rect(screen, WHITE, [450, 585, 100, 5]) #Make small white steps up to the entrance of the house
                pygame.draw.rect(screen, WHITE, [440, 590, 120, 5])
                pygame.draw.rect(screen, WHITE, [430, 595, 140, 5])
                pygame.draw.line(screen, BLACK, (460, 580), (540,580))
                pygame.draw.line(screen, BLACK, (450, 585), (550,585)) #Make a black border around steps to make them easier to make out in the picture
                pygame.draw.line(screen, BLACK, (440, 590), (560,590))
                pygame.draw.line(screen, BLACK, (430, 595), (570,595))
            
                
def draw_fence(): #Uses many lines to create a railing around the porch
                pygame.draw.line(screen, WHITE, (360, 450), (360,600),10)
                pygame.draw.line(screen, WHITE, (460, 450), (460,600),10) #Thick line travel from the roof to the floor to act as pillars
                pygame.draw.line(screen, WHITE, (540, 450), (540,600),10)
                pygame.draw.line(screen, WHITE, (640, 450), (640,600),10)
                pygame.draw.line(screen, WHITE, (350, 550), (460,550),5)
                pygame.draw.line(screen, WHITE, (540, 550), (750,550),5)
                pygame.draw.line(screen, WHITE, (555, 550), (555,600),5)
                pygame.draw.line(screen, WHITE, (565, 550), (565,600),5)
                pygame.draw.line(screen, WHITE, (575, 550), (575,600),5)
                pygame.draw.line(screen, WHITE, (585, 550), (585,600),5)
                pygame.draw.line(screen, WHITE, (595, 550), (595,600),5)
                pygame.draw.line(screen, WHITE, (605, 550), (605,600),5) #White lines represent the railing
                pygame.draw.line(screen, WHITE, (615, 550), (615,600),5)
                pygame.draw.line(screen, WHITE, (625, 550), (625,600),5)
                pygame.draw.line(screen, WHITE, (635, 550), (635,600),5)
                pygame.draw.line(screen, WHITE, (370, 550), (370,600),5)
                pygame.draw.line(screen, WHITE, (380, 550), (380,600),5)
                pygame.draw.line(screen, WHITE, (390, 550), (390,600),5)
                pygame.draw.line(screen, WHITE, (400, 550), (400,600),5)
                pygame.draw.line(screen, WHITE, (410, 550), (410,600),5)
                pygame.draw.line(screen, WHITE, (420, 550), (420,600),5)
                pygame.draw.line(screen, WHITE, (430, 550), (430,600),5)
                pygame.draw.line(screen, WHITE, (440, 550), (440,600),5)
                pygame.draw.line(screen, WHITE, (450, 550), (450,600),5)                


def draw_door(): #Draws a simple door at the center of the house
                pygame.draw.rect(screen, BRICKRED, [480, 500, 40, 75])
                pygame.draw.circle(screen, VERYYELLOW, (490,550), 5) #Adds a tiny door knob to the door
                


def draw_windows(x,y): #Draws a basic window design that is used throughout the house
                pygame.draw.rect(screen, WHITE, [x, y, 30, 35]) #Big rectangle is white in order to act as a border
                pygame.draw.rect(screen, BLUE, [x+3, y+3, 24, 29]) #Smaller rectangle inside acts as the blue colour of the reflection of the sky
                pygame.draw.line(screen, WHITE, (x+10, y+3), (x+10, y+32), 2) 
                pygame.draw.line(screen, WHITE, (x+18, y+3), (x+18, y+32), 2) #White lines separate window in different sections
                pygame.draw.line(screen, WHITE, (x+3, y+17.5), (x+27, y+17.5), 2)
            
                        
def draw_subhouse(x,y): #Draws one of the side portions of the house
                pygame.draw.rect(screen, PEACH, [x-50, y, 100, 125])
                pygame.draw.polygon(screen, PEACH, [[x-60, y], [x+60, y], [x, y-50]])
                pygame.draw.polygon(screen, BLACK, [[x-60, y], [x+60, y], [x, y-50]],2)
                pygame.draw.line(screen, BLACK, (x+50, y), (x+50, y+125), 2)
                pygame.draw.line(screen, BLACK, (x-50, y), (x-50, y+125), 2)
                draw_windows(270,477.5)
                draw_windows(300,477.5)
                draw_windows(270,512.5) #Window function is called back in order to draw windows in there appropriate places
                draw_windows(300,512.5)
                draw_windows(670,477.5)
                draw_windows(700,477.5)
                draw_windows(670,512.5)
                draw_windows(700,512.5)
          
                
def draw_house(): #Joins all the separate sections of the house and the main portion of the house together through one big function
                pygame.draw.polygon(screen, DARKBLUE, [[300, 450], [400, 350], [600, 350], [700,450]]) #Draws roof
                pygame.draw.polygon(screen, BLACK, [[300, 450], [400, 350], [600, 350], [700,450]],2)
                pygame.draw.rect(screen, PEACH, [440, 360, 40, 65])
                pygame.draw.rect(screen, BLACK, [440, 360, 40, 65],2)
                pygame.draw.polygon(screen, PEACH, [[435, 360], [485, 360], [460, 325]]) #Draws left roof opening
                pygame.draw.polygon(screen, BLACK, [[435, 360], [485, 360], [460, 325]],2)
                pygame.draw.rect(screen, PEACH, [520, 360, 40, 65])
                pygame.draw.rect(screen, BLACK, [520, 360, 40, 65],2)
                pygame.draw.polygon(screen, PEACH, [[515, 360], [565, 360], [540, 325]]) #Draws right roof opening
                pygame.draw.polygon(screen, BLACK, [[515, 360], [565, 360], [540, 325]],2)
                pygame.draw.rect(screen, DARKPEACH, [350, 450, 300, 150]) #Dras center portion of the house (where railings, door, and some windows are)
                draw_windows(445, 375)
                draw_windows(525, 375)
                draw_windows(390, 465)
                draw_windows(400, 465) #Window that are not on the subhouse are all drawn with all these window functions
                draw_windows(390, 500)
                draw_windows(400, 500)    
                draw_windows(570, 465)
                draw_windows(580, 465)
                draw_windows(570, 500)
                draw_windows(580, 500)                 
                draw_fence() #Railings are drawn by recalling this function
                draw_house_foundation() #Lower portion of the house is drawn by recalling function
                draw_subhouse(300,450)
                draw_subhouse(700,450)   #Both subhouses are called in to be drawn infront of the house   
                draw_door() #Door is drawn at the front of the house


#=====MAIN PROGRAM=====


draw_sky() #Sky function is recalled to show a randomized sky colour
draw_stars() #Star functon is recalled to show a randomized order of stars in the sky
draw_moon() #Moon function is recalled to show the moon in a randomized location in the sky
draw_trees() #Recalls function to draw the pine trees
draw_ground() #Ground function is recalled to show a randomized ground colour
draw_house() #Mega function is recalled to construct the entire house
draw_grave() 
draw_grave() #Grave function is called four times to create four tombstones in the picture
draw_grave() 
draw_grave() 
draw_pumpkin() 
draw_pumpkin() 
draw_pumpkin() #Pumpkin function is called four times to create four pumpkins in the front yard of the house
draw_pumpkin() 






pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()