import customtkinter


class Frame(customtkinter.CTkFrame):
    def __init__(self, parent, width=None, height=None, bg_color='transparent', fg_color='transparent', corner_radius=0, border_color='', border_width=0):
        super().__init__(parent)
        self.configure(width=width, height=height, bg_color=bg_color, fg_color=fg_color, corner_radius=corner_radius, border_color=border_color, border_width=border_width)

class SFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, parent, width=None, height=None, fg_color='transparent', corner_radius=0):
        super().__init__(parent)
        self.configure(width=width, height=height, fg_color=fg_color, corner_radius=corner_radius)