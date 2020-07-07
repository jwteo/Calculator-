import tkinter as tk

height = 550
width = 420


def buttons_pressed(item_selected):
    global operator

    if item_selected == "C": # CLEAR BUTTON
        clear(operator)

    if item_selected == "=":
        evaluation(operator)

    if item_selected == "x":
        operations(item_selected)

    if item_selected == "^":
        operations(item_selected)

    if item_selected != "C" and item_selected != "=" and item_selected != 'x' and item_selected != "^":
        operations(item_selected)

def clear(elements):
    global operator
    operator = ""  # delete previous entries
    label["text"] = ""

def operations(item_selected):
    global operator

    # multiplication
    if item_selected == "x":
        operator += str("*")
        label["text"] += str("x")

    # 'to the power of', not XOR logic gate
    if item_selected == "^":
        operator += str("**")
        label["text"] += str("^")

    # for operations such as "+", "-", "/", "//"
    if item_selected != "C" and item_selected != "=" and item_selected != 'x' and item_selected != "^":
        operator += str(item_selected)
        label["text"] += str(item_selected)

def evaluation(elements):
    global operator
    label["text"] = str(eval(elements))
    operator = str(eval(elements))


root = tk.Tk()
root.title('Calculator')

display = ""
operator = ""

canvas = tk.Canvas(root, height=height, width=width, bg="#800000")  # specify size of the calculator
canvas.pack()

# Creating the display screen for the arithmetic operations and numbers
frame = tk.Frame(root, relief='sunken', borderwidth=6)
frame.place(height=70, width=332, anchor='n', relx=0.5, rely=0.06)

label = tk.Label(frame, font=('Courier', '30'), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

# Creating all the buttons of the calculator
# 1st Row
buttonA = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="C", font=('Courier', '43'),
                    command=lambda: buttons_pressed("C"))
buttonA.place(height=80, width=83, relx=0.108, rely=0.2)

buttonB = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="x^y", font=('Courier', '30'),
                    command=lambda: buttons_pressed("^"))
buttonB.place(height=80, width=83, relx=0.304, rely=0.2)

buttonC = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="//", font=('Courier', '43'),
                    command=lambda: buttons_pressed("//"))
buttonC.place(height=80, width=83, relx=0.50002, rely=0.2)

buttonD = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="%", font=('Courier', '43'),
                    command=lambda: buttons_pressed("%"))
buttonD.place(height=80, width=83, relx=0.696, rely=0.2)

# 2nd Row
buttonE = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="1", font=('Courier', '43'),
                    command=lambda: buttons_pressed(1))
buttonE.place(height=80, width=83, relx=0.108, rely=0.36)

buttonF = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="2", font=('Courier', '43'),
                    command=lambda: buttons_pressed(2))
buttonF.place(height=80, width=83, relx=0.304, rely=0.36)

buttonG = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="3", font=('Courier', '43'),
                    command=lambda: buttons_pressed(3))
buttonG.place(height=80, width=83, relx=0.50002, rely=0.36)

buttonH = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="+", font=('Courier', '43'),
                    command=lambda: buttons_pressed("+"))
buttonH.place(height=80, width=83, relx=0.696, rely=0.36)

# 3rd Row
buttonI = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="4", font=('Courier', '43'),
                    command=lambda: buttons_pressed(4))
buttonI.place(height=80, width=83, relx=0.108, rely=0.518)

buttonJ = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="5", font=('Courier', '43'),
                    command=lambda: buttons_pressed(5))
buttonJ.place(height=80, width=83, relx=0.304, rely=0.518)

buttonK = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="6", font=('Courier', '43'),
                    command=lambda: buttons_pressed(6))
buttonK.place(height=80, width=83, relx=0.50002, rely=0.518)

buttonL = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="-", font=('Courier', '43'),
                    command=lambda: buttons_pressed("-"))
buttonL.place(height=80, width=83, relx=0.696, rely=0.518)

# 4th Row
buttonM = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="7", font=('Courier', '43'),
                    command=lambda: buttons_pressed(7))
buttonM.place(height=80, width=83, relx=0.108, rely=0.677)

buttonN = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="8", font=('Courier', '43'),
                    command=lambda: buttons_pressed(8))
buttonN.place(height=80, width=83, relx=0.304, rely=0.677)

buttonO = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="9", font=('Courier', '43'),
                    command=lambda: buttons_pressed(9))
buttonO.place(height=80, width=83, relx=0.50002, rely=0.677)

buttonP = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="x", font=('Courier', '43'),
                    command=lambda: buttons_pressed("x"))
buttonP.place(height=80, width=83, relx=0.696, rely=0.677)

# 5th Row
buttonQ = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="0", font=('Courier', '43'),
                    command=lambda: buttons_pressed(0))
buttonQ.place(height=80, width=83, relx=0.108, rely=0.834)

buttonR = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text=".", font=('Courier', '43'),
                    command=lambda: buttons_pressed("."))
buttonR.place(height=80, width=83, relx=0.304, rely=0.834)

buttonS = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="=", font=('Courier', '43'),
                    command=lambda: buttons_pressed("="))
buttonS.place(height=80, width=83, relx=0.50002, rely=0.834)

buttonT = tk.Button(root, bg="#D3D3D3", relief='ridge', borderwidth=3, text="/", font=('Courier', '43'),
                    command=lambda: buttons_pressed("/"))
buttonT.place(height=80, width=83, relx=0.696, rely=0.834)

root.mainloop()
