def collision(myX,userX,myY,userY, myRadius, userRadius): #The variables in here are comprised of user-input values as well as set values from me to find out if the user's circle collides with mine
      if int(userX - myX)**2 + int(userY - myX)**2 <= int(userRadius + myRadius)**2: #This equation basically finds out if the distance between the x and y coordinates of the user and my circle. If the distance of the coordinates is equal to the sum of the radii (That is a word. Search it up.) of the two circles
            print("Your circle and my circle collide.")
      else:
            print("Your circle and my circle do not collide.") #If the sum of the radii and the distance between the two centers are not equal, then we just use an else statement to write that the two circles do not collide
            
mycoorx = 0 #Sets my center's x coordinate at 0
mycoory = 0 #Sets my center's y coordinate at 0
myradius = 50 #Sets my radius length at 50 units

print("My circle's center is located at (0,0) and it has a radius of 50 units.") #This print statement states the measurements of my circle for the user's information

#Level 3+
radius = myradius**2 #squares the radius to make it easier to use the formula (x2-x1)**2 + (y2-y1)**2 = r**2

coor3=input("Please put a coordinate of a point in a (x,y) form: ")    #Asks the user to input the coordinates of there point in (x,y)
usercoorx3 = int(coor3[1:coor3.find(",")]) #Isolates and finds the x coordinate of the user's desire by using string manipulation. 
usercoory3 = int(coor3[coor3.find(",")+1:coor3.find(")")]) #Isolates and and finds the y coordinate of the user's desire by using string manipulation. 

dist = ((usercoorx3-mycoorx)**2 + (usercoory3 - mycoory)**2) #Converts string input to int input to calculate the distance between the user input point and my circle's center  
if dist > radius:
      print ("The point is outside the circle.")  #If the distance is bigger than the radius, then that means that the user input-point will fall outside of the circle
elif dist == radius:
      print ("The point is on the circle.")       #If the distance is equal to the length of my radius, then that means that the point lies on my circle
else:
      print ("The point is inside the circle.")   #If the distance is smaller than the length of my radius, then that means that the point is inside my circle


#Level 4+
coor = input("Please enter the dimensions of your circle in the form (x,y) radius: ") #Asks the user to input the x, y, and radius measurements by only using one input command (Duh you can CLEARLY see that)

userradius = coor[coor.find(" ")+1:] #Isolates and finds the radius measurement of the user's desire by using string manipulation.
usercoorx = coor[1:coor.find(",")] #Isolates and finds the x coordinate of the user's desire by using string manipulation. 
usercoory = coor[coor.find(",")+1:coor.find(")")] #Isolates and and finds the y coordinate of the user's desire by using string manipulation. (What can I say, you told us that you copy paste a lot in coding)

#======Comparisons to Check if User Input is Correct========

if coor.startswith("(") == False: #Ensures that the user starts input with a start bracket
      print("Please ensure that your input starts with a start bracket. Your input should be in the form \"(x,y) radius\".") 
    
elif coor.find("(") == -1: #Finds out if user hasn't put a start bracket and motions user to use one
      print("Please input a start bracket (there should be at least one start bracket). Your input should be in the form \"(x,y) radius\".")
      
      #OPTIONAL CODE BELOW
      
#elif userradius == "":
      #print("Please input a radius. Your input should look like \"(x,y) radius\".") #Checks to see if user has even input a radius at all
          
#elif usercoorx == "":
      #print("Please input a x coordinate. Your input should look like \"(x,y) radius\".") #Checks to see if user has even input a x coordinate at all
          
#elif usercoory == "":
      #print("Please input a y coordinate. Your input should look like \"(x,y) radius\".") #Checks to see if user has even input a y coordinate at all
      
#The above comparisons are OPTIONAL lines of code that make the error handling more accurate. This code specifically deals with when the user types in "(,) " However, they are optional and can be left untouched depending on how you feel Mr. Van Rooyen. NOTE: I hope I don't get marks taken off for these lines of code as they are technically "comments" and are not part of my code.


    
elif coor.find(")") == -1: #Finds out if user hasn't put a end bracket and motions user to use one
      print("Please input a end bracket (there should be at least one end bracket). Your input should be in the form \"(x,y) radius\".")
    
elif coor.find(",") == -1: #Finds out if user hasn't used a comma and motions user to use one
      print("Please input a comma to separate the coordinates (there should be at least one comma present in your input). Your input should be in the form \"(x,y) radius\".")
    
elif coor.find(" ") == -1: #Finds out if user hasn't used a space to separate his/her input and encourages to use the space
      print("Please input the space to separate the x and y coordinates. Your input should be in the form \"(x,y) radius\".")
    
elif usercoorx.startswith("-") == True: #Does the collision(myX,userX,myY,userY, myRadius, userRadius) function early in the case of the user using a negative integer as a x coordinate
      usercoorx = coor[2:coor.find(",")]  #Takes "-" out so x coordinate is an integer
      usercoorx = int(usercoorx)
      usercoory = int(usercoory) #Converts all string inputs to integers
      userradius = int(userradius)
      collision(mycoorx,usercoorx,mycoory,usercoory,myradius,userradius)
      
elif usercoory.startswith("-") == True: #Does the collision(myX,userX,myY,userY, myRadius, userRadius) function early in the case of the user using a negative integer as a y coordinate 
      usercoory = coor[coor.find(",")+2:coor.find(")")] #Takes "-" out so y coordinate is an integer
      usercoorx = int(usercoorx)
      usercoory = int(usercoory) #Converts all string inputs to integers
      userradius = int(userradius)
      collision(mycoorx,usercoorx,mycoory,usercoory,myradius,userradius)
      
elif usercoory.startswith("-") == True and usercoorx.startswith("-") == True: #does the collision(myX,userX,myY,userY, myRadius, userRadius) function early in the case of the user using negative integers
      usercoorx = coor[2:coor.find(",")]  #Takes "-" out so x coordinate is an integer
      usercoory = coor[coor.find(",")+2:coor.find(")")] #Takes "-" out so y coordinate is an integer
      usercoorx = int(usercoorx)
      usercoory = int(usercoory) #Converts all string inputs to integers
      userradius = int(userradius)
      collision(mycoorx,usercoorx,mycoory,usercoory,myradius,userradius)      
    
elif coor.count("(") != 1: #Counts if the user has input more than one opening bracket to break the code
      print("Please enter only one start bracket (there should not be more than one start bracket present in the input). Your input should be in the form \"(x,y) radius\".") 
    
elif coor.count(")") != 1: #Counts if the user has input more than one closing bracket to break the code
      print("Please enter only one end bracket (there should not be more than one end bracket present in the input). Your input should be in the form \"(x,y) radius\".") 
    
elif coor.count(",") != 1: #Counts if the user has input more than one coma to break the code
      print("Please enter only one comma (We aren't working with three coordinates or anything else here). Your input should be in the form \"(x,y) radius\".") 
    
elif coor.count(" ") != 1: 
      print("Please enter only one space to separate the x and y coordinates and the radius measurement (You can't just put spaces as values or write words in this input!). Your input should be in the form \"(x,y) radius\".") #Ensures that user does not add more than the required amount of spaces in the input command
    
elif userradius.isdigit() == False:
      print("Please ensure that your radius value is an integer (no symbols, or letters of any sort can be used). Your input should be in the form \"(x,y) radius\".") #Checks if user has input a valid radius value instead of alphabets
    
elif usercoorx.isdigit() == False:
      print("Please ensure that the x coordinate value is an integer (no symbols, or letters of any sort can be used). Your input should be in the form \"(x,y) radius\".") #Checks if user has input a valid x coordinate value instead of alphabets
    
elif usercoory.isdigit() == False:
      print("Please ensure that the y coordinate value is an integer (no symbols, or letters of any sort can be used). Your input should be in the form \"(x,y) radius\".") #Checks if user has input a valid y coordinate value instead of alphabets
      

    
#======Action Taken after it is Determined that the User Input is Correct======

else:
      usercoorx = int(usercoorx)  
      usercoory = int(usercoory) #Converts all string inputs to integers
      userradius = int(userradius)
      collision(mycoorx,usercoorx,mycoory,usercoory,myradius,userradius) #After the comparisons, if python finds that the input is correct (all brackets, comma, space, and positive integers are used), it converts the strings to integers and then plugs them into the collision(mycoorx,usercoorx,mycoory,usercoory,myradius,userradius) command to find out if the circles collide or not
