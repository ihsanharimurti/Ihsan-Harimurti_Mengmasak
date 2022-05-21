import mysql.connector
from tkinter import *

mydb=mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database="login_ta"
)

global n1
global n2

def btn_clicked():
    mycursor=mydb.cursor()
    username= n1.get()
    password= n2.get()
    sql = "SELECT * FROM userdata WHERE username = %s AND password = %s"
    mycursor.execute(sql, [(username), (password)])
    cekkredensial = mycursor.fetchall()
    if cekkredensial:
        print("berhasil")
    else:
        print("gagal")
    print("Button Clicked")


window = Tk()
window.title('Mengmasak')
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

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    693.5, 364.0,
    image=background_img)

canvas.create_text(
    239.5, 274.5,
    text = "Sign Into",
    fill = "#393939",
    font = ("Poppins-Bold", int(62.0)))

canvas.create_text(
    205.0, 343.5,
    text = "Your Account",
    fill = "#393939",
    font = ("Poppins-Bold", int(30.0)))

canvas.create_text(
    282.5, 130.0,
    text = "Mengmasak",
    fill = "#393939",
    font = ("Poppins-SemiBold", int(32.0)))

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    313.5, 503.0,
    image = entry0_img)

n2 = StringVar()
entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    textvariable=n2,
    show='*',
    highlightthickness = 0)

entry0.place(
    x = 105.0, y = 484,
    width = 417.0,
    height = 36)

canvas.create_text(
    131.0, 475.0,
    text = "Password",
    fill = "#203060",
    font = ("Poppins-Regular", int(12.0)))

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    313.5, 425.0,
    image = entry1_img)
n1 = StringVar()
entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    textvariable=n1,
    highlightthickness = 0)

entry1.place(
    x = 105.0, y = 406,
    width = 417.0,
    height = 36)

canvas.create_text(
    133.0, 394.0,
    text = "Username",
    fill = "#203060",
    font = ("Poppins-Regular", int(12.0)))

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 100, y = 630,
    width = 427,
    height = 38)

window.resizable(False, False)
window.mainloop()
