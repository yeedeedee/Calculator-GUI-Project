from tkinter import *


equation = ""
def Calculate(event):
  global equation
  character = event.widget.cget("text")
  if character == "=":
    answer = eval(equation)
    equation = str(answer)
    screen.set(equation)
  elif character == "C":
    equation = ""
    screen.set(equation)
  elif character == "CE":
    equation = equation[0:-1]
    screen.set(equation)
  else:
    equation = equation + character
    screen.set(equation)
    

root = Tk()
root.title("Calculator")
root.configure(bg = "teal")


screen = StringVar()

display = Entry(root, bg = "black", fg = "white" , textvariable= screen)
display.grid(row = 0, column = 0, columnspan=4, sticky = "we", ipady=9)

button7 = Button(root, text = "7", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button7.grid(row=1, column = 0)
button7.bind("<Button-1>", Calculate)

button8 = Button(root, text = "8", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button8.grid(row=1, column = 1)
button8.bind("<Button-1>", Calculate)

button9 = Button(root, text = "9", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button9.grid(row=1, column = 2)
button9.bind("<Button-1>", Calculate)

button4 = Button(root, text = "4", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button4.grid(row=2, column = 0)
button4.bind("<Button-1>", Calculate)

button5 = Button(root, text = "5", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button5.grid(row=2, column = 1)
button5.bind("<Button-1>", Calculate)

button6 = Button(root, text = "6", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button6.grid(row=2, column = 2)
button6.bind("<Button-1>", Calculate)

button1 = Button(root, text = "1", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button1.grid(row=3, column = 0)
button1.bind("<Button-1>", Calculate)

button2 = Button(root, text = "2", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button2.grid(row=3, column = 1)
button2.bind("<Button-1>", Calculate)

button3 = Button(root, text = "3", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button3.grid(row=3, column = 2)
button3.bind("<Button-1>", Calculate)

button0 = Button(root, text = "0", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button0.grid(row=4, column = 0)
button0.bind("<Button-1>", Calculate)

button_add = Button(root, text = "+", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button_add.grid(row=1, column = 3)
button_add.bind("<Button-1>", Calculate)

button_subtract = Button(root, text = "-", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button_subtract.grid(row=2, column = 3)
button_subtract.bind("<Button-1>", Calculate)

button_multiply = Button(root, text = "*", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button_multiply.grid(row=3, column = 3)
button_multiply.bind("<Button-1>", Calculate)

button_divide = Button(root, text = "/", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button_divide.grid(row=4, column = 2)
button_divide.bind("<Button-1>", Calculate)

button_decimal = Button(root, text = ".", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button_decimal.grid(row=4, column = 1)
button_decimal.bind("<Button-1>", Calculate)

button_equal = Button(root, text = "=", width = 4, height = 2, borderwidth = 6, relief=RAISED)
button_equal.grid(row=4, column = 3)
button_equal.bind("<Button-1>", Calculate)

button_delete = Button(root, text = "CE", width = 8, height = 2, borderwidth = 6, relief=RAISED)
button_delete.grid(row=5, column = 0, columnspan = 2, sticky="we")
button_delete.bind("<Button-1>", Calculate)

button_clear_all = Button(root, text = "C", width = 8, height = 2, borderwidth = 6, relief=RAISED)
button_clear_all.grid(row=5, column = 2, columnspan = 2, sticky="we")
button_clear_all.bind("<Button-1>", Calculate)

root.mainloop()
