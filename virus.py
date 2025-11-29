from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Virus scanner")
window.geometry("300x200")

# funcation to display warning message
# messagebox.showwarning("Window name", "Text to be displayed")
def msg():
    messagebox.showwarning("Virus Alert!", "Virus detected on your system!")

# create a button to trigger the warning message
btn = Button(text="Scan for Virus", command=msg, bg="#00FF26", fg="black")
btn.pack()

# start the main loop
window.mainloop()
