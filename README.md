# Adoption-Centre
A Python/Tkinter-based Adoption Centre GUI application
# Adoption Centre

A desktop GUI application (Python + Tkinter) for managing an animal adoption centre.  
Customers can log in, browse adoptable animals, adopt up to two of each type, and view their own adoption history.  
Managers can log in, filter and remove/add animals, and see a list of all users.

---

## 📂 Project Structure

AdoptionCentre/
├── README.md
├── main.py
├── Utils.py
├── image/ # Banner and any other UI images
│ └── cat_banner.jpg
├── model/ # Core business logic + data classes
│ ├── AdoptionCentre.py
│ ├── Animal.py
│ ├── Animals.py
│ ├── Customer.py
│ ├── Manager.py
│ ├── Users.py
│ ├── exception/
│ │ ├── InvalidOperationException.py
│ │ └── UnauthorizedAccessException.py
│ └── … (any other model files)
├── view/ # All GUI “View” modules
│ ├── LoginView.py
│ ├── CustomerDashboardView.py
│ ├── DetailsView.py
│ ├── ManagerDashboardView.py
│ ├── AddAnimalView.py
│ └── UserListView.py
└── requirements.txt # (Optional) List dependencies if needed


## 🚀 Getting Started

Run the app:

bash
Copy
Edit
python3 main.py
The login screen will appear.

Customers log in via name & email (e.g. Dahyun Kim / dahyun.kim@example.com).

Managers log in with their manager ID (e.g. 1001).

📋 Features
Customer Side
Log in with name + email. Invalid credentials show an error dialogue.

Customer Dashboard

“Welcome <FirstName>” banner

A scrollable list of currently adoptable animals (name & age).

“Adopt” button (enabled only when an animal is selected).

Enforces adoption limit: max 2 per animal type; otherwise, it shows an error.

“My Details” opens a separate window listing the customer’s adopted animals.

“Close” returns to the login screen.

Details View (popup)

Banner and “Your Adoptions” header

Table showing Name, Age, and Type columns for each adopted animal

“Close” button closes the popup only

Manager Side
Log in with manager ID.

Manager Dashboard

“Welcome Manager <Name>” banner

Filter banner (All, Cat, Dog, Rabbit) that filters the table in real time.

Table showing Name | Age | Type | Adopted (Yes/No)

Footer banner with four large buttons (Remove, Add Animal, Users, Close):

Remove: removes the selected unadopted animal.

Add Animal: opens a pop-up with fields (Type dropdown, Name, Age).

Prevents duplicates and non-integer ages.

On success, it refreshes the table immediately.

Users: opens a pop-up listing all users (single-column list “Name (Manager)” or “Name (email)”).

Close: exits the entire application.

Add Animal View (popup)

Banner and “Add Animal” header

Dropdown for Type, Entry for Name, Entry for Age

“Save” validates and adds a new animal, then closes the popup

“Cancel” closes the popup without changes

User List View (popup)

Banner and “User List” header

Single-column TreeView listing “Name (Manager)” or “Name (email)”

“Close” button closes the popup

📝 How It Works
model/AdoptionCentre.py holds all the logic:

login_customer(name, email) & login_manager(manager_id)

get_adoptable_animals(), get_all_animals(), get_animal_types()

adopt_animal(user, animal_name), add_animal(type, name, age), remove_animal(name)

All exceptions (InvalidOperationException, UnauthorizedAccessException) live under model/exception/

View/ files use Tkinter frames and widgets to build each screen.

Each view follows the pattern:

Top banner (image/cat_banner.jpg)

A colored stripe or filter bar, if required

Central panel (Listbox or Treeview) in a white background area

A colored footer with flat, evenly spaced buttons

Utils.py contains helper functions for loading images and configuring Treeviews.

✔️ Testing
Customer flow

Log in as a seeded customer (e.g. Dahyun Kim / dahyun.kim@example.com).

Adopt an animal → it disappears from the main list and appears under “My Details.”

Adopt a second of the same type → still allowed.

Attempt a third of the same type → error dialogue appears.

“Close” on any popup or dashboard returns to the login screen.

Manager flow

Log in with a seeded manager ID (e.g. 1001).

Use the filter buttons (“All,” “Cat,” “Dog,” “Rabbit,” etc.) to filter the table.

Select an unadopted animal → Remove → it disappears from the table.

Select an adopted animal → Remove → error dialogue appears.

Add Animal → enter valid data → table refreshes.

Try a duplicate name or a non-integer age → error dialogue appears.

Users → pop-up lists all users.

Close → exits the entire application.
