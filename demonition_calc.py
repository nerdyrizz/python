from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# setting up main window
root = Tk()
root.title("Demonition Calculator")
root.geometry("650x400")
root.configure(bg="#ff7ccd")

# adding widgets in the main window
Upload = Image.open("calc.png")
Upload = Upload.resize((300, 300))
img = ImageTk.PhotoImage(Upload)
label = Label(root, image = img, bg="#ff7ccd")
label.place(x=180, y=20)    

label1 = Label(root, text="Demonition Calculator", font=("Arial", 20), bg="#ff7ccd")
label1.place(relx=0.5, y=340, anchor="center")


# function to display a message box and preceed if ok is pressed
def msg():
    Msgbox = messagebox.showinfo("Demonition Calculator", "Welcome to Demonition Calculator! Click OK to proceed.")
    if Msgbox == "ok":
        topwin()

    
# adding buttons to the main window
btn = Button(root, text="Start Calculation", command=msg, bg="#710536", fg="white", font=("Arial", 14))
btn.place(x=260, y=360)

# function to open a new top level window
def topwin():
    top = Toplevel()
    top.title("Calculation Window")
    top.geometry("650x350+50+50")
    top.configure(bg="#ff7ccd")

    label = Label(top, text="Enter the total amount", font=("Arial", 16), bg="#ff7ccd")
    entry = Entry(top, font=("Arial", 14), width=20)
    lbl = Label(top, text="These are the notes for each demoniton", font=("Arial", 16), bg="#ff7ccd")

    l1 = Label(top, text="2000", font=("Arial", 14), bg="#ff7ccd")
    l2 = Label(top, text="500", font=("Arial", 14), bg="#ff7ccd")
    l3 = Label(top, text="100", font=("Arial", 14), bg="#ff7ccd")

    t1 = Entry(top, font=("Arial", 14), width=10)
    t2 = Entry(top, font=("Arial", 14), width=10)
    t3 = Entry(top, font=("Arial", 14), width=10)

    def calculator():
        global amount
        amount = int(entry.get())
        note2000 = amount // 2000
        amount %= 2000
        note500 = amount // 500
        amount %= 500
        note100 = amount // 100

        t1.delete(0, END)
        t2.delete(0, END)  
        t3.delete(0, END)

        t1.insert(0, str(note2000))
        t2.insert(0, str(note500))
        t3.insert(0, str(note100))
    calc_btn = Button(top, text="Calculate", command=calculator, bg="#710536", fg="white", font=("Arial", 14))
    calc_btn.place(x=270, y=220)
    # placing widgets in the top level window
    label.place(x=220, y=20)    
    entry.place(x=250, y=60)
    lbl.place(x=200, y=100)
    l1.place(x=200, y=140)
    l2.place(x=300, y=140)
    l3.place(x=400, y=140)
    t1.place(x=200, y=180)
    t2.place(x=300, y=180)
    t3.place(x=400, y=180)

    top.mainloop()

root.mainloop()