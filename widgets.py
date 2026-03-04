import customtkinter


class Button(customtkinter.CTkButton):
    def __init__(self, parent, width=None, height=None, fg_color='transparent', corner_radius=0, text=None, command=None):
        super().__init__(parent, width=100, height=40, fg_color=("#4483E1", "#3F5A8E"), corner_radius=10)
        self.configure(width=width, height=height, text=text, command=command)

    def register_user(self, username, password):
        print(f'{username}\n{password}')
    
    def login(self):
        print('User logged in.')
    

class Entry(customtkinter.CTkEntry):
    def __init__(self, parent, width, height, placeholder_text):
        super().__init__(parent, corner_radius=12)
        self.configure(width=width, height=height, placeholder_text=placeholder_text)