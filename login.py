from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb=mysql.connector.connect(
 host="localhost",
 user="root",
 password="Darkknight114!",
 database="login_ta"
)

def btn_clicked_login():
    mycursor=mydb.cursor()
    username= n1.get()
    password= n2.get()
    sql = "SELECT * FROM userdata WHERE username = %s AND password = %s"
    mycursor.execute(sql, [(username), (password)])
    cekkredensial = mycursor.fetchall()
    if cekkredensial:
        window.destroy()
        import dashboard
    else:
        messagebox.showinfo("Error", "Please provide correct username and password!!")                
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

background_img = PhotoImage(file = f"Assets/login_background.png")
background = canvas.create_image(
    866.5, 383.0,
    image=background_img)

entry0_img = PhotoImage(file = f"Assets/login_img_textBox0.png")
entry0_bg = canvas.create_image(
    313.5, 503.0,
    image = entry0_img)

n2=StringVar()
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

entry1_img = PhotoImage(file = f"Assets/login_img_textBox1.png")
entry1_bg = canvas.create_image(
    313.5, 425.0,
    image = entry1_img)

n1=StringVar()
entry1 = Entry(
    bd = 0,
    bg = "#ffffff",
    textvariable=n1,
    highlightthickness = 0)

entry1.place(
    x = 105.0, y = 406,
    width = 417.0,
    height = 36)

img0 = PhotoImage(file = f"Assets/login_img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked_login,
    relief = "flat")

b0.place(
    x = 100, y = 630,
    width = 427,
    height = 38)

window.resizable(False, False)
window.mainloop()