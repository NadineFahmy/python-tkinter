from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

def signup() :
    sign_screen = Tk()
    sign_screen.title('Signup')
    sign_screen.geometry('925x500+300+200')
    sign_screen.resizable(False, False)
    sign_screen.configure(bg='#fff')
    head = Label(sign_screen, text='Sign up', fg='#FE736C', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    head.place(x=400, y=5)

    def on_enterf(e):
        fname.delete(0, 'end')
    def on_leavef(e):
        name = fname.get()
        if name == '':
            fname.insert(0, 'First Name')

    def on_enterl(e):
        lname.delete(0, 'end')
    def on_leavel(e):
        name = lname.get()
        if name == '':
            lname.insert(0, 'Last Name')

    def on_enterp(e):
        passup.delete(0, 'end')
    def on_leavep(e):
        name = passup.get()
        if name == '':
            passup.insert(0, 'Password')

    def on_entere(e):
        email.delete(0, 'end')
    def on_leavee(e):
        name = email.get()
        if name == '':
            email.insert(0, 'Email')

    def on_enterph(e):
        phone.delete(0, 'end')
    def on_leaveph(e):
        name = phone.get()
        if name == '':
            phone.insert(0, 'Phone Number')

    fname = Entry(sign_screen, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    lname = Entry(sign_screen, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    email = Entry(sign_screen, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    passup = Entry(sign_screen, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
    phone = Entry(sign_screen, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))

    fname.place(x=245, y=100)
    fname.insert(0, 'First Name')
    fname.bind('<FocusIn>', on_enterf)
    fname.bind('<FocusOut>', on_leavef)
    Frame(sign_screen, width=200, height=2, bg='black').place(x=240, y=127)

    lname.place(x=540, y=100)
    lname.insert(0, 'Last Name')
    lname.bind('<FocusIn>', on_enterl)
    lname.bind('<FocusOut>', on_leavel)
    Frame(sign_screen, width=200, height=2, bg='black').place(x=535, y=127)

    email.place(x=245, y= 140)
    email.insert(0, 'Email')
    email.bind('<FocusIn>', on_entere)
    email.bind('<FocusOut>', on_leavee)
    Frame(sign_screen, width=200, height=2, bg='black').place(x=240, y=167)

    passup.place(x=245, y=180)
    passup.insert(0, 'Password')
    passup.bind('<FocusIn>', on_enterp)
    passup.bind('<FocusOut>', on_leavep)
    Frame(sign_screen, width=200, height=2, bg='black').place(x=240, y=207)

    phone.place(x=245, y=220)
    phone.insert(0, 'Phone Number')
    phone.bind('<FocusIn>', on_enterph)
    phone.bind('<FocusOut>', on_leaveph)
    Frame(sign_screen, width=200, height=2, bg='black').place(x=240, y=247)

    Label(sign_screen, text='Gender:', fg='black', bg='white', font=('Microsoft YaHei UI Light', 11)).place(x=245, y=260)
    Radiobutton(sign_screen, text= 'Male', variable= 'male', value= 1, fg='black', bg='white', font=('Microsoft YaHei UI Light', 11)).place(x=305, y=260)
    Radiobutton(sign_screen, text='Female', variable='female', value=2, fg='black', bg='white', font=('Microsoft YaHei UI Light', 11)).place(x=375, y=260)

    Button(sign_screen, width=39, pady=7, text='Send', bg='#FE736C', fg='white', border=0).place(x=340, y=320)

    sign_screen.mainloop()

img = PhotoImage(file='—Pngtree—hand drawn cartoon medical blood_5483126 (1).png')
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Log in', fg='#FE736C', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100 , y=5)

def on_enter(e) :
    user.delete(0, 'end')

def on_leave(e) :
    name = user.get()
    if name == '' :
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame, width=295, height=2 , bg='black').place(x=25, y=107)

def on_enter(e) :
    code.delete(0, 'end')

def on_leave(e) :
    name = code.get()
    if name == '' :
        code.insert(0, 'Password')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame, width=295, height=2 , bg='black').place(x=25, y=177)

Button(frame, width=39, pady=7, text='Log in', bg='#FE736C', fg='white', border=0).place(x=35, y=204)

label = Label(frame, text='Don`t have an account?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#FE736C', command=signup)
sign_up.place(x=215 , y=270)

root.mainloop()