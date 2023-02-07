from tkinter import *
from tkinter import messagebox

import mysql.connector #pip install mysql-connector-python
import bcrypt #pip install bcrypt

def database_connect():
    connect = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "database_name"
    )
    return connect

def login_validation():
    connect = database_connect()
    username = get_username_login.get()
    password = get_password_login.get()
    password_encode = password.encode("utf-8")
    cursor = connect.cursor()
    sql = "SELECt * FROM accounts WHERE account_username = '%s'" % (username)
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None :
        messagebox.showwarning("System", "Username not found")
    else:
        password_hash = result[2]
        password_hash_encode = password_hash.encode("utf-8")
        validation = bcrypt.checkpw(password_encode, password_hash_encode)
        if validation :

            messagebox.showinfo("System", "Login Success")
        else:
            messagebox.showwarning("System", "Wrong Password")

def register_validation():
    connect = database_connect()
    username = get_username_register.get()
    password = get_password_register.get()
    password_encode = password.encode("utf-8")
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password_encode, salt)
    cursor = connect.cursor()
    sql = "SELECt * FROM accounts WHERE account_username = '%s'" % (username)
    cursor.execute(sql)
    result = cursor.fetchone()
    if result == None :
        sql = "INSERT INTO accounts (account_username, account_password, account_status) VALUES (%s, %s, %s)"
        values = (username, password_hash, 0)
        cursor.execute(sql, values)
        connect.commit()
        messagebox.showinfo("System", "Register Success")
        back()
    else:
        messagebox.showwarning("System", "This username already exists")
    
def back():
    screen_register.destroy()
    screen_login.deiconify()
    
def reigster_screen():
    screen_login.withdraw()
    global screen_register
    screen_register = Toplevel(screen_login)
    width = 400
    height = 330 #(widget_amount * sum_widget_height) + (widget_amount * (sum(widget_height/2)))
    screen_window_width = screen_register.winfo_screenwidth()
    screen_window_height = screen_register.winfo_screenheight()
    x_axis = int((screen_window_width/2) - (width/2))
    y_axis = int((screen_window_height/2) - (height/2))
    screen_register.geometry(f"{width}x{height}+{x_axis}+{y_axis}")
    screen_register.title("Register")
    screen_register.configure(background="#292b2c")

    #Label Header
    lbl_header = Label(screen_register, text="Register", font=("Arial",18), bg="#292b2c", fg="#f7f7f7")
    lbl_header_width = 100
    lbl_header_height = 30
    lbl_header_x_axis = int((width/2)-(lbl_header_width/2))
    lbl_header_y_axis = (lbl_header_height//2)
    lbl_header.place(width=lbl_header_width,height=lbl_header_height,x=lbl_header_x_axis,y=lbl_header_y_axis)

    #Label Username
    lbl_username = Label(screen_register, text="Username", font=("Arial",16), bg="#292b2c", fg="#f7f7f7")
    lbl_username_width = 200
    lbl_username_height = 30
    lbl_username_x_axis = int((width/2)-(lbl_username_width/2))
    lbl_username_y_axis = lbl_header_y_axis + lbl_username_height + (lbl_username_height//2)
    lbl_username.place(width=lbl_username_width,height=lbl_username_height,x=lbl_username_x_axis,y=lbl_username_y_axis)

    #Entry Username
    global get_username_register
    global entry_username_register
    get_username_register = StringVar()
    entry_username_register = Entry(screen_register, textvariable=get_username_register, font=("Arial",16))
    entry_username_width = 200
    entry_username_height = 30
    entry_username_x_axis = int((width/2)-(entry_username_width/2))
    entry_username_y_axis = lbl_username_y_axis + entry_username_height + (entry_username_height//2)
    entry_username_register.place(width=entry_username_width,height=entry_username_height,x=entry_username_x_axis,y=entry_username_y_axis)
    
    #Label Password
    lbl_password = Label(screen_register, text="Password", font=("Arial",16), bg="#292b2c", fg="#f7f7f7")
    lbl_password_width = 200
    lbl_password_height = 30
    lbl_password_x_axis = int((width/2)-(lbl_password_width/2))
    lbl_password_y_axis = entry_username_y_axis + lbl_password_height + (lbl_password_height//2)
    lbl_password.place(width=lbl_password_width,height=lbl_password_height,x=lbl_password_x_axis,y=lbl_password_y_axis)

    #Entry Password
    global get_password_register
    global entry_password_register
    get_password_register = StringVar()
    entry_password_register = Entry(screen_register, textvariable=get_password_register, font=("Arial",16), show="*")
    entry_password_width = 200
    entry_password_height = 30
    entry_password_x_axis = int((width/2)-(entry_password_width/2))
    entry_password_y_axis = lbl_password_y_axis + entry_password_height + (entry_password_height//2)
    entry_password_register.place(width=entry_password_width,height=entry_password_height,x=entry_password_x_axis,y=entry_password_y_axis)

    #Button Register
    btn_register = Button(screen_register, command=register_validation, text="Register", font=("Arial",16), bg="#f0ad4e", bd=0, activebackground="#ce9544", relief="flat")
    btn_register_width = 200
    btn_register_height = 30
    btn_register_x_axis = int((width/2)-(btn_register_width/2))
    btn_register_y_axis = entry_password_y_axis + btn_register_height + (btn_register_height//2)
    btn_register.place(width=btn_register_width,height=btn_register_height,x=btn_register_x_axis,y=btn_register_y_axis)

    #Button Back
    btn_back = Button(screen_register, command=back,text="Back", font=("Arial",16), bg="#f0ad4e", bd=0, activebackground="#ce9544", relief="flat")
    btn_back_width = 200
    btn_back_height = 30
    btn_back_x_axis = int((width/2)-(btn_back_width/2))
    btn_back_y_axis = btn_register_y_axis + btn_back_height + (btn_back_height//2)
    btn_back.place(width=btn_back_width,height=btn_back_height,x=btn_back_x_axis,y=btn_back_y_axis)
    
    screen_register.mainloop()

def login_screen():
    global screen_login
    screen_login = Tk()
    width = 400
    height = 330 #(widget_amount * sum_widget_height) + (widget_amount * (sum(widget_height/2)))
    screen_window_width = screen_login.winfo_screenwidth()
    screen_window_height = screen_login.winfo_screenheight()
    x_axis = int((screen_window_width/2) - (width/2))
    y_axis = int((screen_window_height/2) - (height/2))
    screen_login.geometry(f"{width}x{height}+{x_axis}+{y_axis}")
    screen_login.title("Login")
    screen_login.configure(background="#292b2c")

    #Label Header
    lbl_header = Label(screen_login, text="Login", font=("Arial",18), bg="#292b2c", fg="#f7f7f7")
    lbl_header_width = 100
    lbl_header_height = 30
    lbl_header_x_axis = int((width/2)-(lbl_header_width/2))
    lbl_header_y_axis = (lbl_header_height//2)
    lbl_header.place(width=lbl_header_width,height=lbl_header_height,x=lbl_header_x_axis,y=lbl_header_y_axis)

    #Label Username
    lbl_username = Label(screen_login, text="Username", font=("Arial",16), bg="#292b2c", fg="#f7f7f7")
    lbl_username_width = 200
    lbl_username_height = 30
    lbl_username_x_axis = int((width/2)-(lbl_username_width/2))
    lbl_username_y_axis = lbl_header_y_axis + lbl_username_height + (lbl_username_height//2)
    lbl_username.place(width=lbl_username_width,height=lbl_username_height,x=lbl_username_x_axis,y=lbl_username_y_axis)

    #Entry Username
    global get_username_login
    global entry_username_login
    get_username_login = StringVar()
    entry_username_login = Entry(screen_login, textvariable=get_username_login, font=("Arial",16))
    entry_username_width = 200
    entry_username_height = 30
    entry_username_x_axis = int((width/2)-(entry_username_width/2))
    entry_username_y_axis = lbl_username_y_axis + entry_username_height + (entry_username_height//2)
    entry_username_login.place(width=entry_username_width,height=entry_username_height,x=entry_username_x_axis,y=entry_username_y_axis)

    #Label Password
    lbl_password = Label(screen_login, text="Password", font=("Arial",16), bg="#292b2c", fg="#f7f7f7")
    lbl_password_width = 200
    lbl_password_height = 30
    lbl_password_x_axis = int((width/2)-(lbl_password_width/2))
    lbl_password_y_axis = entry_username_y_axis + lbl_password_height + (lbl_password_height//2)
    lbl_password.place(width=lbl_password_width,height=lbl_password_height,x=lbl_password_x_axis,y=lbl_password_y_axis)

    #Entry Password
    global get_password_login
    global entry_password_login
    get_password_login = StringVar()
    entry_password_login = Entry(screen_login, textvariable=get_password_login, font=("Arial",16), show="*")
    entry_password_width = 200
    entry_password_height = 30
    entry_password_x_axis = int((width/2)-(entry_password_width/2))
    entry_password_y_axis = lbl_password_y_axis + entry_password_height + (entry_password_height//2)
    entry_password_login.place(width=entry_password_width,height=entry_password_height,x=entry_password_x_axis,y=entry_password_y_axis)

    #Button Login
    btn_login = Button(screen_login, command=login_validation, text="Login", font=("Arial",16), bg="#f0ad4e", bd=0, activebackground="#ce9544", relief="flat")
    btn_login_width = 200
    btn_login_height = 30
    btn_login_x_axis = int((width/2)-(btn_login_width/2))
    btn_login_y_axis = entry_password_y_axis + btn_login_height + (btn_login_height//2)
    btn_login.place(width=btn_login_width,height=btn_login_height,x=btn_login_x_axis,y=btn_login_y_axis)

    #Button Register
    btn_register = Button(screen_login, command=reigster_screen,text="Register", font=("Arial",16), bg="#f0ad4e", bd=0, activebackground="#ce9544", relief="flat")
    btn_register_width = 200
    btn_register_height = 30
    btn_register_x_axis = int((width/2)-(btn_register_width/2))
    btn_register_y_axis = btn_login_y_axis + btn_register_height + (btn_register_height//2)
    btn_register.place(width=btn_register_width,height=btn_register_height,x=btn_register_x_axis,y=btn_register_y_axis)
    
    screen_login.mainloop()

login_screen()
