import tkinter as tk
import random

# Function that performs the dice roll
def dice_roll(dice, sides):
    roll = []
    for i in range(dice):
        face = random.randint(1, sides)
        roll.append(face)
    return roll

# Function to handle the button click event
def roll_dice():
    # Get the number of dice and sides from the entry fields
    dice = int(dice_entry.get())
    sides = int(sides_entry.get())

    # Validation: check if the number of dice and sides are valid
    if dice <= 0:
        result_label.config(text="Must have at least one dice!")
        return
    if sides <= 0:
        result_label.config(text="Must have at least one side!")
        return

    # Perform the dice roll
    roll = dice_roll(dice, sides)

    # Display the result
    result_label.config(text=f"Roll results: {roll}")

# Set up the main window
root = tk.Tk()
root.title("Dice Roller")

# Set up the UI elements
dice_label = tk.Label(root, text="Number of Dice:")
dice_label.pack()

dice_entry = tk.Entry(root)
dice_entry.pack()

sides_label = tk.Label(root, text="Number of Sides (default is 6):")
sides_label.pack()

sides_entry = tk.Entry(root)
sides_entry.insert(0, "6")  # Default to 6 sides
sides_entry.pack()

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.pack()

result_label = tk.Label(root, text="Roll results will appear here.")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
