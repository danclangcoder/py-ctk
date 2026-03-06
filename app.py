import customtkinter
from tkinter import messagebox
from frames import Frame, SFrame
from widgets import Button, Entry, Label
from database import init_db
from auth import register, login
from datetime import datetime
from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
menu_icon_path = os.path.join(BASE_DIR, "menu_icon.png")

init_db()

# customtkinter.set_appearance_mode('light')
customtkinter.set_appearance_mode("dark")


class AppWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Spreadsheets Management System")
        # self.geometry('1920x1080')
        self.minsize(800, 500)
        # self.maximize_window()

        self.container = Frame(self)
        self.container.pack(expand=True, fill="both")

        self.build_frames()

    def maximize_window(self):
        self.after(10, lambda: self.state("zoomed"))

    def build_frames(self):
        # Login Screen
        self.login_frame = Frame(
            self.container,
            width=400,
            height=450,
            fg_color=("#dbdbdb", "#2A2A2A"),
            corner_radius=30,
        )
        self.login_frame.pack(pady=(200, 0))
        self.build_login(self.login_frame)

        # Dashboard Screen
        self.dashboard_frame = Frame(self.container, fg_color=("#b1b1b1", "#202020"))

        # Scrollable container
        self.body = SFrame(self.dashboard_frame)
        self.body.pack(expand=True, fill="both")

        self.menu_icon = customtkinter.CTkImage(
            Image.open('menu_icon.png'), size=(20, 20)
        )

        self.sidebar = Frame(self.body, width=50, fg_color=("#dbdbdb", "#2A2A2A"))
        self.sidebar_visible = False
        self.sidebar_btn = customtkinter.CTkButton(
            self.body,
            text="",
            image=self.menu_icon,
            fg_color="transparent",
            hover_color="#383838",
            width=50,
            height=50,
            command=self.toggle_sidebar,
        ).pack(side='left', anchor='nw', padx=5, pady=20)

        # Dashboard Frames
        self.top_layer = Frame(
            self.body, fg_color=("#dbdbdb", "#2A2A2A"), corner_radius=25
        )
        self.top_layer.pack(fill="x", padx=20, pady=20)

        self.container_1 = Frame(
            self.body, height=300, fg_color=("#dbdbdb", "#2A2A2A"), corner_radius=35
        )
        self.container_2 = Frame(
            self.body, height=500, fg_color=("#dbdbdb", "#2A2A2A"), corner_radius=35
        )
        self.container_3 = Frame(
            self.body, height=200, fg_color=("#dbdbdb", "#2A2A2A"), corner_radius=35
        )
        self.container_1.pack(fill="x", padx=20, pady=20)
        self.container_2.pack(fill="x", padx=20, pady=20)
        self.container_3.pack(fill="x", padx=20, pady=20)

        self.frames = [
            self.top_layer,
            self.container_1,
            self.container_2,
            self.container_3,
        ]

        self.build_dashboard(self.frames)

    def build_login(self, frame):
        self.login_title = Label(
            frame, text="Login", font=("Segoe UI Black", 24, "bold")
        )
        self.username = Entry(frame, width=250, height=30, placeholder_text="Username")
        self.password = Entry(
            frame, width=250, height=30, placeholder_text="Password", show="*"
        )
        self.login_button = Button(frame, text="Login", command=self.login_user)

        self.login_title.place(relx=0.5, rely=0.15, anchor="center")
        self.username.place(relx=0.5, rely=0.30, anchor="center")
        self.password.place(relx=0.5, rely=0.40, anchor="center")
        self.login_button.place(relx=0.5, rely=0.85, anchor="center")

    def build_dashboard(self, frames):
        top, ct1, ct2, ct3 = frames
        self.welcome_title = Label(
            top, text="Dashboard", font=("Segoe UI Black", 36, "bold")
        )
        date_today = datetime.now().strftime("%B %d, %Y")
        self.date_today = Label(
            top, text=date_today, font=("Cascadia Mono", 16, "bold")
        )

        self.welcome_title.pack(pady=(10, 0))
        self.date_today.pack(pady=(0, 10))

    def register_user(self):
        username = self.username.get()
        password = self.password.get()
        success, message = register(username, password)
        if not success:
            messagebox.showerror("Register error", message)
            print("ERROR", message)
        else:
            messagebox.showinfo("Success", message)
            print(message)

    def login_user(self):
        username, password = [self.username.get(), self.password.get()]
        success, message = login(username, password)
        if not success:
            messagebox.showerror("Login attempt failed", message)
            print("ERROR", message)
        else:
            self.show_dashboard()
            print(message)

    def show_dashboard(self):
        self.dashboard_frame.pack(expand=True, fill="both")
        self.login_frame.pack_forget()

    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar.pack_forget()
            self.sidebar_visible = False
        else:
            self.sidebar.pack(side="left", fill="y", before=self.sidebar_btn)
            self.sidebar_visible = True


if __name__ == "__main__":
    app = AppWindow()
    app.mainloop()
