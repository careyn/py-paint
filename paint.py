from tkinter import *

color = 'black'

current_x, current_y = 0, 0


def locate_cursor(event):
    global current_x, current_y
    current_x, current_y = event.x, event.y


def show_color(new_color):
    global color

    color = new_color


def draw_line(event):
    global current_x, current_y
    canvas.create_line((current_x, current_y, event.x, event.y), fill=color)
    current_x, current_y = event.x, event.y


def new_canvas():
    canvas.delete('all')
    color_choice()


window = Tk()

window.title('PythonPaint')
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

canvas = Canvas(window)

canvas.grid(row=0, column=0, stick='nsew')

menu_bar = Menu(window)
window.config(menu=menu_bar)
submenu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(label='File', menu=submenu)
submenu.add_command(label='New Canvas', command=new_canvas)

canvas.bind('<Button-1>', locate_cursor)
canvas.bind('<B1-Motion>', draw_line)


def color_choice():
    opt = canvas.create_rectangle((10, 10, 30, 30), fill='black')
    canvas.tag_bind(opt, '<Button-1>', lambda x: show_color('black'))

    opt = canvas.create_rectangle((10, 40, 30, 60), fill='gray')
    canvas.tag_bind(opt, '<Button-1>', lambda x: show_color('gray'))

    opt = canvas.create_rectangle((10, 70, 30, 90), fill='white')
    canvas.tag_bind(opt, '<Button-1>', lambda x: show_color('white'))

    opt = canvas.create_rectangle((10, 100, 30, 120), fill='brown4')
    canvas.tag_bind(opt, '<Button-1>', lambda x: show_color('brown4'))

    opt = canvas.create_rectangle((10, 130, 30, 150), fill='red')
    canvas.tag_bind(opt, '<Button-1>', lambda x: show_color('red'))

    opt = canvas.create_rectangle((10, 160, 30, 180), fill='orange')
    canvas.tag_bind(opt, '<Button-1>', lambda x: show_color('orange'))

    opt = canvas.create_rectangle((10, 190, 30, 210), fill='yellow')
    canvas.tag_bind(opt, '<Button-1>', lambda x: show_color('yellow'))

    opt = canvas.create_rectangle((10, 220, 30, 240), fill='green')
    canvas.tag_bind(opt, '<Button-1>', lambda x: show_color('green'))

    opt = canvas.create_rectangle((10, 250, 30, 270), fill='blue')
    canvas.tag_bind(opt, '<Button-1>', lambda x: show_color('blue'))

    opt = canvas.create_rectangle((10, 280, 30, 300), fill='purple')
    canvas.tag_bind(opt, '<Button-1>', lambda x: show_color('purple'))


color_choice()


window.mainloop()

