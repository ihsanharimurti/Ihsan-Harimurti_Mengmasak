from tkinter import *

window = Tk()
window.geometry("1366x768")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

def btn_clicked():
    window.destroy()
    import login

background_img = PhotoImage(file = f"Assets/welcome_background.png")
background = canvas.create_image(
    683.0, 384.0,
    image=background_img)

img0 = PhotoImage(file = f"Assets/welcome_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 577, y = 501,
    width = 212,
    height = 61)

window.resizable(False, False)
window.mainloop()
