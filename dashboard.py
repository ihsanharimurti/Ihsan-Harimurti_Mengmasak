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

background_img = PhotoImage(file = f"Assets/dashboard_background.png")
background = canvas.create_image(
    670.0, 375.0,
    image=background_img)

img0 = PhotoImage(file = f"Assets/dashboard_img0.png")

def btn_clicked__next():
    import next

def btn_clicked_soto():
    window.destroy()
    import soto

def btn_clicked_steak():
    window.destroy()
    import steak

def btn_clicked_bakmie():
    import next

def btn_clicked_pasta():
    import next

def btn_clicked_logout():
    window.destroy()
    import login
    window.mainloop()

b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked__next,
    relief = "flat")

b0.place(
    x = 1165, y = 649,
    width = 68,
    height = 24)


img1 = PhotoImage(file = f"Assets/dashboard_img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked_pasta,
    relief = "flat")

b1.place(
    x = 85, y = 522,
    width = 422,
    height = 68)

img2 = PhotoImage(file = f"Assets/dashboard_img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked_bakmie,
    relief = "flat")

b2.place(
    x = 85, y = 433,
    width = 423,
    height = 64)

img3 = PhotoImage(file = f"Assets/dashboard_img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked_steak,
    relief = "flat")

b3.place(
    x = 85, y = 340,
    width = 422,
    height = 63)

img4 = PhotoImage(file = f"Assets/dashboard_img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked_soto,
    relief = "flat")

b4.place(
    x = 85, y = 245,
    width = 422,
    height = 63)

img5 = PhotoImage(file = f"Assets/dashboard_img5.png")


b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked_logout,
    relief = "flat")

b5.place(
    x = 1131, y = 25,
    width = 107,
    height = 33)

window.resizable(False, False)
window.mainloop()
