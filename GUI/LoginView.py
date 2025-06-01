import tkinter as tk
import os
from ErrorView import ErrorView
from Utils import Utils
from CustomerDashboardView import CustomerDashboardView
from ManagerDashboardView import ManagerDashboardView

class LoginView(tk.Frame):
    def __init__(self, parent, model, app):
        super().__init__(parent)
        self.model = model
        self.app = app

     
        self.username_var   = tk.StringVar()
        self.email_var      = tk.StringVar()
        self.manager_id_var = tk.StringVar()

        self.create_widgets()
        self.update_login_button_state()

    def create_widgets(self):
        # Banner
        banner = Utils.image(self, os.path.join('image','cat_banner.jpg'))
        banner.pack(fill='x')

        header = tk.Frame(self, bg='#F6F6F6', height=50)
        header.pack(fill='x')
        header.pack_propagate(False)
        tk.Label(header, text="Login",
                 font=("Helvetica", 16, "bold"),
                 fg='#A67CFC', bg='#F6F6F6')\
          .place(relx=0.5, rely=0.5, anchor='center')

        tk.Frame(self, height=1, bg='#CCCCCC').pack(fill='x')

        # Main content
        panel1 = tk.Frame(self, bg='#F6F6F6', padx=40, pady=20)
        panel1.pack(fill='x')

        tk.Label(panel1, text="Username:",
                 font=("Helvetica", 12, "bold"),
                 fg='#A67CFC', bg='#F6F6F6')\
          .grid(row=0, column=0, sticky='w', pady=8)
        tk.Entry(panel1, textvariable=self.username_var,
                 font=("Helvetica",12),
                 bg='black', fg='white', insertbackground='white')\
          .grid(row=0, column=1, sticky='we', padx=(10,0), pady=8)

        tk.Label(panel1, text="Email:",
                 font=("Helvetica", 12, "bold"),
                 fg='#A67CFC', bg='#F6F6F6')\
          .grid(row=1, column=0, sticky='w', pady=8)
        tk.Entry(panel1, textvariable=self.email_var,
                 font=("Helvetica",12),
                 bg='black', fg='white', insertbackground='white')\
          .grid(row=1, column=1, sticky='we', padx=(10,0), pady=8)

        panel1.columnconfigure(1, weight=1)

  
        tk.Frame(self, height=1, bg='#CCCCCC').pack(fill='x')

        # Main content for manager login
        panel2 = tk.Frame(self, bg='#F6F6F6', padx=40, pady=20)
        panel2.pack(fill='x')

        tk.Label(panel2, text="Manager ID:",
                 font=("Helvetica", 12, "bold"),
                 fg='#A67CFC', bg='#F6F6F6')\
          .grid(row=0, column=0, sticky='w', pady=8)
        tk.Entry(panel2, textvariable=self.manager_id_var,
                 font=("Helvetica",12),
                 bg='black', fg='white', insertbackground='white')\
          .grid(row=0, column=1, sticky='we', padx=(10,0), pady=8)

        panel2.columnconfigure(1, weight=1)

        tk.Frame(self, height=1, bg='#CCCCCC').pack(fill='x')

        footer = tk.Frame(self, bg='#A67CFC', height=80)
        footer.pack(fill='x')
        footer.pack_propagate(False)

        # Login button 
        login_border = tk.Frame(footer, bg='#444444', padx=4, pady=4)
        login_border.place(relx=0.05, rely=0.5, anchor='w')
        self.login_btn = tk.Button(
            login_border, text="Login",
            font=("Helvetica",12,"bold"),
            state='disabled',
            fg='white', bg='#F6F6F6',
            relief='flat',
            command=self.on_login
        )
        self.login_btn.pack()

        # Exit button 
        exit_border = tk.Frame(footer, bg='#444444', padx=4, pady=4)
        exit_border.place(relx=0.95, rely=0.5, anchor='e')
        tk.Button(
            exit_border, text="Exit",
            font=("Helvetica",12,"bold"),
            fg='#A67CFC', bg='white',
            relief='flat',
            command=self.app.root.destroy
        ).pack()

        # Traces for enabling login button 
        for var in (self.username_var, self.email_var, self.manager_id_var):
            var.trace_add('write', lambda *a: self.update_login_button_state())

    def update_login_button_state(self):
    
        is_mgr = bool(self.manager_id_var.get().strip())
        is_cust = bool(self.username_var.get().strip() and 
                       self.email_var.get().strip())
        if is_mgr or is_cust:
            self.login_btn.config(state='normal', fg='#A67CFC', bg='white')
        else:
            self.login_btn.config(state='disabled', fg='white', bg='#F6F6F6')

    def on_login(self):
        uname = self.username_var.get().strip()
        email = self.email_var.get().strip()
        mid   = self.manager_id_var.get().strip()
        try:
            if mid:
                user = self.model.login_manager(mid)
                self.app.switch_view(ManagerDashboardView, user=user)
            else:
                user = self.model.login_customer(uname, email)
                self.app.switch_view(CustomerDashboardView, user=user)
        except Exception as ex:
            self.app.switch_view(
                ErrorView, 
                message=str(ex), 
                callback=self.app.show_login_view
            )
