#Python 3.10.6
#Pyautogui version: 0.9.53
#
import pyautogui


pyautogui.alert("Hello :)")


#0,0       X increases -->
#+---------------------------+
#|                           | Y increases
#|                           |     |
#|   1920 x 1080 screen      |     |
#|                           |     V
#|                           |
#|                           |
#+---------------------------+ 1919, 1079

#right click
import random
import time
def plsClick():
	time.sleep(random.randint(1,100)/100)
	pyautogui.click()

def plsRightClick():
	time.sleep(random.randint(1,100)/100)
	pyautogui.click(button='right')

#Regular double click
def plsDoubleClick():
	time.sleep(random.randint(1,100)/100)
	pyautogui.doubleClick()
		

#Moves the mouse realistically
def plsMove(intPassed1, intPassed2):
	intRandom = random.randrange(3)
	if intRandom == 0:
		intRandSpeed1 = 500
		intRandSpeed2 = 650 
	elif intRandom == 1:
		intRandSpeed1 = 125
		intRandSpeed2 = 250
	elif intRandom == 2:
		intRandSpeed1 = 250
		intRandSpeed2 = 500
	elif intRandom == 3:
		intRandSpeed1 = 125
		intRandSpeed2 = 650
	int1 = 0
	int2 = 0
	intVar1 = 1
	intVar2 = 1
	if intPassed1 < 0: intVar1 = -1
	if intPassed2 < 0: intVar2 = -1
	
	while intPassed1 != int1 or intPassed2 != int2:
		intRandom = random.randint(1,2)
		if intRandom == 1 and int1 != intPassed1:
			#print(f"X: {pyautogui.position()}")
			int1 += intVar1
			pyautogui.move(1,0)
		elif intRandom == 2 and int2 != intPassed2:
			#print(f"Y: {pyautogui.position()}")
			int2 += intVar2
			pyautogui.move(0,1)
		
		#backstory to this: apparently pyautogui takes too long to move so I had to comment out this section, if it becomes more efficient uncomment the line of code below, it is based on the following: 2203 pixels 5 to 6 seconds when slow, 1.25 to 2 seconds fast.
		#time.sleep((random.randint(intRandSpeed1, intRandSpeed2)/100)/2203)
				
		#this is the current fix for the issue stated
		time.sleep(random.randint(intRandSpeed1,intRandSpeed2)/(650*20))

#Move to a specific spot on the screen like a human		
def plsMoveTo(intPassed1, intPassed2):
	currentMouseX, currentMouseY = pyautogui.position()
	plsMove(intPassed1 - currentMouseX, intPassed2 - currentMouseY)


#intPassed1 = X for left upper bound, intPassed2 = Y for left upper bound
#intPassed3 = X for right lower bound, intPassed4 = Y for lower right bound
def plsMoveToBox(intPassed1, intPassed2, intPassed3, intPassed4):
	plsMove(random.randint(intPassed1, intPassed3), random.randint(intPassed2, intPassed4)) 

#plsDetermineXY made for easier location of pixels
def plsDetermineXY(intPassed):
	arr1 = []
	for int1 in range(intPassed):
		intCounter1 = time.time()
		while time.time() - intCounter1 < 90:
			arr2 = []
			for int2 in range(5):
				arr2.append(pyautogui.position())
				#print(pyautogui.position())
				time.sleep(1)
			set1 = set([x for x in arr2 if arr2.count(x) > 1])
			if len(set1) == 1: break
		arr1.append(list(set1)[0])
		print(list(set1)[0])	
	return arr1

