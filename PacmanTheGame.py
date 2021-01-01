from tkinter import *
import turtle
from turtle import *
import math
import random

#https://www.youtube.com/watch?v=YXPyB4XeYLA

root = Tk()
root.title('Pac-Man - The Game')
root.geometry('550x270')

myLabel = Label(root, text='Hello There! \n Welcome to Pac-Man - The Game')
myLabel.pack()

#Instructions button
def instructionsClick():
	Instructions ="Follow the instructions in the terminal'.\n Enter W,A,S,D keys into the terminal to navigate the turtle through the map.\n Every dot you consume provides you with 1 points.\nThe aim of the game is to eat all the dots and reach the other end without colliding with the ghosts.\n There are three levels & more :D Best of Luck!!!"
	myLabel = Label(root, text = Instructions)
	myLabel.pack()

myButton = Button(root, text='Instructions', command=instructionsClick)
myButton.pack()

#About Button
def aboutClick():
	Creation = 'Created by: F08G09 CLASS OF 2024 \n Umang Sanjeev Gupta (1005393) \n Adelle Chan Min Hui (1005418) \n Adriana Ng Elynn (1005356) \n Ho Jun Hui Nicholas (1005001)' 
	myLabel = Label(root, text = Creation)
	myLabel.pack()

myButton = Button(root, text='About The Game', command=aboutClick)
myButton.pack()

#Quit Button
button_quit = Button(root, text='Exit Program', command =root.quit)
button_quit.pack()

#Gamecode

def game():
	Name = input('Hello There, Welcome to our Pac-Man game!!!\nPls click on to the instruction button to find out how to play the game\nWhen ready, please enter your name.')
	difficulty = input('What difficulty would u like to play on? Easy, Medium, or Hard').lower()
	hardness = ['easy', 'medium', 'hard', 'extra hard', 'hardest', 'kenny choo']
	god_mode = ['extra hard', 'hardest', 'kenny choo']
	if difficulty in hardness:
		print('Hello ',Name, 'The difficulty you have chosen is', difficulty, 'All the best and Have Fun!!!')
	else:
		print('Not a correct choice: {}'.format(difficulty))

	t = turtle.Turtle()
	t.speed("fastest")
	t.shape("square")
	t.color("blue")
	t.shapesize(2,2,2)
	t.penup()
	sc=turtle.Screen()
	sc.bgcolor("black")
	H = 860
	W = 740
	step = 40
	sc.setup(H,W)
	t.speed("fastest")
	#t.pensize(15)
	t.pencolor("black")
	h = H-100
	w = W-100
	w1 = (w-2*step)//(2*step)

	#Refer to Appendix 1 for lines of code used to produce coordinates
	lsc = [(-300.00,-40.00), (-340.00,-40.00), (-380.00,-40.00), (-380.00,-80.00), (-380.00,-120.00), (-380.00,-160.00), (-380.00,-200.00), (-380.00,-240.00), (-380.00,-280.00), (-340.00,-280.00), (-300.00,-280.00), (-260.00,-280.00), (-220.00,-280.00), (-180.00,-280.00), (-140.00,-280.00), (-100.00,-280.00), (-60.00,-280.00), (-20.00,-280.00), (20.00,-280.00), (60.00,-280.00), (100.00,-280.00), (140.00,-280.00), (180.00,-280.00), (220.00,-280.00), (260.00,-280.00), (300.00,-280.00), (340.00,-280.00), (340.00,-240.00), (340.00,-200.00), (340.00,-160.00), (340.00,-120.00), (340.00,-80.00), (340.00,-40.00), (300.00,-40.00), (260.00,-40.00), (260.00,-120.00), (260.00,-160.00), (260.00,-200.00), (220.00,-200.00), (180.00,-200.00), (20.00,-200.00), (20.00,-160.00), (20.00,-120.00), (20.00,-80.00), (60.00,-80.00), (100.00,-80.00), (100.00,-160.00), (100.00,-200.00), (100.00,-240.00), (100.00,-280.00), (-60.00,-200.00), (-60.00,-160.00), (-60.00,-120.00), (-60.00,-80.00), (-100.00,-80.00), (-140.00,-80.00), (-140.00,-160.00), (-140.00,-200.00), (-140.00,-240.00), (-140.00,-280.00), (-220.00,-200.00), (-260.00,-200.00), (-300.00,-200.00), (-300.00,-160.00), (-300.00,-120.00), (-300.00,40.00), (-340.00,40.00), (-380.00,40.00), (-380.00,80.00), (-380.00,120.00), (-380.00,160.00), (-380.00,200.00), (-380.00,240.00), (-380.00,280.00), (-340.00,280.00), (-300.00,280.00), (-260.00,280.00), (-220.00,280.00), (-180.00,280.00), (-140.00,280.00), (-100.00,280.00), (-60.00,280.00), (-20.00,280.00), (20.00,280.00), (60.00,280.00), (100.00,280.00), (140.00,280.00), (180.00,280.00), (220.00,280.00), (260.00,280.00), (300.00,280.00), (340.00,280.00), (340.00,240.00), (340.00,200.00), (340.00,160.00), (340.00,120.00), (340.00,80.00), (340.00,40.00), (300.00,40.00), (260.00,40.00), (260.00,120.00), (260.00,160.00), (260.00,200.00), (220.00,200.00), (180.00,200.00), (20.00,200.00), (20.00,160.00), (20.00,120.00), (20.00,80.00), (60.00,80.00), (100.00,80.00), (100.00,160.00), (100.00,200.00), (100.00,240.00), (100.00,280.00), (-60.00,200.00), (-60.00,160.00), (-60.00,120.00), (-60.00,80.00), (-100.00,80.00), (-140.00,80.00), (-140.00,160.00), (-140.00,200.00), (-140.00,240.00), (-140.00,280.00), (-220.00,200.00), (-260.00,200.00), (-300.00,200.00), (-300.00,160.00), (-300.00,120.00), (-220.00,120.00), (-220.00,80.00), (-220.00,40.00), (-220.00,0.00), (-220.00,-40.00), (-220.00,-80.00), (-220.00,-120.00), (180.00,-120.00), (180.00,-80.00), (180.00,-40.00), (180.00,0.00), (180.00,40.00), (180.00,80.00), (180.00,120.00), (100.00,0.00), (60.00,0.00), (20.00,0.00), (-20.00,0.00), (-60.00,0.00), (-100.00,0.00), (-140.00,0.00)]

	for k in lsc:
	    t.stamp()
	    t.goto(k)
	    
	starth = h//2
	startw = w//2

	border = False

	ls = []
	for i in range(-starth,starth,step):
	    for j in range((-startw+step),startw,step):
	        ls.append((float(i),float(j)))


	ft = turtle.Turtle()
	ft.penup()
	ft.shape("circle")
	ft.color("pink")
	ft.shapesize(0.5,0.5,0.5)
	ft.goto(-380,0)
	ft.speed("fastest")
	border = False
	fval=0
	score = 0
	fid = {}
	for k in ls:
	    for l in lsc:
	        if (k==l):
	            border = True
	            break
	    if(border == False):
	        ft.goto(k)
	        id = ft.stamp()
	        fid[k]=id
	        fval+=1
	    else:
	        border = False
	#print(fval)

	pt = turtle.Turtle()
	pt.penup()
	pt.speed("fastest")
	pt.shape("turtle")
	pt.color("yellow")
	pt.shapesize(1.5,1.5,1.5)
	#start = h//2
	pt.goto(-starth,0)
	ft.clearstamp(fid[(-starth,0)])

	#x(-380,380) (STEPSIZE40)
	#Y(-320,320)
	#Creating the ghosts

	gh1= turtle.Turtle()
	gh1.penup()
	#gh.speed()
	gh1.goto(-260,240)
	gh1.shapesize(2,2,2)
	gh1.color("red")
	g1border = False
	

	gh2= turtle.Turtle()
	gh2.penup()
	#gh.speed()
	gh2.goto(-260,-240)
	gh2.shapesize(2,2,2)
	gh2.color("green")
	g2border = False

	gh3= turtle.Turtle()
	gh3.penup()
	#gh.speed()
	gh3.goto(260,240)
	gh3.shapesize(2,2,2)
	gh3.color("yellow")
	g3border = False
	repf = []

	gh4= turtle.Turtle()
	gh4.penup()
	#gh.speed()
	gh4.goto(260,-240)
	gh4.shapesize(2,2,2)
	gh4.color("purple")
	g4border = False
	repf = []

	if (difficulty != 'easy'):
		gh5= turtle.Turtle()
		gh5.penup()
		#gh.speed()
		gh5.goto(-20,240)
		gh5.shapesize(2,2,2)
		gh5.color("white")
		g5border = False
		repf = []
	
	if (difficulty != 'easy'):
		
		gh6= turtle.Turtle()
		gh6.penup()
		#gh.speed()
		gh6.goto(20,-240)
		gh6.shapesize(2,2,2)
		gh6.color("orange")
		g6border = False
		repf = []
		
	if (difficulty != 'easy') and (difficulty != 'medium'):	
		gh7= turtle.Turtle()
		gh7.penup()
		#gh.speed()
		gh7.goto(-140,120)
		gh7.shapesize(2,2,2)
		gh7.color("light steel blue")
		g7border = False
		repf = []

	if (difficulty != 'easy') and (difficulty != 'medium'):
		gh8= turtle.Turtle()
		gh8.penup()
		#gh.speed()
		gh8.goto(-140,-120)
		gh8.shapesize(2,2,2)
		gh8.color("lemonchiffon")
		g8border = False
		repf = []

	if (difficulty != 'easy') and (difficulty != 'medium'):
		gh9= turtle.Turtle()
		gh9.penup()
		#gh.speed()
		gh9.goto(140,120)
		gh9.shapesize(2,2,2)
		gh9.color("pale green")
		g9border = False
		repf = []

	if (difficulty != 'easy') and (difficulty != 'medium'):
		gh10= turtle.Turtle()
		gh10.penup()
		#gh.speed()
		gh10.goto(140,-120)
		gh10.shapesize(2,2,2)
		gh10.color("crimson")
		g10border = False
		repf = []
		#i = 0
	if difficulty in god_mode:
		gh11= turtle.Turtle()
		gh11.penup()
		#gh.speed()
		gh11.goto(-60,0)
		gh11.shapesize(2,2,2)
		gh11.color("tomato")
		g11border = False
		repf = []

	if difficulty in god_mode:
		gh12= turtle.Turtle()
		gh12.penup()
		#gh.speed()
		gh12.goto(60,0)
		gh12.shapesize(2,2,2)
		gh12.color("aquamarine")
		g12border = False
		repf = []

	if difficulty in god_mode:
		gh13= turtle.Turtle()
		gh13.penup()
		#gh.speed()
		gh13.goto(-180,200)
		gh13.shapesize(2,2,2)
		gh13.color("gold")
		g13border = False
		repf = []

	if difficulty in god_mode:
		gh14= turtle.Turtle()
		gh14.penup()
		#gh.speed()
		gh14.goto(-180,-200)
		gh14.shapesize(2,2,2)
		gh14.color("blue violet")
		g14border = False
		repf = []

	if difficulty in god_mode:
		gh15= turtle.Turtle()
		gh15.penup()
		#gh.speed()
		gh15.goto(180,-200)
		gh15.shapesize(2,2,2)
		gh15.color("lavender")
		g15border = False
		repf = []

	if difficulty in god_mode:
		gh16= turtle.Turtle()
		gh16.penup()
		#gh.speed()
		gh16.goto(180,200)
		gh16.shapesize(2,2,2)
		gh16.color("light cyan")
		g16border = False
		repf = []

	if difficulty in god_mode:
		gh17= turtle.Turtle()
		gh17.penup()
		#gh.speed()
		gh17.goto(-340,280)
		gh17.shapesize(2,2,2)
		gh17.color("dim gray")
		g17border = False
		repf = []


	if difficulty in god_mode:
		gh18= turtle.Turtle()
		gh18.penup()
		#gh.speed()
		gh18.goto(-340,-280)
		gh18.shapesize(2,2,2)
		gh18.color("saddle brown")
		g18border = False
		repf = []


	if difficulty in god_mode:
		gh19= turtle.Turtle()
		gh19.penup()
		#gh.speed()
		gh19.goto(340,280)
		gh19.shapesize(2,2,2)
		gh19.color("hot pink")
		g19border = False
		repf = []


	if difficulty in god_mode:
		gh20= turtle.Turtle()
		gh20.penup()
		#gh.speed()
		gh20.goto(340,-280)
		gh20.shapesize(2,2,2)
		gh20.color("rosy brown")
		g20border = False
		repf = []

#Logic for ghost
	while(pt.pos()!=(starth,0)):

	       #while(gh.pos()!=(starth,0)):
	            '''if (difficulty == 'easy'):
	            	#if(pt.pos()==gh1.pos() or pt.pos()==gh2.pos() or pt.pos()==gh3.pos()or pt.pos()==gh4.pos()):
	            		#print("game over")
	            		#break
	            #if (difficulty == 'medium'):
	            	#if(pt.pos()==gh1.pos() or pt.pos()==gh2.pos() or pt.pos()==gh3.pos()or pt.pos()==gh4.pos()or pt.pos()==gh5.pos()or pt.pos()==gh6.pos()):
	            		#print("game over")
	            		break
	            #if (difficulty == 'hard'):
	            	#if(pt.pos()==gh1.pos() or pt.pos()==gh2.pos() or pt.pos()==gh3.pos()or pt.pos()==gh4.pos()or pt.pos()==gh5.pos()or pt.pos()==gh6.pos()or pt.pos()==gh7.pos()or pt.pos()==gh8.pos()or pt.pos()==gh9.pos()or pt.pos()==gh10.pos()):
	            		#print("game over")
	            		break
	            if difficulty in god_mode:
	            	if(pt.pos()==gh1.pos() or pt.pos()==gh2.pos() or pt.pos()==gh3.pos()or pt.pos()==gh4.pos()or pt.pos()==gh5.pos()or pt.pos()==gh6.pos()or pt.pos()==gh7.pos()or pt.pos()==gh8.pos()or pt.pos()==gh9.pos()or pt.pos()==gh10.pos()or pt.pos()==gh11.pos()or pt.pos()==gh12.pos()or pt.pos()==gh13.pos()or pt.pos()==gh14.pos()or pt.pos()==gh15.pos()or pt.pos()==gh16.pos()or pt.pos()==gh17.pos()or pt.pos()==gh18.pos()or pt.pos()==gh19.pos()or pt.pos()==gh20.pos()):
	                	print("game over")
	                	break'''
	            gch = random.randint(0,4)
	            g1x,g1y = gh1.pos()
	   
	            if(gch == 0):
	                g1x = round(g1x-step)
	                g1y = round(g1y)
	            elif(gch == 1):
	                g1x = round(g1x)
	                g1y = round(g1y-step)
	            elif(gch == 2):
	                g1x = round(g1x)
	                g1y = round(g1y+step)
	            elif(gch == 3):
	                g1x = round(g1x+step)
	                g1y = round(g1y)
	   
	            g1x = float(g1x)
	            g1y = float(g1y)
	            g1pos = (g1x,g1y)
	        
	            if(g1x <  (step-starth) or g1y < (step-startw) or g1x >  (starth-step) or g1y > (startw-step)):
	                g1border = True
	        
	            if(g1border == False):
	                gh1.goto(g1x,g1y) 
	            else:
	       		    g1border = False
	            
	             
	            gch = random.randint(0,4)
	            g2x,g2y = gh2.pos()
	   
	            if(gch == 0):
	                g2x = round(g2x-step)
	                g2y = round(g2y)
	            elif(gch == 1):
	                g2x = round(g2x)
	                g2y = round(g2y-step)
	            elif(gch == 2):
	                g2x = round(g2x)
	                g2y = round(g2y+step)
	            elif(gch == 3):
	                g2x = round(g2x+step)
	                g2y = round(g2y)
	   
	            g2x = float(g2x)
	            g2y = float(g2y)
	            g2pos = (g2x,g2y)
	        
	            if(g2x <  (step-starth) or g2y < (step-startw) or g2x >  (starth-step) or g2y > (startw-step)):
	                g2border = True
	        
	            if(g2border == False):
	                gh2.goto(g2x,g2y) 
	            else:
	                g2border = False

	            gch = random.randint(0,4)
	            g3x,g3y = gh3.pos()
	   
	            if(gch == 0):
	                g3x = round(g3x-step)
	                g3y = round(g3y)
	            elif(gch == 1):
	                g3x = round(g3x)
	                g3y = round(g3y-step)
	            elif(gch == 2):
	                g3x = round(g3x)
	                g3y = round(g3y+step)
	            elif(gch == 3):
	                g3x = round(g3x+step)
	                g3y = round(g3y)
	   
	            g3x = float(g3x)
	            g3y = float(g3y)
	            g3pos = (g3x,g3y)
	        
	            if(g3x <  (step-starth) or g3y < (step-startw) or g3x >  (starth-step) or g3y > (startw-step)):
	                g3border = True
	        
	            if(g3border == False):
	                gh3.goto(g3x,g3y) 
	            else:
	                g3border = False

	            gch = random.randint(0,4)
	            g4x,g4y = gh4.pos()
	   
	            if(gch == 0):
	                g4x = round(g4x-step)
	                g4y = round(g4y)
	            elif(gch == 1):
	                g4x = round(g4x)
	                g4y = round(g4y-step)
	            elif(gch == 2):
	                g4x = round(g4x)
	                g4y = round(g4y+step)
	            elif(gch == 3):
	                g4x = round(g4x+step)
	                g4y = round(g4y)
	   
	            g4x = float(g4x)
	            g4y = float(g4y)
	            g4pos = (g4x,g4y)
	        
	            if(g4x <  (step-starth) or g4y < (step-startw) or g4x >  (starth-step) or g4y > (startw-step)):
	                g4border = True
	        
	            if(g4border == False):
	                gh4.goto(g4x,g4y) 
	            else:
	                g4border = False

	            if (difficulty != 'easy'):
		            gch = random.randint(0,4)
		            g5x,g5y = gh5.pos()
		   
		            if(gch == 0):
		                g5x = round(g5x-step)
		                g5y = round(g5y)
		            elif(gch == 1):
		                g5x = round(g5x)
		                g5y = round(g5y-step)
		            elif(gch == 2):
		                g5x = round(g5x)
		                g5y = round(g5y+step)
		            elif(gch == 3):
		                g5x = round(g5x+step)
		                g5y = round(g5y)
		   
		            g5x = float(g5x)
		            g5y = float(g5y)
		            g5pos = (g5x,g5y)
		        
		            if(g5x <  (step-starth) or g5y < (step-startw) or g5x >  (starth-step) or g5y > (startw-step)):
		                g5border = True
		        
		            if(g5border == False):
		                gh5.goto(g5x,g5y) 
		            else:
		                g5border = False

	            if (difficulty != 'easy'):
		            gch = random.randint(0,4)
		            g6x,g6y = gh6.pos()
		   
		            if(gch == 0):
		                g6x = round(g6x-step)
		                g6y = round(g6y)
		            elif(gch == 1):
		                g6x = round(g6x)
		                g6y = round(g6y-step)
		            elif(gch == 2):
		                g6x = round(g6x)
		                g6y = round(g6y+step)
		            elif(gch == 3):
		                g6x = round(g6x+step)
		                g6y = round(g6y)
		   
		            g6x = float(g6x)
		            g6y = float(g6y)
		            g6pos = (g6x,g6y)
		        
		            if(g6x <  (step-starth) or g6y < (step-startw) or g6x >  (starth-step) or g6y > (startw-step)):
		                g6border = True
		        
		            if(g6border == False):
		                gh6.goto(g6x,g6y) 
		            else:
		                g6border = False

	            if (difficulty != 'easy') and (difficulty != 'medium'):
		            gch = random.randint(0,4)
		            g7x,g7y = gh7.pos()
		   
		            if(gch == 0):
		                g7x = round(g7x-step)
		                g7y = round(g7y)
		            elif(gch == 1):
		                g7x = round(g7x)
		                g7y = round(g7y-step)
		            elif(gch == 2):
		                g7x = round(g7x)
		                g7y = round(g7y+step)
		            elif(gch == 3):
		                g7x = round(g7x+step)
		                g7y = round(g7y)
		   
		            g7x = float(g7x)
		            g7y = float(g7y)
		            g7pos = (g7x,g7y)
		        
		            if(g7x <  (step-starth) or g7y < (step-startw) or g7x >  (starth-step) or g7y > (startw-step)):
		                g7border = True
		        
		            if(g7border == False):
		                gh7.goto(g7x,g7y) 
		            else:
		                g7border = False

	            if (difficulty != 'easy') and (difficulty != 'medium'):
		            gch = random.randint(0,4)
		            g8x,g8y = gh8.pos()
		   
		            if(gch == 0):
		                g8x = round(g8x-step)
		                g8y = round(g8y)
		            elif(gch == 1):
		                g8x = round(g8x)
		                g8y = round(g8y-step)
		            elif(gch == 2):
		                g8x = round(g8x)
		                g8y = round(g8y+step)
		            elif(gch == 3):
		                g8x = round(g8x+step)
		                g8y = round(g8y)
		   
		            g8x = float(g8x)
		            g8y = float(g8y)
		            g8pos = (g8x,g8y)
		        
		            if(g8x <  (step-starth) or g8y < (step-startw) or g8x >  (starth-step) or g8y > (startw-step)):
		                g8border = True
		        
		            if(g8border == False):
		                gh8.goto(g8x,g8y) 
		            else:
		                g8border = False

	            if (difficulty != 'easy') and (difficulty != 'medium'):
		            gch = random.randint(0,4)
		            g9x,g9y = gh9.pos()
		   
		            if(gch == 0):
		                g9x = round(g9x-step)
		                g9y = round(g9y)
		            elif(gch == 1):
		                g9x = round(g9x)
		                g9y = round(g9y-step)
		            elif(gch == 2):
		                g9x = round(g9x)
		                g9y = round(g9y+step)
		            elif(gch == 3):
		                g9x = round(g9x+step)
		                g9y = round(g9y)
		   
		            g9x = float(g9x)
		            g9y = float(g9y)
		            g9pos = (g9x,g9y)
		        
		            if(g9x <  (step-starth) or g9y < (step-startw) or g9x >  (starth-step) or g9y > (startw-step)):
		                g9border = True
		        
		            if(g9border == False):
		                gh9.goto(g9x,g9y) 
		            else:
		                g9border = False

	            if (difficulty != 'easy') and (difficulty != 'medium'):
		            gch = random.randint(0,4)
		            g10x,g10y = gh10.pos()
		   
		            if(gch == 0):
		                g10x = round(g10x-step)
		                g10y = round(g10y)
		            elif(gch == 1):
		                g10x = round(g10x)
		                g10y = round(g10y-step)
		            elif(gch == 2):
		                g10x = round(g10x)
		                g10y = round(g10y+step)
		            elif(gch == 3):
		                g10x = round(g10x+step)
		                g10y = round(g10y)
		   
		            g10x = float(g10x)
		            g10y = float(g10y)
		            g10pos = (g10x,g10y)
		        
		            if(g10x <  (step-starth) or g10y < (step-startw) or g10x >  (starth-step) or g10y > (startw-step)):
		                g10border = True
		        
		            if(g10border == False):
		                gh10.goto(g10x,g10y) 
		            else:
		                g10border = False

	            if difficulty in god_mode:
		            gch = random.randint(0,4)
		            g11x,g11y = gh11.pos()
		   
		            if(gch == 0):
		                g11x = round(g11x-step)
		                g11y = round(g11y)
		            elif(gch == 1):
		                g11x = round(g11x)
		                g11y = round(g11y-step)
		            elif(gch == 2):
		                g11x = round(g11x)
		                g11y = round(g11y+step)
		            elif(gch == 3):
		                g11x = round(g11x+step)
		                g11y = round(g11y)
		   
		            g11x = float(g11x)
		            g11y = float(g11y)
		            g11pos = (g11x,g11y)
		        
		            if(g11x <  (step-starth) or g11y < (step-startw) or g11x >  (starth-step) or g11y > (startw-step)):
		                g11border = True
		        
		            if(g11border == False):
		                gh11.goto(g11x,g11y) 
		            else:
		                g11border = False

	            if difficulty in god_mode:
		            gch = random.randint(0,4)
		            g12x,g12y = gh12.pos()
		   
		            if(gch == 0):
		                g12x = round(g12x-step)
		                g12y = round(g12y)
		            elif(gch == 1):
		                g12x = round(g12x)
		                g12y = round(g12y-step)
		            elif(gch == 2):
		                g12x = round(g12x)
		                g12y = round(g12y+step)
		            elif(gch == 3):
		                g12x = round(g12x+step)
		                g12y = round(g12y)
		   
		            g12x = float(g12x)
		            g12y = float(g12y)
		            g12pos = (g12x,g12y)
		        
		            if(g12x <  (step-starth) or g12y < (step-startw) or g12x >  (starth-step) or g12y > (startw-step)):
		                g12border = True
		        
		            if(g12border == False):
		                gh12.goto(g12x,g12y) 
		            else:
		                g12border = False

	            if difficulty in god_mode:
		            gch = random.randint(0,4)
		            g13x,g13y = gh13.pos()
		   
		            if(gch == 0):
		                g13x = round(g13x-step)
		                g13y = round(g13y)
		            elif(gch == 1):
		                g13x = round(g13x)
		                g13y = round(g13y-step)
		            elif(gch == 2):
		                g13x = round(g13x)
		                g13y = round(g13y+step)
		            elif(gch == 3):
		                g13x = round(g13x+step)
		                g13y = round(g13y)
		   
		            g13x = float(g13x)
		            g13y = float(g13y)
		            g13pos = (g13x,g13y)
		        
		            if(g13x <  (step-starth) or g13y < (step-startw) or g13x >  (starth-step) or g13y > (startw-step)):
		                g13border = True
		        
		            if(g13border == False):
		                gh13.goto(g13x,g13y) 
		            else:
		                g13border = False

	            if difficulty in god_mode:
		            gch = random.randint(0,4)
		            g14x,g14y = gh14.pos()
		   
		            if(gch == 0):
		                g14x = round(g14x-step)
		                g14y = round(g14y)
		            elif(gch == 1):
		                g14x = round(g14x)
		                g14y = round(g14y-step)
		            elif(gch == 2):
		                g14x = round(g14x)
		                g14y = round(g14y+step)
		            elif(gch == 3):
		                g14x = round(g14x+step)
		                g14y = round(g14y)
		   
		            g14x = float(g14x)
		            g14y = float(g14y)
		            g14pos = (g14x,g14y)
		        
		            if(g14x <  (step-starth) or g14y < (step-startw) or g14x >  (starth-step) or g14y > (startw-step)):
		                g14border = True
		        
		            if(g14border == False):
		                gh14.goto(g14x,g14y) 
		            else:
		                g14border = False

	            if difficulty in god_mode:
		            gch = random.randint(0,4)
		            g15x,g15y = gh15.pos()
		   
		            if(gch == 0):
		                g15x = round(g15x-step)
		                g15y = round(g15y)
		            elif(gch == 1):
		                g15x = round(g15x)
		                g15y = round(g15y-step)
		            elif(gch == 2):
		                g15x = round(g15x)
		                g15y = round(g15y+step)
		            elif(gch == 3):
		                g15x = round(g15x+step)
		                g15y = round(g15y)
		   
		            g15x = float(g15x)
		            g15y = float(g15y)
		            g15pos = (g15x,g15y)
		        
		            if(g15x <  (step-starth) or g15y < (step-startw) or g15x >  (starth-step) or g15y > (startw-step)):
		                g15border = True
		        
		            if(g15border == False):
		                gh15.goto(g15x,g15y) 
		            else:
		                g15border = False

	            if difficulty in god_mode:
		            gch = random.randint(0,4)
		            g16x,g16y = gh16.pos()
		   
		            if(gch == 0):
		                g16x = round(g16x-step)
		                g16y = round(g16y)
		            elif(gch == 1):
		                g16x = round(g16x)
		                g16y = round(g16y-step)
		            elif(gch == 2):
		                g16x = round(g16x)
		                g16y = round(g16y+step)
		            elif(gch == 3):
		                g16x = round(g16x+step)
		                g16y = round(g16y)
		   
		            g16x = float(g16x)
		            g16y = float(g16y)
		            g16pos = (g16x,g16y)
		        
		            if(g16x <  (step-starth) or g16y < (step-startw) or g16x >  (starth-step) or g16y > (startw-step)):
		                g16border = True
		        
		            if(g16border == False):
		                gh16.goto(g16x,g16y) 
		            else:
		                g16border = False

	            if difficulty in god_mode:
		            gch = random.randint(0,4)
		            g17x,g17y = gh17.pos()
		   
		            if(gch == 0):
		                g17x = round(g17x-step)
		                g17y = round(g17y)
		            elif(gch == 1):
		                g17x = round(g17x)
		                g17y = round(g17y-step)
		            elif(gch == 2):
		                g17x = round(g17x)
		                g17y = round(g17y+step)
		            elif(gch == 3):
		                g17x = round(g17x+step)
		                g17y = round(g17y)
		   
		            g17x = float(g17x)
		            g17y = float(g17y)
		            g17pos = (g17x,g17y)
		        
		            if(g17x <  (step-starth) or g17y < (step-startw) or g17x >  (starth-step) or g17y > (startw-step)):
		                g17border = True
		        
		            if(g17border == False):
		                gh17.goto(g17x,g17y) 
		            else:
		                g17border = False

	            if difficulty in god_mode:
		            gch = random.randint(0,4)
		            g18x,g18y = gh18.pos()
		   
		            if(gch == 0):
		                g18x = round(g18x-step)
		                g18y = round(g18y)
		            elif(gch == 1):
		                g18x = round(g18x)
		                g18y = round(g18y-step)
		            elif(gch == 2):
		                g18x = round(g18x)
		                g18y = round(g18y+step)
		            elif(gch == 3):
		                g18x = round(g18x+step)
		                g18y = round(g18y)
		   
		            g18x = float(g18x)
		            g18y = float(g18y)
		            g18pos = (g18x,g18y)
		        
		            if(g18x <  (step-starth) or g18y < (step-startw) or g18x >  (starth-step) or g18y > (startw-step)):
		                g18border = True
		        
		            if(g18border == False):
		                gh18.goto(g18x,g18y) 
		            else:
		                g18border = False

	            if difficulty in god_mode:
		            gch = random.randint(0,4)
		            g19x,g19y = gh19.pos()
		   
		            if(gch == 0):
		                g19x = round(g19x-step)
		                g19y = round(g19y)
		            elif(gch == 1):
		                g19x = round(g19x)
		                g19y = round(g19y-step)
		            elif(gch == 2):
		                g19x = round(g19x)
		                g19y = round(g19y+step)
		            elif(gch == 3):
		                g19x = round(g19x+step)
		                g19y = round(g19y)
		   
		            g19x = float(g19x)
		            g19y = float(g19y)
		            g19pos = (g19x,g19y)
		        
		            if(g19x <  (step-starth) or g19y < (step-startw) or g19x >  (starth-step) or g19y > (startw-step)):
		                g19border = True
		        
		            if(g19border == False):
		                gh19.goto(g19x,g19y) 
		            else:
		                g19border = False

	            if difficulty in god_mode:
		            gch = random.randint(0,4)
		            g20x,g20y = gh20.pos()
		   
		            if(gch == 0):
		                g20x = round(g20x-step)
		                g20y = round(g20y)
		            elif(gch == 1):
		                g20x = round(g20x)
		                g20y = round(g20y-step)
		            elif(gch == 2):
		                g20x = round(g20x)
		                g20y = round(g20y+step)
		            elif(gch == 3):
		                g20x = round(g20x+step)
		                g20y = round(g20y)
		   
		            g20x = float(g20x)
		            g20y = float(g20y)
		            g20pos = (g20x,g20y)
		        
		            if(g20x <  (step-starth) or g20y < (step-startw) or g20x >  (starth-step) or g20y > (startw-step)):
		                g20border = True
		        
		            if(g20border == False):
		                gh20.goto(g20x,g20y) 
		            else:
		                g20border = False
			
	            cho = input("Enter movement A for left, S for down, D for right, W for up \n Type in exit or quit to leave the game")
	            x,y = pt.pos()
	            if(cho == 'a' or cho == 'A'):
	                x = x-step
	            # y = round(y)
	            elif(cho == 's' or cho == 'S'):
	      #  x = round(x)
	                y = y-step
	            elif(cho == 'w' or cho == 'W'):
	    #    x = round(x)
	                y = y+step
	            elif(cho == 'd' or cho =='D'):
	                x = x+step
	            elif(cho == 'exit' or cho == 'quit'):
	            	break

	       # y = round(y)
	            new_pos = (float(x),float(y))
	            
	            for i in range(len(lsc)):
	        
	                if(new_pos == lsc[i]):
	                    border = True
	                    break
	                if((x <  -starth) or (y < -startw) or (x >  starth) or (y > startw)):
	                    border = True
	    
	            #print(new_pos) 
	            if (difficulty == 'easy'):
	            	if(pt.pos()==gh1.pos() or pt.pos()==gh2.pos() or pt.pos()==gh3.pos()or pt.pos()==gh4.pos()):
	            		print("game over")
	            		break
	            if (difficulty == 'medium'):
	            	if(pt.pos()==gh1.pos() or pt.pos()==gh2.pos() or pt.pos()==gh3.pos()or pt.pos()==gh4.pos()or pt.pos()==gh5.pos()or pt.pos()==gh6.pos()):
	            		print("game over")
	            		break
	            if (difficulty == 'hard'):
	            	if(pt.pos()==gh1.pos() or pt.pos()==gh2.pos() or pt.pos()==gh3.pos()or pt.pos()==gh4.pos()or pt.pos()==gh5.pos()or pt.pos()==gh6.pos()or pt.pos()==gh7.pos()or pt.pos()==gh8.pos()or pt.pos()==gh9.pos()or pt.pos()==gh10.pos()):
	            		print("game over")
	            		break
	            if difficulty in god_mode:
	            	if(pt.pos()==gh1.pos() or pt.pos()==gh2.pos() or pt.pos()==gh3.pos()or pt.pos()==gh4.pos()or pt.pos()==gh5.pos()or pt.pos()==gh6.pos()or pt.pos()==gh7.pos()or pt.pos()==gh8.pos()or pt.pos()==gh9.pos()or pt.pos()==gh10.pos()or pt.pos()==gh11.pos()or pt.pos()==gh12.pos()or pt.pos()==gh13.pos()or pt.pos()==gh14.pos()or pt.pos()==gh15.pos()or pt.pos()==gh16.pos()or pt.pos()==gh17.pos()or pt.pos()==gh18.pos()or pt.pos()==gh19.pos()or pt.pos()==gh20.pos()):
	                	print("game over")
	                	break

	            if(border == False):
	                pt.goto(x,y)
	                
	                if(pt.pos()==(starth,0)):
	                    ft.clearstamp((starth,0))
	                    score+=1
	                    break
	                
	                ft.clearstamp(fid[new_pos])
	                count = False 
	                for a in repf:
	                    if (new_pos==a):
	                        count = True
	                        break
	                if(count == False):
	                    score+=1
	                    repf.append(new_pos)
	                else:
	                    count = False
	                        
	                
	            else:
	                border = False
	            #print("pacman pos",pt.pos())

	ft.clearstamp((340.0,0.0))        
	ft.clearstamp((starth,0))

	if (pt.pos()==(starth,0) and score==138):
	    print("CONGRATULATIONS ",Name," YOU WON THE GAME!\nYour score is ",score)
	    
	if (pt.pos()==(starth,0)):
	    print("Thank You for playing ", Name," you finished the game but you did not win\nYour score is ", score)
	
	else:
	    print("Thank You for playing ", Name," your score is ",score)
	ft.clear()
	pt.hideturtle()
	gh1.hideturtle()
	gh2.hideturtle()
	gh3.hideturtle()
	gh4.hideturtle()
	if (difficulty != 'easy'):
		gh5.hideturtle()
		gh6.hideturtle()
	if (difficulty != 'easy') and (difficulty != 'medium'):
		gh7.hideturtle()
		gh8.hideturtle()
		gh9.hideturtle()
		gh10.hideturtle()
	if difficulty in god_mode:
		
		gh11.hideturtle()
		gh12.hideturtle()
		gh13.hideturtle()
		gh14.hideturtle()
		gh15.hideturtle()
		gh16.hideturtle()
		gh17.hideturtle()
		gh18.hideturtle()
		gh19.hideturtle()
		gh20.hideturtle()
	

def restart():
 	print('Play game?')

def menu():
	while True:
		restart()
		choice =input('Enter yes or no').lower()
		if choice == 'yes':
			game()
		elif choice == 'no':
			return False
			print('Click close programme on the GUI to exit')
		else:
			print('Not a correct choice: {}'.format(choice))

menu()
root.mainloop()


#Appendix 1: Code used to derive coordinates to plot points
'''
t = turtle.Turtle()
sc=turtle.Screen()
#sc.bgcolor("black")

H = 860
W = 740
step = 40
sc.setup(H,W)
t.speed("fastest")
#t.pensize(15)
t.pencolor("blue")
h = H-100
w = W-100
w1 = (w-2*step)//(2*step)
t.penup()
t.goto((-h//2 + 2*step),-step)
lsco.append(t.pos())
print(h//step)
print(w1)

t.left(180)
t.pendown()
for i in range(w1+1):
    if(i == 2):
        t.left(90)
    t.forward(step)
    lsco.append(t.pos())
    

t.left(90)
for i in range(h//step  + w1 - 2):
    if(i == h//step - 1):
        t.left(90)
    t.forward(step)
    lsco.append(t.pos())
    

t.left(90)


for i in range(2):
    t.forward(step)
    lsco.append(t.pos())
t.penup()
t.left(90)
t.forward(2*step)
lsco.append(t.pos())
t.pendown()

for i in range(4):
    if (i==2):
        t.right(90)
    t.forward(step)
    lsco.append(t.pos())


print(t.pos())
x,y = t.pos()
x = round(x- 4*step)
y = round(y)
t.penup()
t.goto(x,y)

t.pendown()
lsco.append(t.pos())
t.right(90)
for i in range(3):
    t.forward(step)
    lsco.append(t.pos())
t.right(90)
for i in range(2):
    t.forward(step)
    lsco.append(t.pos())
x,y = t.pos()
x = round(x)
y = round(y-2*step)
t.penup()
t.goto(x,y)

t.pendown()
lsco.append(t.pos())
t.right(90)
for i in range(3):
    t.forward(step)
    lsco.append(t.pos())

x,y = t.pos()
x = round(x- 4*step)
y = round(y+2*step)
t.penup()
t.goto(x,y)

t.pendown()
lsco.append(t.pos())

t.left(180)
for i in range(3):
    t.forward(step)
    lsco.append(t.pos())
t.left(90)
for i in range(2):
    t.forward(step)
    lsco.append(t.pos())

x,y = t.pos()
x = round(x)
y = round(y-2*step)
t.penup()
t.goto(x,y)

t.pendown()
lsco.append(t.pos())
t.left(90)
for i in range(3):
    t.forward(step)
    lsco.append(t.pos())
    
x,y = t.pos()
x = round(x-2*step)
y = round(y+2*step)
t.penup()
t.goto(x,y)
t.pendown()
lsco.append(t.pos())
t.right(90)

for i in range(4):
    if(i == 2):
        t.right(90)
    t.forward(step)
    lsco.append(t.pos())

#upper half

t.penup()
t.goto((-h//2 + 2*step),step)
lsco.append(t.pos())
print(h//step)
print(w1)

t.left(90)
t.pendown()
for i in range(2):
    t.forward(step)
    lsco.append(t.pos())
t.right(90)
for i in range(w1-1):
    t.forward(step)
    lsco.append(t.pos())
t.right(90)
for i in range(h//step - 1 ):
    t.forward(step)
    lsco.append(t.pos())

t.right(90)
for i in range(w1-1):
    t.forward(step)
    lsco.append(t.pos())
t.right(90)


for i in range(2):
    t.forward(step)
    lsco.append(t.pos())
t.penup()
t.right(90)
t.forward(2*step)
lsco.append(t.pos())
t.pendown()

for i in range(2):
    t.forward(step)
    lsco.append(t.pos())
t.left(90)
for i in range(2):
    t.forward(step)
    lsco.append(t.pos())
print(t.pos())
x,y = t.pos()
x = round(x- 4*step)
y = round(y)
t.penup()
t.goto(x,y)

t.pendown()
lsco.append(t.pos())
t.left(90)
for i in range(3):
    t.forward(step)
    lsco.append(t.pos())
t.left(90)
for i in range(2):
    t.forward(step)
    lsco.append(t.pos())
x,y = t.pos()
x = round(x)
y = round(y+2*step)
t.penup()
t.goto(x,y)

t.pendown()
lsco.append(t.pos())
t.left(90)
for i in range(3):
    t.forward(step)
    lsco.append(t.pos())

x,y = t.pos()
x = round(x- 4*step)
y = round(y-2*step)
t.penup()
t.goto(x,y)

t.pendown()
lsco.append(t.pos())

t.left(180)
for i in range(3):
    t.forward(step)
    lsco.append(t.pos())
t.right(90)
for i in range(2):
    t.forward(step)
    lsco.append(t.pos())

x,y = t.pos()
x = round(x)
y = round(y+2*step)
t.penup()
t.goto(x,y)

t.pendown()
lsco.append(t.pos())
t.right(90)
for i in range(3):
    t.forward(step)
    lsco.append(t.pos())
    
x,y = t.pos()
x = round(x-2*step)
y = round(y-2*step)
t.penup()
t.goto(x,y)
t.pendown()
lsco.append(t.pos())
t.left(90)

for i in range(4):
    if(i == 2):
        t.left(90)
    t.forward(step)
    lsco.append(t.pos())

x,y = t.pos()
x = round(x+2*step)
y = round(y)

t.penup()
t.goto(x,y)

t.pendown()
lsco.append(t.pos())

#two long bars

for i in range(6):
    t.forward(step)
    lsco.append(t.pos())

x,y = t.pos()
x = round(x+10*step)
y = round(y)

t.penup()
t.goto(x,y)

t.pendown()
lsco.append(t.pos())
t.left(180)
for i in range(6):
    t.forward(step)
    lsco.append(t.pos())
    
x,y = t.pos()
x = round(x-2*step)
y = round(y-3*step)

t.penup()
t.goto(x,y)
t.pendown()
lsco.append(t.pos())

t.left(90)
t.stamp()
t.penup()
t.forward(step)
t.pendown()
lsco.append(t.pos())
for i in range(4):
    t.forward(step)
    lsco.append(t.pos())


t.penup()
t.forward(step)
t.pendown()
lsco.append(t.pos())
t.stamp()
'''