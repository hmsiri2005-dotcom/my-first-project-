from tkinter import *

# Create main window
root = Tk()
root.title("Calculator")
root.geometry("320x450")
root.resizable(False, False)

# Entry box
entry = Entry(root, width=20, font=("Arial", 24), bd=10, relief=RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Function to click button
def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(num))

# Function to clear
def clear():
    entry.delete(0, END)

# Function to calculate
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=7, height=3, font=("Arial",14),
               command=equal).grid(row=row, column=col, padx=5, pady=5)
    else:
        Button(root, text=text, width=7, height=3, font=("Arial",14),
               command=lambda t=text: click(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
Button(root, text="C", width=32, height=2, font=("Arial",14),
       command=clear, bg="red", fg="white").grid(row=5, column=0, columnspan=4, pady=5)

root.mainloop()