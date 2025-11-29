from tkinter import *
window = Tk()
window.title("click counter")
window.geometry("100x100")

# event hander for keypress
def handle_keypress(event):
    """print the character associated with the key pressed"""
    print(event.char)

# bind keypress event to the handler
window.bind("<Key>", handle_keypress)

# event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")

# create a button
btn = Button(text = "Click me")
btn.pack()

# bind button click event to the handler
btn.bind("<Button-1>", handle_click)

# start the main loop
window.mainloop()