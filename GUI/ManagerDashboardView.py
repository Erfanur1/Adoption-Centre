import tkinter as tk
import os
from Utils import Utils
from ErrorView import ErrorView

class ManagerDashboardView(tk.Frame):
    def __init__(self, parent, model, app, user):
        super().__init__(parent)
        self.model = model
        self.app = app
        self.user = user

        self.app.root.title("Manager Dashboard")
        self.create_widgets()

    def create_widgets(self):
        # Banner
        banner = Utils.image(self, os.path.join('image', 'cat_banner.jpg'))
        banner.pack(fill='x')

    
        stripe = tk.Frame(self, bg='#F6F6F6', height=50)
        stripe.pack(fill='x')
        stripe.pack_propagate(False)
        tk.Label(
            stripe,
            text=f"Welcome Manager {self.user.name}",
            font=("Helvetica", 16, "bold"),
            fg='#A67CFC', bg='#F6F6F6'
        ).place(relx=0.5, rely=0.5, anchor='center')

  
        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')


        filter_bar = tk.Frame(self, bg='#F6F6F6', height=50)
        filter_bar.pack(fill='x')
        filter_bar.pack_propagate(False)
        types = ["All"] + self.model.get_animal_types()
        for idx, t in enumerate(types):
            btn = tk.Button(
                filter_bar,
                text=t,
                font=("Helvetica", 12),
                fg='#A67CFC', bg='#F6F6F6',
                activebackground='#F6F6F6', activeforeground='#A67CFC',
                relief='flat', bd=0, highlightthickness=0,
                command=lambda t=t: self.apply_filter(t)
            )
            btn.grid(row=0, column=idx, sticky='nsew')
            filter_bar.grid_columnconfigure(idx, weight=1)

        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')

        # Main content 
        panel = tk.Frame(self, bg='white', padx=40, pady=20)
        panel.pack(fill='both', expand=True)
        scrollbar = tk.Scrollbar(panel)
        scrollbar.pack(side='right', fill='y')
        cols = ("Name", "Age", "Type", "Adopted")
        self.tree = Utils.treeview(panel, cols)
        try:
            self.tree.configure(background='white', foreground='black')
        except Exception:
            pass
        self.tree.pack(fill='both', expand=True)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree.yview)
        self.update_table()

    
        tk.Frame(self, bg='#CCCCCC', height=1).pack(fill='x')

    
        footer = tk.Frame(self, bg='#A67CFC', height=80)
        footer.pack(fill='x')
        footer.pack_propagate(False)

        labels = ["Remove", "Add Animal", "Users", "Close"]
        actions = [
            self.remove_selected,
            self.open_add_window,
            self.open_users_window,
            self.app.root.destroy
        ]
        for i, (lbl, cmd) in enumerate(zip(labels, actions)):
            btn = tk.Button(
                footer,
                text=lbl,
                font=("Helvetica", 14, "bold"),
                fg='#888888', bg='#A67CFC',
                activebackground='#A67CFC', activeforeground='#888888',
                relief='flat', bd=0, highlightthickness=0,
                command=cmd
            )
            btn.grid(row=0, column=i, sticky='nsew', padx=10, pady=10)
            footer.grid_columnconfigure(i, weight=1)
        footer.grid_rowconfigure(0, weight=1)

    def update_table(self, filter_type="All"):
        for row in self.tree.get_children():
            self.tree.delete(row)
        items = self.model.get_all_animals()
        if filter_type != "All":
            items = [a for a in items if a.type == filter_type]
        for a in items:
            self.tree.insert(
                "", "end",
                values=(a.name, a.age, a.type,
                        "Yes" if a.is_already_adopted() else "No")
            )

    def apply_filter(self, t):
        self.update_table(filter_type=t)

    def remove_selected(self):
        sel = self.tree.selection()
        if not sel:
            return
        name = self.tree.item(sel[0])['values'][0]
        try:
            self.model.remove_animal(name)
            self.update_table()
        except Exception as e:
            self.app.switch_view(
                ErrorView,
                message=str(e),
                callback=lambda: self.app.switch_view(ManagerDashboardView, user=self.user)
            )

    def open_add_window(self):
        import tkinter as tk
        from AddAnimalView import AddAnimalView
        win = tk.Toplevel(self)
        win.title("Add Animal")
        AddAnimalView(win, self.model, self.app, callback=self.update_table).pack(fill='both', expand=True)

    def open_users_window(self):
        import tkinter as tk
        from UserListView import UserListView
        win = tk.Toplevel(self)
        win.title("User List")
        UserListView(win, self.model, self.app).pack(fill='both', expand=True)
