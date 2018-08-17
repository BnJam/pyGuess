from tkinter import * # GUI
import random		  # random library

randInt = random.randint(1,20) # choose random number
guess = 0 # set number of guesses

# Quit button functionality
def close_window(): 
	window.destroy()

# Guessing functionality
def makeGuess():
	global guess # global to access and reassign value to guess
	# guess is too low
	if int(user_input.get()) < randInt and guess < 6:
		guess += 1
		user_input.config({"background":"yellow"})
		label2 = Label(frame3, text="Too low...")
		label2.pack()
	# guess is too high
	if int(user_input.get()) > randInt and guess < 6:
		guess += 1
		user_input.config({"background":"red"})
		label2 = Label(frame3, text="Too high...")
		label2.pack()
	# guess is right
	if int(user_input.get()) == randInt and guess < 6:
		user_input.config({"background":"green"})
		label2 = Label(frame3, text="You Guessed the Number! " + str(randInt))
		label2.pack()
	# running out of guesses
	if guess == 6:
		label2 = Label(frame3, text="You ran out of guesses! Answer: " + str(randInt))
		label2.pack()		
	

# creating Tkinter GUI object
window = Tk()
# user input frame
frame = Frame(window)
frame.pack()
# button frame
frame2 = Frame(window)
frame2.pack()
#output ftrame
frame3 = Frame(window)
frame3.pack()
# window title
window.title("Guess.py")

# user input frame
label1 = Label(frame, text="Make Guess: ")
label1.pack(side=LEFT)
user_input = Entry(frame, bd=5)
user_input.pack(side=RIGHT)

# button frame
quitButton = Button (frame2, text = "Quit", command = close_window)
quitButton.pack(side=RIGHT)
guessButton = Button(frame2, text = "Guess", command = makeGuess)
guessButton.pack(side=LEFT)

window.lift()
window.mainloop()


