from pygame import * #Imports pygame in order to use
import random #Imports random for random colours
init() #Initiates code
size = width, height = 1000, 700 #Size of screen
screen = display.set_mode(size)


r = 255 
g = 255 #Starting RGB value for paintbrush
b = 255
button = 0 #Starting value of mouse clicks
radius = 10 #Starting radius of brush
smallfont = font.SysFont("Times New Roman",15) #Used for text in code

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (197, 197, 197)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (107, 104, 99)
PINK = (249, 57, 255)
LIGHT_BLUE = (54, 207, 241)
YELLOW = (255, 241, 73)
ORANGE = (252, 155, 64)      #Colours used
PURPLE = (167, 0, 238)
DARKER_GREEN = (58, 158, 73)
MAROON = (128,0,0)
NAVY = (0,0,128)
GOLD = (255,215,0)
PALE_GREEN = (152,251,152)
BLUE_VIOLET = (138,43,226)
MAGENTA = (255,0,255)
BEIGE = (245,245,220)
DARK_GREEN = (0,100,0)
LAWN_GREEN = (124,252,0)
SEA_GREEN = (46,139,87)
MIDNIGHT_BLUE = (25,25,112)
SADDLE_BROWN = (139,69,19)
STEEL_BLUE = (70,130,180)
SALMON = (250,128,114)
DARK_GOLD = (184,134,11)
KHAKI = (189,183,107)


def userInterface():
    draw.rect(screen,WHITE,(0,0,250,700)) #Draws side white menu bar 

def display_colour(r,g,b):
    draw.rect(screen,(r,g,b),(0,0,250,50))
    draw.rect(screen,BLACK,(0,0,250,50),2) #Displays current colour on top of the preset colours

def text_labels():
    e = smallfont.render("CLR",1,(255,255,255))
    screen.blit(e, Rect(209,268,40,40)) 
    e = smallfont.render("ERS",1,(255,255,255)) #Adds labels to buttons to let the user know the button's function
    screen.blit(e, Rect(209,368,40,40)) 
    e = smallfont.render("FILL",1,(255,255,255))
    screen.blit(e, Rect(209,218,40,40))  
    e = smallfont.render("RDM",1,(255,255,255))
    screen.blit(e, Rect(209,318,40,40))      
    
def drawBorder(x,y):
    draw.rect(screen,BLACK,(x, y, 40, 40),5) #Function that is recalled multiple times in order to draw borders around selected preset
    display.flip()
    
#==========COLOUR PRESET BUTTONS BEGIN=============
    
def colour_button_green(x,y,r,g,b):
    if 5+40 > x > 5 and 55+40 > y > 55:
        draw.rect(screen,GREEN,(5, 55, 40, 40))
        draw.rect(screen,BLACK,(5, 55, 40, 40),5) #Allows button to interact with user and sets RGB value of brush if clicked
        if button==1:
            r = 0
            g = 255
            b = 0
    else:
        draw.rect(screen,GREEN,(5, 55, 40, 40))
        draw.rect(screen,BLACK,(5, 55, 40, 40),3)
    return r,g,b

def colour_button_gray(x,y,r,g,b):
    if 55+40 > x > 55 and 55+40 > y > 55:
        draw.rect(screen,GRAY,(55, 55, 40, 40))
        draw.rect(screen,BLACK,(55, 55, 40, 40),5) #Allows button to interact with user and sets RGB value of brush if clicked
        if button==1:
            r = 197
            g = 197
            b = 197
    else:
        draw.rect(screen,GRAY,(55, 55, 40, 40))
        draw.rect(screen,BLACK,(55, 55, 40, 40),3) 
    return r,g,b

def colour_button_white(x,y,r,g,b):
    if 105+40 > x > 105 and 55+40 > y > 55:
        draw.rect(screen,WHITE,(105, 55, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(105, 55, 40, 40),5)
        if button==1:
            r = 255
            g = 255
            b = 255
    else:
        draw.rect(screen,WHITE,(105, 55, 40, 40))
        draw.rect(screen,BLACK,(105, 55, 40, 40),3) 
    return r,g,b
     
def colour_button_red(x,y,r,g,b):
    if 155+40 > x > 155 and 55+40 > y > 55:   
        draw.rect(screen,RED,(155, 55, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(155, 55, 40, 40),5)
        if button==1:
            r = 255
            g = 0
            b = 0        
    else:
        draw.rect(screen,RED,(155, 55, 40, 40))
        draw.rect(screen,BLACK,(155, 55, 40, 40),3) 
    return r,g,b
        
def colour_button_blue(x,y,r,g,b):
    if 5+40 > x > 5 and 105+40 > y > 105: 
        draw.rect(screen,BLUE,(5, 105, 40, 40))
        draw.rect(screen,BLACK,(5, 105, 40, 40),5) #Allows button to interact with user and sets RGB value of brush if clicked
        if button==1:
            r = 0
            g = 0
            b = 255          
    else:
        draw.rect(screen,BLUE,(5, 105, 40, 40))
        draw.rect(screen,BLACK,(5, 105, 40, 40),3)
    return r,g,b

def colour_button_dark_gray(x,y,r,g,b):
    if 55+40 > x > 55 and 105+40 > y > 105: 
        draw.rect(screen,DARK_GRAY,(55, 105, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(55, 105, 40, 40),5)
        if button==1:
            r = 107
            g = 104
            b = 99        
    else:
        draw.rect(screen,DARK_GRAY,(55, 105, 40, 40))
        draw.rect(screen,BLACK,(55, 105, 40, 40),3)
    return r,g,b

def colour_button_pink(x,y,r,g,b):
    if 105+40 > x > 105 and 105+40 > y > 105:         #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,PINK,(105, 105, 40, 40))
        draw.rect(screen,BLACK,(105, 105, 40, 40),5)
        if button==1:
            r = 249
            g = 57
            b = 255          
    else:
        draw.rect(screen,PINK,(105, 105, 40, 40))
        draw.rect(screen,BLACK,(105, 105, 40, 40),3)
    return r,g,b

def colour_button_light_blue(x,y,r,g,b):
    if 155+40 > x > 155 and 105+40 > y > 105: 
        draw.rect(screen,LIGHT_BLUE,(155, 105, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(155, 105, 40, 40),5)
        if button==1:
            r = 54
            g = 207
            b = 241          
    else:
        draw.rect(screen,LIGHT_BLUE,(155, 105, 40, 40))
        draw.rect(screen,BLACK,(155, 105, 40, 40),3) 
    return r,g,b

def colour_button_yellow(x,y,r,g,b):
    if 5+40 > x > 5 and 155+40 > y > 155:     
        draw.rect(screen,YELLOW,(5, 155, 40, 40))
        draw.rect(screen,BLACK,(5, 155, 40, 40),5) #Allows button to interact with user and sets RGB value of brush if clicked
        if button==1:
            r = 255
            g = 241
            b = 73         
    else:
        draw.rect(screen,YELLOW,(5, 155, 40, 40))
        draw.rect(screen,BLACK,(5, 155, 40, 40),3)
    return r,g,b

def colour_button_orange(x,y,r,g,b):       
    if 55+40 > x > 55 and 155+40 > y > 155:  
        draw.rect(screen,ORANGE,(55, 155, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(55, 155, 40, 40),5)
        if button==1:
            r = 252
            g = 155
            b = 64          
    else:
        draw.rect(screen,ORANGE,(55, 155, 40, 40))
        draw.rect(screen,BLACK,(55, 155, 40, 40),3)
    return r,g,b

def colour_button_purple(x,y,r,g,b):       
    if 105+40 > x > 105 and 155+40 > y > 155:         
        draw.rect(screen,PURPLE,(105, 155, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(105, 155, 40, 40),5)
        if button==1:
            r = 167
            g = 0
            b = 238          
    else:
        draw.rect(screen,PURPLE,(105, 155, 40, 40))
        draw.rect(screen,BLACK,(105, 155, 40, 40),3)
    return r,g,b

def colour_button_darker_green(x,y,r,g,b):       
    if 155+40 > x > 155 and 155+40 > y > 155:   
        draw.rect(screen,DARKER_GREEN,(155, 155, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(155, 155, 40, 40),5)
        if button==1:
            r = 58
            g = 158
            b = 73      
    else:
        draw.rect(screen,DARK_GREEN,(155, 155, 40, 40))
        draw.rect(screen,BLACK,(155, 155, 40, 40),3)
    return r,g,b

def colour_button_maroon(x,y,r,g,b):       
    if 5+40 > x > 5 and 205+40 > y > 205: 
        draw.rect(screen,MAROON,(5, 205, 40, 40))
        draw.rect(screen,BLACK,(5, 205, 40, 40),5) #Allows button to interact with user and sets RGB value of brush if clicked
        if button==1:
            r = 128
            g = 0
            b = 0          
    else:    
        draw.rect(screen,MAROON,(5, 205, 40, 40))
        draw.rect(screen,BLACK,(5, 205, 40, 40),3)
    return r,g,b

def colour_button_navy(x,y,r,g,b):       
    if 55+40 > x > 55 and 205+40 > y > 205: 
        draw.rect(screen,NAVY,(55, 205, 40, 40))
        draw.rect(screen,BLACK,(55, 205, 40, 40),5) #Allows button to interact with user and sets RGB value of brush if clicked
        if button==1:
            r = 0
            g = 0
            b = 128          
    else:
        draw.rect(screen,NAVY,(55, 205, 40, 40))
        draw.rect(screen,BLACK,(55, 205, 40, 40),3)
    return r,g,b

def colour_button_gold(x,y,r,g,b):       
    if 105+40 > x > 105 and 205+40 > y > 205:        
        draw.rect(screen,GOLD,(105, 205, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(105, 205, 40, 40),5)
        if button==1:
            r = 255
            g = 215
            b = 0          
    else:
        draw.rect(screen,GOLD,(105, 205, 40, 40))
        draw.rect(screen,BLACK,(105, 205, 40, 40),3)
    return r,g,b

def colour_button_pale_green(x,y,r,g,b):       
    if 155+40 > x > 155 and 205+40 > y > 205: 
        draw.rect(screen,PALE_GREEN,(155, 205, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(155, 205, 40, 40),5)
        if button==1:
            r = 152
            g = 251
            b = 152          
    else:
        draw.rect(screen,PALE_GREEN,(155, 205, 40, 40))
        draw.rect(screen,BLACK,(155, 205, 40, 40),3)        
    return r,g,b

def colour_button_violet_blue(x,y,r,g,b):       
    if 5+40 > x > 5 and 255+40 > y > 255: 
        draw.rect(screen,BLUE_VIOLET,(5, 255, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(5, 255, 40, 40),5)
        if button==1:
            r = 138
            g = 43
            b = 226          
    else:
        draw.rect(screen,BLUE_VIOLET,(5, 255, 40, 40))
        draw.rect(screen,BLACK,(5, 255, 40, 40),3)
    return r,g,b

def colour_button_magenta(x,y,r,g,b):       
    if 55+40 > x > 55 and 255+40 > y > 255: 
        draw.rect(screen,MAGENTA,(55, 255, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(55, 255, 40, 40),5)
        if button==1:
            r = 255
            g = 0
            b = 255          
    else:
        draw.rect(screen,MAGENTA,(55, 255, 40, 40))
        draw.rect(screen,BLACK,(55, 255, 40, 40),3)
    return r,g,b

def colour_button_beige(x,y,r,g,b):       
    if 105+40 > x > 105 and 255+40 > y > 255: 
        draw.rect(screen,BEIGE,(105, 255, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(105, 255, 40, 40),5)
        if button==1:
            r = 245
            g = 245
            b = 220          
    else:
        draw.rect(screen,BEIGE,(105, 255, 40, 40))
        draw.rect(screen,BLACK,(105, 255, 40, 40),3)
    return r,g,b

def colour_button_lawn_green(x,y,r,g,b):       
    if 155+40 > x > 155 and 255+40 > y > 255: 
        draw.rect(screen,LAWN_GREEN,(155, 255, 40, 40))  #Allows button to interact with user and sets RGB value of brush if clicked   
        draw.rect(screen,BLACK,(155, 255, 40, 40),5)  
        if button==1:
            r = 124
            g = 252
            b = 0          
    else:
        draw.rect(screen,LAWN_GREEN,(155, 255, 40, 40))    
        draw.rect(screen,BLACK,(155, 255, 40, 40),3)
    return r,g,b

def colour_button_dark_green(x,y,r,g,b):       
    if 5+40 > x > 5 and 305+40 > y > 305: 
        draw.rect(screen,DARK_GREEN,(5, 305, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(5, 305, 40, 40),5)
        if button==1:
            r = 0
            g = 100
            b = 0          
    else:
        draw.rect(screen,DARK_GREEN,(5, 305, 40, 40))
        draw.rect(screen,BLACK,(5, 305, 40, 40),3)  
    return r,g,b

def colour_button_sea_green(x,y,r,g,b):       
    if 55+40 > x > 55 and 305+40 > y > 305: 
        draw.rect(screen,SEA_GREEN,(55, 305, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(55, 305, 40, 40),5)
        if button==1:
            r = 46
            g = 139
            b = 87          
    else:
        draw.rect(screen,SEA_GREEN,(55, 305, 40, 40))
        draw.rect(screen,BLACK,(55, 305, 40, 40),3)
    return r,g,b

def colour_button_midnight_blue(x,y,r,g,b):       
    if 105+40 > x > 105 and 305+40 > y > 305: 
        draw.rect(screen,MIDNIGHT_BLUE,(105, 305, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(105, 305, 40, 40),5)
        if button==1:
            r = 25
            g = 25
            b = 112          
    else:
        draw.rect(screen,MIDNIGHT_BLUE,(105, 305, 40, 40))
        draw.rect(screen,BLACK,(105, 305, 40, 40),3)
    return r,g,b

def colour_button_saddle_brown(x,y,r,g,b):       
    if 155+40 > x > 155 and 305+40 > y > 305: 
        draw.rect(screen,SADDLE_BROWN,(155, 305, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(155, 305, 40, 40),5)   
        if button==1:
            r = 139
            g = 69
            b = 19          
    else:
        draw.rect(screen,SADDLE_BROWN,(155, 305, 40, 40)) 
        draw.rect(screen,BLACK,(155, 305, 40, 40),3)          
    return r,g,b

def colour_button_steel_blue(x,y,r,g,b):       
    if 5+40 > x > 5 and 355+40 > y > 355: 
        draw.rect(screen,STEEL_BLUE,(5, 355, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(5, 355, 40, 40),5)
        if button==1:
            r = 70
            g = 130
            b = 180          
    else:
        draw.rect(screen,STEEL_BLUE,(5, 355, 40, 40))
        draw.rect(screen,BLACK,(5, 355, 40, 40),3)
    return r,g,b

def colour_button_salmon(x,y,r,g,b):       
    if 55+40 > x > 55 and 355+40 > y > 355: 
        draw.rect(screen,SALMON,(55, 355, 40, 40))
        draw.rect(screen,BLACK,(55, 355, 40, 40),5) #Allows button to interact with user and sets RGB value of brush if clicked
        if button==1:
            r = 250
            g = 128
            b = 114          
    else:
        draw.rect(screen,SALMON,(55, 355, 40, 40))
        draw.rect(screen,BLACK,(55, 355, 40, 40),3)
    return r,g,b

def colour_button_dark_gold(x,y,r,g,b):       
    if 105+40 > x > 105 and 355+40 > y > 355: 
        draw.rect(screen,DARK_GOLD,(105, 355, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(105, 355, 40, 40),5)
        if button==1:
            r = 184
            g = 134
            b = 11          
    else:
        draw.rect(screen,DARK_GOLD,(105, 355, 40, 40))
        draw.rect(screen,BLACK,(105, 355, 40, 40),3)
    return r,g,b

def colour_button_khaki(x,y,r,g,b):       
    if 155+40 > x > 155 and 355+40 > y > 355: 
        draw.rect(screen,KHAKI,(155, 355, 40, 40)) #Allows button to interact with user and sets RGB value of brush if clicked
        draw.rect(screen,BLACK,(155, 355, 40, 40),5)
        if button==1:
            r = 189
            g = 183
            b = 107          
    else:
        draw.rect(screen,KHAKI,(155, 355, 40, 40))
        draw.rect(screen,BLACK,(155, 355, 40, 40),3)    
    return r,g,b

#=========COLOUR PRESET BUTTONS END===============

def button_fill(r,g,b):  
    if 205+40 > mx > 205 and 205+40 > my > 205: 
        draw.rect(screen,BLACK,(205, 205, 40, 40)) #Draws for fill function
        draw.rect(screen,BLACK,(205, 205, 40, 40),5)          
        if button==1:
            draw.rect(screen,(r,g,b),(250,0,750,700)) #Fills the entire screen with selected paint if mouse is clicked
    else:
        draw.rect(screen,BLACK,(205, 205, 40, 40)) 
        draw.rect(screen,BLACK,(205, 205, 40, 40),3) 

def button_clear():  
    if 205+40 > mx > 205 and 255+40 > my > 255: 
        draw.rect(screen,BLACK,(205, 255, 40, 40)) #Draws for clear function
        draw.rect(screen,BLACK,(205, 255, 40, 40),5)        
        if button==1:
            draw.rect(screen,BLACK,(250,0,750,700)) #Covers entire screen with black to clear canvas
    else:
        draw.rect(screen,BLACK,(205, 255, 40, 40)) 
        draw.rect(screen,BLACK,(205, 255, 40, 40),3)         

def button_eraser(x,y,r,g,b):     
    if 205+40 > mx > 205 and 355+40 > my > 355:
        draw.rect(screen,BLACK,(205, 355, 40, 40)) #Draws button for eraser function
        draw.rect(screen,BLACK,(205, 355, 40, 40),5)          
        if button==1:
            r = 0
            g = 0 #If mouse is clicked, colour of brush changes to black in order to erase
            b = 0
    else:
        draw.rect(screen,BLACK,(205, 355, 40, 40)) 
        draw.rect(screen,BLACK,(205, 355, 40, 40),3)     
    return r,g,b

def brush_interface():
    draw.rect(screen,WHITE,(20,400,200,50))
    draw.circle(screen,BLACK,(20,425),10) #Draws overall interface/slider of the brush size selection
    draw.line(screen,GRAY,(35,425),(200,425),5)
    draw.circle(screen,BLACK,(225,425),20)

def button_brush_size(x,y, r):
    
    radius = 10 #Initial radius
    if 35+165 > x > 35 and 405+40 > y > 405: 
        if button==1:
            brush_interface()
            draw.line(screen,BLACK,(x,415),(x,435),5) #Sets new radius to the x value of the user's click
            radius = x
            return radius//4 #division by 4 make radius range more logical
    return r
            
def button_random(x,y,r,g,b):
    if 205+40 > mx > 205 and 305+40 > my > 305:
        draw.rect(screen,BLACK,(205,305,40,40)) #Draws button for random colour function
        draw.rect(screen,BLACK,(205,305,40,40),5)         
        if button==1:
            r = random.randint(0,255)
            g = random.randint(0,255) #Assigns random numvers to RGB if mouse is clicked
            b = random.randint(0,255)
    else:
        draw.rect(screen,BLACK,(205,305,40,40))
        draw.rect(screen,BLACK,(205,305,40,40),3)          
    return r,g,b


def r_interface():
    startcoor = 0
    r = 0
    while startcoor < 250:
        draw.rect(screen,(r,0,0),(startcoor,560,0,40)) #Loop to set colour gradiants for RED
        startcoor += 1
        r += 1  
    
def g_interface():
    startcoor = 0
    g = 0
    while startcoor < 250:
        draw.rect(screen,(0,g,0),(startcoor,605,0,40)) #Loop to set colour gradiants for GREEN
        startcoor += 1
        g += 1 
        
def b_interface():
    startcoor = 0
    b = 0
    while startcoor < 250:
        draw.rect(screen,(0,0,b),(startcoor,650,0,40)) #Loop to set colour gradiants for BLUE
        startcoor += 1
        b += 1   
        
def red_set(x,y, rval):
    if 0 < x < 250 and 560 < y < 600:
        if button==1:
            r_interface()
            draw.line(screen,BLACK,(x,560),(x,599),5) #Assigns x value of mouse click to R value
            return x
    return rval

def green_set(x,y,gval):
    if 0 < x < 250 and 600 < y < 640:
        if button==1:
            g_interface()
            draw.line(screen,BLACK,(x,605),(x,643),5) #Assigns x value of mouse click to G value
            return x
    return gval    

    
def blue_set(x,y,bval):
    if 0 < x < 250 and 640 < y < 680:
        if button==1:
            b_interface()
            draw.line(screen,BLACK,(x,650),(x,688),5) #Assigns x value of mouse click to B value
            return x
    return bval 
    

def drawScene(screen, button,r,g,b,radius):
    # Draw circle if the left mouse button is down. Does the make function of drawing on canvas
    if (250+radius)+750 > mx > (250+radius) and 0+700 > my > 0:
        if button==1:
            draw.circle(screen, (r,g,b), (mx,my), radius)
    display.flip()

running = True 

def getVal(tup):
    for i in range(3):
        if tup[i]==1:
            return i+1
    return 0


userInterface()
brush_interface()
r_interface()
g_interface()
b_interface() #Calls all methods used to make up the application interface before game loop
red_set(0,0,r)
green_set(0,0,g)
blue_set(0,0,b) 
display.flip()

# Game Loop
while running:
    
    for evnt in event.get():             # checks all events that happen
        if evnt.type == QUIT:
            running = False
        if evnt.type == MOUSEBUTTONDOWN:
            mx, my = evnt.pos          
            button = evnt.button        
        if evnt.type == MOUSEMOTION:
            mx, my = evnt.pos
            button = getVal(evnt.buttons)
    
    #Loading feature
    if 5+240 > mx > 5 and 495+30 > my > 495:
        draw.rect(screen,BLACK,(5, 495, 240, 30)) 
        draw.rect(screen,BLACK,(5, 495, 240, 30),5) #Draws button responsible to load image
        e = smallfont.render("LOAD AND SAVE",1,(0,0,0))
        screen.blit(e, Rect(5,500,240,30))          
                   
        if button==1:
            pic = image.load("PaintImage_.png") #Loads picture if mouse is clicked
            screen.blit(pic,(250,0))
    else:
        draw.rect(screen,BLACK,(5, 495, 240, 30)) 
        draw.rect(screen,BLACK,(5, 495, 240, 30),3)  
          
            
    #Saving feature
    if 5+240 > mx > 5 and 455+30 > my > 455: 
        draw.rect(screen,BLACK,(5, 455, 240, 30)) 
        draw.rect(screen,BLACK,(5, 455, 240, 30),5)  #Draws button responsible tosave image
                
        if button==1:
            save_surface = Surface((380, 320))
            save_surface.blit(screen, (0, 0), (100, 0, 380, 320)) #Saves image as PaintImage_.png with the click of mouse button
            
            
            try:
                sav = "PaintImage_" + ".png"
              
                    
            except IOError:
                save_flag = True
            picture = Rect(250,0,750,700)
            sub = screen.subsurface(picture)
            image.save(sub, sav)   
            print("File has been saved!") #Let's you know that file has been daved in python shell
            button = 0   
    draw.rect(screen,BLACK,(5, 455, 240, 30)) 
    draw.rect(screen,BLACK,(5, 455, 240, 30),3)   
    
    
    
    ##ABOUT CODE BELOW:
    ##I tried manking GUIs to save and load files, I nailed the save GUI, however, 
    ##I experinced difficulties involving removing deleted letters from screen #and mouse input. However, I still believe it is worth you looking at and #give me advice on. I spent a lot of time learning this and I hope you #understand what I was trying to go for 
    
    
    
    
        
        #draw.rect(screen,BLACK,(5, 455, 240, 30)) 
        #draw.rect(screen,BLACK,(5, 455, 240, 30),3)                 
    #if 5+240 > mx > 5 and 455+30 > my > 455: 
            #draw.rect(screen,BLACK,(5, 455, 240, 30)) 
            #draw.rect(screen,BLACK,(5, 455, 240, 30),5) 
            #if button==1:
                #draw.rect(screen,WHITE,(400,200,450,400))
                #draw.rect(screen,GREEN,(500,500,100,50))
                #save = smallfont.render("SAVE" , 1, (0, 0, 0))
                #screen.blit(save, Rect(530,515,100,50))
                #draw.rect(screen,RED,(650,500,100,50))
                #cancel = smallfont.render("CANCEL" , 1, (0, 0, 0))
                #screen.blit(cancel, Rect(670,515,100,50))                
                #text = medfont.render("Please Enter Your File Name Below:" , 1, (0, 0, 0))
                #text2 = medfont.render("(If You Make A Typo, Please ",1,(0,0,0))
                #text3 = medfont.render("Press Cancel And Try Again)",1,(0,0,0))
                #screen.blit(text3, Rect(405,280,450,400))
                #screen.blit(text2, Rect(405,250,450,400))
                #screen.blit(text, Rect(405,220,450,400))
                
                #name = ""
                #while True:
                    #for evnt in event.get():
                        #if evnt.type == KEYDOWN:
                            #if evnt.unicode.isalpha():
                                #name += evnt.unicode
                            #if evnt.unicode.isdigit():
                                #name += evnt.unicode
                            #if evnt.key == K_BACKSPACE:
                                #name = name[:-1]
                            #if evnt.type == MOUSEBUTTONDOWN:
                                    #mx, my = evnt.pos          
                                    #button = evnt.button        
                            #if evnt.type == MOUSEMOTION:
                                    #mx, my = evnt.pos
                                    #button = getVal(evnt.buttons)                                
                            
                                   
                        #file = medfont.render(name, True, (0, 0, 0))
                        #screen.blit(file, Rect(405,400,450,400))
                        #display.flip()
                 
            #if 500+100 > mx > 500 and 500+50 > my > 500: 
                #if button==1:
                    #save_surface = Surface((380, 320))
                    #save_surface.blit(screen, (0, 0), (100, 0, 380, 320))
                            
                            
                    #try:
                        #sav = name + '.png'
                        #with open(sav):
                            #print("file already exists")
                                    
                    #except IOError:
                        #save_flag = True
                           
                        #image.save(screen, sav)   
                        #print("File has been saved!")
                        #button = 0  
            
            #draw.rect(screen,BLACK,(5, 455, 240, 30)) 
            #draw.rect(screen,BLACK,(5, 455, 240, 30),3)      
      
    r, g, b = colour_button_darker_green(mx,my,r,g,b) 
    r, g, b = colour_button_dark_gray(mx,my,r,g,b)
    r, g, b = colour_button_gray(mx,my,r,g,b)
    r, g, b = colour_button_green(mx,my,r,g,b)
    r, g, b = colour_button_light_blue(mx,my,r,g,b)
    r, g, b = colour_button_orange(mx,my,r,g,b)
    r, g, b = colour_button_pink(mx,my,r,g,b)
    r, g, b = colour_button_purple(mx,my,r,g,b)
    r, g, b = colour_button_red(mx,my,r,g,b)
    r, g, b = colour_button_blue(mx,my,r,g,b)
    r, g, b = colour_button_white(mx,my,r,g,b)
    r, g, b = colour_button_yellow(mx,my,r,g,b)
    r, g, b = colour_button_maroon(mx,my,r,g,b)
    r, g, b = colour_button_beige(mx,my,r,g,b)
    r, g, b = colour_button_dark_green(mx,my,r,g,b)
    r, g, b = colour_button_lawn_green(mx,my,r,g,b)
    r, g, b = colour_button_sea_green(mx,my,r,g,b)  #Calls all colour preset buttons to game loop to become part of the application
    r, g, b = colour_button_midnight_blue(mx,my,r,g,b)
    r, g, b = colour_button_saddle_brown(mx,my,r,g,b)
    r, g, b = colour_button_steel_blue(mx,my,r,g,b)
    r, g, b = colour_button_salmon(mx,my,r,g,b)
    r, g, b = colour_button_dark_gold(mx,my,r,g,b)
    r, g, b = colour_button_khaki(mx,my,r,g,b)
    r, g, b = colour_button_navy(mx,my,r,g,b)
    r, g, b = colour_button_gold(mx,my,r,g,b)
    r, g, b = colour_button_pale_green(mx,my,r,g,b)
    r, g, b = colour_button_violet_blue(mx,my,r,g,b)
    r, g, b = colour_button_magenta(mx,my,r,g,b)
    r, g, b = colour_button_steel_blue(mx,my,r,g,b)
    r, g, b = button_random(mx,my,r,g,b)
    r, g, b = button_eraser(mx,my,r,g,b)
    display_colour(r,g,b)
    button_brush_size(mx,my, radius)
    button_fill(r,g,b) #Calls functional buttons to make application more useful
    button_clear()
    text_labels()

    #If statements below ensure that a thick black border stays on a selected preset to signify that it is in use
    if r==0 and g==255 and b==0:
        drawBorder(5, 55) #Green
    if r==197 and g==197 and b==197:
        drawBorder(55, 55) #Gray
    if r==255 and g==255 and b==255:
        drawBorder(105, 55) #White
    if r==255 and g==0 and b==0:
        drawBorder(155, 55) #Red
    if r==0 and g==0 and b==255:
        drawBorder(5, 105) #Blue
    if r==107 and g==104 and b==99:
        drawBorder(55, 105) #Dark Gray
    if r==249 and g==57 and b==255:
        drawBorder(105, 105) #Pink
    if r==54 and g==207 and b==241:
        drawBorder(155, 105) #Light Blue
    if r==255 and g==241 and b==73:
        drawBorder(5, 155) #Yellow
    if r==252 and g==155 and b==64:
        drawBorder(55, 155) #Orange
    if r==167 and g==0 and b==238:
        drawBorder(105, 155) #Purple
    if r==58 and g==158 and b==73:
        drawBorder(155, 155) #Darker Green
    if r==128 and g==0 and b==0:
        drawBorder(5, 205) #Maroon
    if r==0 and g==0 and b==128:
        drawBorder(55, 205) #Navy    
    if r==255 and g==215 and b==0:
        drawBorder(105, 205) #Gold
    if r==152 and g==251 and b==152:
        drawBorder(155, 205) #Pale Green    
    if r==138 and g==43 and b==226: 
        drawBorder(5, 255) #Blue Violet
    if r==255 and g==0 and b==255:
        drawBorder(55, 255) #Magenta 
    if r==245 and g==245 and b==220:
        drawBorder(105,255) #Beige
    if r==124 and g==252 and b==0:
        drawBorder(155,255) #Lawn Green
    if r==0 and g==100 and b==0:
        drawBorder(5,305) #Dark Green
    if r==46 and g==139 and b==87:
        drawBorder(55,305) #Sea Green
    if r==25 and g==25 and b==112:
        drawBorder(105,305) #Midnight Blue
    if r==139 and g==69 and b==19:
        drawBorder(155,305) #Saddle Brown
    if r==70 and g==130 and b==180:
        drawBorder(5,355) #Steel Blue
    if r==250 and g==128 and b==114:
        drawBorder(55,355) #Salmon
    if r==184 and g==134 and b==11:
        drawBorder(105,355) #Dark Gold
    if r==189 and g==183 and b==107:
        drawBorder(155,355) #Khaki
    
   
    
    radius = button_brush_size(mx,my, radius)
    r = red_set(mx,my,r)
    g = green_set(mx,my,g) #Manipulations to a couple variables in order to make them usable
    b = blue_set(mx,my,b)  
    drawScene(screen, button,r,g,b,radius)
 
quit()