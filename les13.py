import tkinter as tk


def move_by_keys(event):
    info_coords = canvas.coords(oval)
    x = info_coords[0]
    y = info_coords[1]
    label.config(text=str(x) + " " + str(y))

    if event.keysym == 'Up':
        canvas.move(oval, 0, -50)
    elif event.keysym == 'Down':
        canvas.move(oval, 0, 50)
    elif event.keysym == 'Left':
        canvas.move(oval, -50, 0)
    elif event.keysym == 'Right':
        canvas.move(oval, 50, 0)


win = tk.Tk()
label = tk.Label(win, text="Петров Кирилл")
label.pack()
canvas = tk.Canvas(win, bg="#fff", width=400, height=400)
#oval = canvas.create_oval((300, 300), (400, 400), fill="purple")

for i in range(1, 8):
    canvas.create_line((0, 50*i), (400, 50*i))
    canvas.create_line((50*i, 0), (50*i, 400))


for i in range(0, 4, 1):
    canvas.create_oval((100*i, 0), (50+100*i, 50), fill="red")
    canvas.create_oval((50+100*i, 50), (100+100*i, 100), fill="red")
    oval = canvas.create_oval((100*i, 100), (50+100*i, 150), fill="red")

    canvas.create_oval((50 + 100 * i, 250), (100 + 100 * i, 300), fill="black")
    canvas.create_oval((100 * i, 300), (50 + 100 * i, 350), fill="black")
    canvas.create_oval((50 + 100 * i, 350), (100 + 100 * i, 400), fill="black")



canvas.pack()
win.bind("<KeyPress>", move_by_keys)
win.mainloop()
