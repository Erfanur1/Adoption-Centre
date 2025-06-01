import tkinter as tk
import os
from Utils import Utils
from ErrorView import ErrorView

class CustomerDashboardView(tk.Frame):
    def __init__(self, parent, model, app, user):
        super().__init__(parent)
        self.model = model
        self.app   = app
        self.user  = user

        self.app.root.title("Customer Dashboard")
        self.create_widgets()

    def create_widgets(self):
        # Banner
        banner = Utils.image(self, os.path.join('image','cat_banner.jpg'))
        banner.pack(fill='x')
        # Header
        stripe = tk.Frame(self, bg='#F6F6F6', height=50)
        stripe.pack(fill='x')
        stripe.pack_propagate(False)
        tk.Label(stripe,
                 text=f"Welcome {self.user.first_name}",
                 font=("Helvetica",16,"bold"),
                 fg='#A67CFC', bg='#F6F6F6')\
          .place(relx=0.5, rely=0.5, anchor='center')

        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')

        # Main content
        panel = tk.Frame(self, bg='#F6F6F6', padx=40, pady=20)
        panel.pack(fill='both', expand=True)
        scrollbar = tk.Scrollbar(panel)
        scrollbar.pack(side='right', fill='y')
        self.listbox = tk.Listbox(
            panel,
            yscrollcommand=scrollbar.set,
            font=("Helvetica",12),
            bg='white', fg='black',
            selectbackground='#A67CFC',
            activestyle='none'
        )
        scrollbar.config(command=self.listbox.yview)
        self.listbox.pack(side='left', fill='both', expand=True, padx=80)
        self.listbox.bind('<<ListboxSelect>>', self.on_select)
        self.update_list()

        # Divider
        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')

        # Footer
        footer = tk.Frame(self, bg='#A67CFC', height=80)
        footer.pack(fill='x')
        footer.pack_propagate(False)

        # My Details in a new window (must)
        btn_details = tk.Button(
            footer, text="My Details",
            font=("Helvetica",12,"bold"),
            fg='grey', bg='#888888',
            activebackground='#888888', activeforeground='white',
            relief='flat', bd=0, highlightthickness=0,
            command=self.show_details
        )
        btn_details.place(relx=0.10, rely=0.5, anchor='w')

        # Adopting an animal
        self.btn_adopt = tk.Button(
            footer, text="Adopt",
            font=("Helvetica",12,"bold"),
            fg='black', bg='#888888',
            activebackground='#A67CFC', activeforeground='white',
            relief='flat', bd=0, highlightthickness=0,
            state='disabled',
            command=self.adopt_selected
        )
        self.btn_adopt.place(relx=0.50, rely=0.5, anchor='center')

        # Close logs out (must)
        btn_close = tk.Button(
            footer, text="Close",
            font=("Helvetica",12,"bold"),
            fg='grey', bg='#888888',
    
            relief='flat', bd=0, highlightthickness=0,
            command=self.app.show_login_view
        )
        btn_close.place(relx=0.90, rely=0.5, anchor='e')

    def update_list(self):
        self.listbox.delete(0, tk.END)
        for a in self.model.get_adoptable_animals():
            self.listbox.insert(tk.END, f"{a.name} (Age: {a.age})")

    def on_select(self, _):
        if self.listbox.curselection():
            self.btn_adopt.config(state='normal', fg='white', bg='#A67CFC')
        else:
            self.btn_adopt.config(state='disabled', fg='#888888', bg='#888888')

    def adopt_selected(self):
        idx = self.listbox.curselection()
        if not idx: return
        name = self.listbox.get(idx[0]).split(' (Age:')[0]
        try:
            self.model.adopt_animal(self.user, name)
            self.update_list()
        except Exception as e:
            self.app.switch_view(
                ErrorView,
                message=str(e),
                callback=lambda: self.app.switch_view(CustomerDashboardView, user=self.user)
            )

    def show_details(self):
        import tkinter as tk
        from DetailsView import DetailsView
        detail_win = tk.Toplevel(self)
        detail_win.title("Your Adoptions")
        dv = DetailsView(detail_win, self.model, self.app, self.user)
        dv.pack(fill='both', expand=True)


