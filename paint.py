from tkinter import *

current_x, current_y = 0, 0


def locate_cursor(event):
    global current_x, current_y
    current_x, current_y = event.x, event.y
    print(current_x, current_y)


def draw_line(event):
    global current_x, current_y
    canvas.create_line(current_x, current_y, event.x, event.y)


window = Tk()

window.title('PythonPaint')
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

canvas = Canvas(window)

canvas.grid(row=0, column=0, stick='nsew')

canvas.bind('<Button-1>', locate_cursor)
canvas.bind('<B1-Motion>', draw_line)

window.mainloop()

