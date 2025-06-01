import tkinter as tk
import os
from Utils import Utils
from ErrorView import ErrorView

class AddAnimalView(tk.Frame):
    def __init__(self, parent, model, app, callback):
        super().__init__(parent)
        self.model = model
        self.app = app
        self.callback = callback  
        # variables
        self.type_var = tk.StringVar(value=model.get_animal_types()[0])
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Banner
        banner = Utils.image(self, os.path.join('image','cat_banner.jpg'))
        banner.pack(fill='x')

        # Header
        stripe = tk.Frame(self, bg='#F6F6F6', height=50)
        stripe.pack(fill='x')
        stripe.pack_propagate(False)
        tk.Label(
            stripe,
            text="Add Animal",
            font=("Helvetica", 16, "bold"),
            fg='#A67CFC', bg='#F6F6F6'
        ).place(relx=0.5, rely=0.5, anchor='center')

        
        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')

        # Main content
        panel = tk.Frame(self, bg='#F6F6F6', padx=40, pady=20)
        panel.pack(fill='both', expand=True)
  
        tk.Label(panel, text="Type:", font=("Helvetica",12), fg='#A67CFC', bg='#F6F6F6')\
            .grid(row=0, column=0, sticky='w', pady=8)
        type_menu = tk.OptionMenu(panel, self.type_var, *(["All"] + self.model.get_animal_types()))
        type_menu.config(font=("Helvetica",12), bg='white', fg='black', highlightthickness=0)
        type_menu.grid(row=0, column=1, sticky='we', padx=(10,0), pady=8)

        # Name
        tk.Label(panel, text="Name:", font=("Helvetica",12), fg='#A67CFC', bg='#F6F6F6')\
            .grid(row=1, column=0, sticky='w', pady=8)
        tk.Entry(panel, textvariable=self.name_var, font=("Helvetica",12), bg='white', fg='black')\
            .grid(row=1, column=1, sticky='we', padx=(10,0), pady=8)
        # Age
        tk.Label(panel, text="Age:", font=("Helvetica",12), fg='#A67CFC', bg='#F6F6F6')\
            .grid(row=2, column=0, sticky='w', pady=8)
        tk.Entry(panel, textvariable=self.age_var, font=("Helvetica",12), bg='white', fg='black')\
            .grid(row=2, column=1, sticky='we', padx=(10,0), pady=8)

        panel.columnconfigure(1, weight=1)

        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')

        # Footer
        footer = tk.Frame(self, bg='#A67CFC', height=80)
        footer.pack(fill='x')
        footer.pack_propagate(False)
        # Save
        save_btn = tk.Button(
            footer, text="Save",
            font=("Helvetica",12,"bold"), fg='grey',  # #888888',
            relief='flat', bd=0, highlightthickness=0,
            command=self.save_animal
        )
    
        save_btn.place(relx=0.4, rely=0.5, anchor='center')
        # Cancelling 
        cancel_btn = tk.Button(
            footer, text="Cancel",
            font=("Helvetica",12,"bold"), fg='grey', bg='#888888',
            relief='flat', bd=0, highlightthickness=0,
            command=lambda: self.master.destroy()
        )
        cancel_btn.place(relx=0.6, rely=0.5, anchor='center')

    def save_animal(self):
        t = self.type_var.get().strip()
        name = self.name_var.get().strip()
        age_str = self.age_var.get().strip()
        try:
            age = int(age_str)
        except ValueError:
            raise ErrorView(message="Age must be an integer", callback=None)
        try:
            self.model.add_animal(t, name, age)
            self.callback()
            self.master.destroy()
        except Exception as e:
            self.app.switch_view(ErrorView, message=str(e), callback=lambda: None)
