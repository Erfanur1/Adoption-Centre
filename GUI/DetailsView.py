import tkinter as tk
import os
from Utils import Utils

class DetailsView(tk.Frame):
    # Frame showing the details of the user
    def __init__(self, parent, model, app, user):
        super().__init__(parent)
        self.parent = parent
        self.model  = model
        self.app    = app
        self.user   = user
        self.create_widgets()

    def create_widgets(self):
        # Banner
        banner = Utils.image(self, os.path.join('image','cat_banner.jpg'))
        banner.pack(fill='x')

    
        stripe = tk.Frame(self, bg='#F6F6F6', height=50)
        stripe.pack(fill='x')
        stripe.pack_propagate(False)
        tk.Label(
            stripe,
            text="Your Adoptions",
            font=("Helvetica", 16, "bold"),
            fg='#A67CFC', bg='#F6F6F6'
        ).place(relx=0.5, rely=0.5, anchor='center')

        # Main content
        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')

        # Table
        panel = tk.Frame(self, bg='#F6F6F6', padx=40, pady=20)
        panel.pack(fill='both', expand=True)
        cols = ("Name","Age","Type")
        self.tree = Utils.treeview(panel, cols)
        self.tree.pack(fill='both', expand=True)
        self.update_view()

    
        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')

        # Footer 
        footer = tk.Frame(self, bg='#A67CFC', height=80)
        footer.pack(fill='x')
        footer.pack_propagate(False)
        close_btn = tk.Button(
            footer, text="Close",
            font=("Helvetica",12,"bold"),
            fg='grey', bg='#888888',
            activebackground='#888888', activeforeground='white',
            relief='flat', bd=0, highlightthickness=0,
            command=self.parent.destroy
        )
        close_btn.place(relx=0.90, rely=0.5, anchor='e')

    def update_view(self):
        
        for row in self.tree.get_children():
            self.tree.delete(row)
      
        for a in self.model.get_user_adoptions(self.user):
            self.tree.insert("", "end", values=(a.name, a.age, a.type))
