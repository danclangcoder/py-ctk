import customtkinter
from frames import Frame, SFrame
from widgets import Button, Entry
from hashlib import sha


# customtkinter.set_appearance_mode('light')
customtkinter.set_appearance_mode('dark')


class AppWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Spreadsheets Management System')
        # self.geometry('1920x1080')
        self.minsize(800, 600)
        # self.maximize_window()

        self.build_frames()
        
    def maximize_window(self):
        self.after(10, lambda: self.state('zoomed'))

    def build_frames(self):
        self.sidebar = Frame(self, fg_color=('#b1b1b1', '#202020'))

        self.body = SFrame(self)
        self.body.pack(expand=True, fill='both')

        self.login_frame = Frame(self.body, width=400, height=600, fg_color=('#b1b1b1', "#2A2A2A"), corner_radius=30)
        self.login_frame.pack(pady=(100, 0))
        self.build_widgets(self.login_frame)

    def build_widgets(self, frame):
        self.username = Entry(frame, width=250, height=30, placeholder_text='Username')
        self.username.place(relx=0.5, rely=0.36, anchor='center')
        self.password = Entry(frame, width=250, height=30, placeholder_text='Password')
        self.password.place(relx=0.5, rely=0.42, anchor='center')
        self.register_button = Button(parent=frame, text='Register', command=self.register_user)
        self.register_button.place(relx=0.65, rely=0.85, anchor='center')
        self.login_button = Button(parent=frame, text='Login', command=self.login)
        self.login_button.place(relx=0.35, rely=0.85, anchor='center')

    def register_user(self):
        username, password = [self.username.get(), self.password.get()]
        self.register_button.register_user(username, password)
    
    def login(self):
        self.login_button.login()


if __name__ == '__main__':
    app = AppWindow()
    app.mainloop()