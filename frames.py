import customtkinter


class Frame(customtkinter.CTkFrame):
    def __init__(self, parent, width=None, height=None, fg_color='transparent', corner_radius=0):
        super().__init__(parent)
        self.configure(width=width, height=height, fg_color=fg_color, corner_radius=corner_radius)

class SFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, parent, width=None, height=None, fg_color='transparent', corner_radius=0):
        super().__init__(parent)
        self.configure(width=width, height=height, fg_color=fg_color, corner_radius=corner_radius)