from tkinter import *
import random

# Generate a random number between 1 and 100 as the secret number
secret = random.randint(1, 100)

# Function to check the user's guess against the secret number
def check_guess():
    guess = int(number.get())
    
    # Compare the guess with the secret number and update the result_label accordingly
    if guess == secret:
        result_label.config(text="WINNER !!")
    elif guess < secret:
        result_label.config(text="Little more !")
    else:
        result_label.config(text="Little less !")

# Create the main window using Tkinter
window = Tk()
window.title("Guess the number !")

# Label to instruct the user to guess a number between 1 and 100
Label(window, text="Guess a number between 1 and 100").pack()

# Entry widget to allow the user to input their guess
number = Entry(window)
number.pack()

# Button to trigger the check_guess function when clicked
Button(window, text="check", command=check_guess).pack()

# Label to display the result of the guess (WINNER, Little more, Little less)
result_label = Label(window, text="")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
