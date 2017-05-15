""" Utils for probably the most stupid interface ever designed """

import os
from assignment import Assignment 
from organizer import Organizer
import pickle 

# Splash Screen, and check for save data
def start():
	clearScr()

	print("J-SUD's crappy organizer prototype\n v0.0.0.0.001")

	# If there are saves and we want to use them
	if os.path.exists("saves/data.dat"):
		inp = input("Use saved data? (will overwrite if no) y/n: ")
		if inp == "y":
			clearScr()
			with open("saves/data.dat", "r+b") as f:
				return pickle.load(f)
	# If there are no saves
	else: 
		input("Press enter to continue:")

	# No saves or user doesn't care
	clearScr()
	org = Organizer()
	return org
	

# This is the main router for choices, and returns when exit is called
def mainMenu(org):
	clearScr()
	inp = menuPrompt()
	if inp == "1":
		addAssig(org, "", "")
	elif inp == "2":
		remAssig(org)
	elif inp == "3":
		view(org)
	elif inp == "4":
		save(org)
	elif inp == "5":
		print("Goodbye, my dude")
		return True
	else:
		print("\nInvalid input! \n(numbers only!)")
		input("enter to continue")
		clearScr()
	
	return False


# prompt input for menu
def menuPrompt():
	print("Select a number corresponding to an option \n" + 
			"1: Add assignment \n" + 
			"2: Remove assignment \n" + 
			"3: View assignments \n" + 
			"4: Save File \n" +
			"5: Quit without saving \n")
	return input("Enter your choice: ")


# Add an assignment
def addAssig(org, title, desc):

	if title == "":
		title = input("Enter a title: ")

	if desc == "":
		desc = input("Enter a description: ")

	time = input("Enter a time (? for format instructions): ")
	if time == "?":
		timeFormatDisplay()
		clearScr()
		addAssig(org, title, desc)
		return

	try: 
		time = int(time)
	except ValueError:
		print("Time needs to be an int")
		addAssig(org, title, desc)
		return	

	org.addAssignment(Assignment(title, desc, time))

# Display correct time format
def timeFormatDisplay():
	clearScr()
	print("Come back later lol. \n Enter any int for now, eventually there'll be actual dates")
	input("Press enter to return")

def remAssig(org):
	input("You actually can't do that yet lol, enter to return")

# Print all assignments
def view(org):
	clearScr()
	print("Assignments in order of due-date:")
	print("---------------------------------")
	backup = []
	for i in range(org.size):
		a = org.popAssignment()
		backup.append(a)
		print("Title: {0} \nDue: {1}".format(a.title, a.due))
		print("    {0}".format(a.text))
		print("---------------------------------")

	input("press enter to return")
	for b in backup:
		org.addAssignment(b)


# Use pickle to dump object data to file
def save(org):
	if not os.path.isdir("saves/"):
		os.mkdir("saves/")
	
	if not os.path.exists("saves/data.dat"):
		with open("saves/data.dat", "wb") as f:
			pickle.dump(org, f)
	else:
		with open("saves/data.dat", "r+b") as f:
			pickle.dump(org, f)
		
	print("Saved!")
	clearScr()


# Simple clear screen function
def clearScr():
	os.system('clear')
