import tkinter as tk
import os
from Utils import Utils

class ErrorView(tk.Frame):
    def __init__(self, parent, model, app, message, callback):
        super().__init__(parent, padx=0, pady=0)
        self.app = app
        self.callback = callback
        self.create_widgets(message)

    def create_widgets(self, message):
        banner = Utils.image(self, os.path.join('image','error_banner.jpg'))
        banner.pack(fill='x')
        Utils.separator(self).pack(fill='x', pady=(0,10))

        title = Utils.label(self, "Error")
        title.config(font=("Helvetica", 18, "bold"))
        title.pack(pady=(0,10))

        msg = tk.Label(self, text=message, font=("Helvetica", 12))
        msg.pack(pady=(0,20))

        btn = Utils.button(self, "OK", self.on_ok)
        btn.pack()

    def on_ok(self):
        self.callback()
