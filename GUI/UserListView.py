import tkinter as tk
import os
from Utils import Utils
from model.Manager import Manager

class UserListView(tk.Frame):
   # Using treeview to showcase the list of users 
    def __init__(self, parent, model, app):
        super().__init__(parent)
        self.parent = parent
        self.model  = model
        self.app    = app
        self.create_widgets()

    def create_widgets(self):
        # Banner
        banner = Utils.image(self, os.path.join('image','cat_banner.jpg'))
        banner.pack(fill='x')

        # Main content 
        stripe = tk.Frame(self, bg='#F6F6F6', height=50)
        stripe.pack(fill='x')
        stripe.pack_propagate(False)
        tk.Label(
            stripe,
            text="User List",
            font=("Helvetica", 16, "bold"),
            fg='#A67CFC', bg='#F6F6F6'
        ).place(relx=0.5, rely=0.5, anchor='center')

        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')

        # Panel
        panel = tk.Frame(self, bg='white', padx=40, pady=20)
        panel.pack(fill='both', expand=True)
        cols = ("User",)
        self.tree = Utils.treeview(panel, cols)
        self.tree.pack(fill='both', expand=True)

        # Seed data
        for u in self.model.users.get_users():
            if isinstance(u, Manager):
                entry = f"{u.name} (Manager)"
            else:
                entry = f"{u.name} ({u.email})"
            self.tree.insert("", "end", values=(entry,))

  
        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')

        #CLose 
        footer = tk.Frame(self, bg='#A67CFC', height=80)
        footer.pack(fill='x')
        footer.pack_propagate(False)
        close_btn = tk.Button(
            footer,
            text="Close",
            font=("Helvetica", 14, "bold"),
            fg='#888888', bg='#A67CFC',
            activebackground='#A67CFC', activeforeground='#888888',
            relief='flat', bd=0, highlightthickness=0,
            command=self.parent.destroy
        )
        close_btn.place(relx=0.5, rely=0.5, anchor='center')
