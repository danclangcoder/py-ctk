import customtkinter
from tkinter import messagebox
from frames import Frame, SFrame
from widgets import Button, Entry, Label
from database import init_db
from auth import register, login
from datetime import datetime


init_db()

# customtkinter.set_appearance_mode('light')
customtkinter.set_appearance_mode('dark')


class AppWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Spreadsheets Management System')
        self.geometry('1920x1080')
        self.minsize(800, 800)
        self.maximize_window()

        self.container = Frame(self)
        self.container.pack(expand=True, fill='both')

        self.build_frames()
        
    def maximize_window(self):
        self.after(10, lambda: self.state('zoomed'))

    def build_frames(self):
        # Login Screen
        self.login_frame = Frame(self.container, width=400, height=450, fg_color=("#dbdbdb", "#2A2A2A"), corner_radius=30)
        self.login_frame.pack(pady=(200, 0))
        self.build_login_widgets()

        # Dashboard / Home / App
        self.dashboard_frame = SFrame(self.container, fg_color=('#b1b1b1', '#202020'))
        self.sidebar = Frame(self.dashboard_frame, width=50, fg_color=("#dbdbdb", "#2A2A2A"))
        self.sidebar.pack(side='left', fill='y')
        self.body = Frame(self.dashboard_frame)
        self.body.pack(expand=True, fill='both')
        self.welcome_title = Label(self.body, text="Dashboard", font=('Segoe UI Black', 36, 'bold'))
        self.welcome_title.pack(pady=50)
        self.top_layer = Frame(self.body, fg_color=("#dbdbdb", "#2A2A2A"), corner_radius=40)
        self.top_layer.pack(fill='x', padx=20, pady=20)
        self.build_dashboard_widgets()

    def build_login_widgets(self):
        # Login Widgets
        self.login_title = Label(self.login_frame, text='Login or Register', font=('Segoe UI Black', 24, 'bold'))
        self.login_title.place(relx=0.5, rely=0.15, anchor='center')
        self.username = Entry(self.login_frame, width=250, height=30, placeholder_text='Username')
        self.username.place(relx=0.5, rely=0.30, anchor='center')
        self.password = Entry(self.login_frame, width=250, height=30, placeholder_text='Password', show='*')
        self.password.place(relx=0.5, rely=0.40, anchor='center')
        self.register_button = Button(self.login_frame, text='Register', command=self.register_user)
        self.register_button.place(relx=0.65, rely=0.85, anchor='center')
        self.login_button = Button(self.login_frame, text='Login', command=self.login_user)
        self.login_button.place(relx=0.35, rely=0.85, anchor='center')

    def build_dashboard_widgets(self):
        now = datetime.now()
        formatted_date = now.strftime("%m/%d/%Y")
        self.date_today = Label(self.top_layer, text=formatted_date)
        self.date_today.place(relx=0.8, rely=0.2, anchor='center')

    def register_user(self):
        # username, password = [self.username.get(), self.password.get()]
        username = self.username.get()
        password = self.password.get()
        success, message = register(username, password)
        if not success:
            messagebox.showerror('Register error', message)
            print('ERROR', message)
        else:
            messagebox.showinfo('Success', message)
            print(message)
    
    def login_user(self):
        username, password = [self.username.get(), self.password.get()]
        success, message = login(username, password)
        if not success:
            messagebox.showerror('Login attempt failed', message)
            print('ERROR', message)
        else:
            self.show_dashboard()
            print(message)

    def show_dashboard(self):
        self.dashboard_frame.pack(expand=True, fill='both')
        self.login_frame.pack_forget()

if __name__ == '__main__':
    app = AppWindow()
    app.mainloop()