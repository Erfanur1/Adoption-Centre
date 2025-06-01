import tkinter as tk
from LoginView import LoginView
from model.AdoptionCentre import AdoptionCentre

class MainApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Prog2 Adoption Centre")
        self.model = AdoptionCentre()
        self.current_view = None
        self.show_login_view()
        self.root.mainloop()

    def switch_view(self, view_class, **kwargs):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = view_class(self.root, self.model, self, **kwargs)
        self.current_view.pack(fill='both', expand=True)

    def show_login_view(self):
        self.switch_view(LoginView)

if __name__ == '__main__':
    MainApp()
