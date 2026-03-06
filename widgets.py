import customtkinter


class Button(customtkinter.CTkButton):
    def __init__(self, parent, text=None, command=None):
        super().__init__(
            parent,
            width=100,
            height=40,
            fg_color=("#185CC2", "#3F5A8E"),
            hover_color=("#1D3D6E", "#22427E"),
            corner_radius=10,
        )
        self.configure(text=text, command=command)


class Entry(customtkinter.CTkEntry):
    def __init__(self, parent, width, height, placeholder_text, show=None):
        super().__init__(parent, corner_radius=12)
        self.configure(
            width=width, height=height, placeholder_text=placeholder_text, show=show
        )


class Label(customtkinter.CTkLabel):
    def __init__(
        self,
        parent,
        text=None,
        font=(None, 0),
        fg_color="transparent",
        corner_radius=0,
    ):
        super().__init__(parent)
        self.configure(
            text=text, font=font, fg_color=fg_color, corner_radius=corner_radius
        )
