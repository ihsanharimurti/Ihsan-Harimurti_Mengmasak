from tkinter import *

window = Tk()

window.geometry("1366x768")
window.configure(bg = "#73777b")
canvas = Canvas(
    window,
    bg = "#73777b",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

def btn_clicked_dashboard():
    window.destroy()
    import dashboard

def btn_clicked_logout():
    window.destroy()
    import login

background_img = PhotoImage(file = f"Assets/steak_background.png")
background = canvas.create_image(
    683.0, 384.0,
    image=background_img)

img0 = PhotoImage(file = f"Assets/steak_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked_dashboard,
    relief = "flat")

b0.place(
    x = 583, y = 718,
    width = 200,
    height = 33)

img1 = PhotoImage(file = f"Assets/steak_img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked_logout,
    relief = "flat")

b1.place(
    x = 1144, y = 34,
    width = 107,
    height = 33)

window.resizable(False, False)
window.mainloop()
