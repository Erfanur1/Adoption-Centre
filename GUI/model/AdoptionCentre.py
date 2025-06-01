from model.Users import Users
from model.Animals import Animals
from model.Customer import Customer
from model.exception.InvalidOperationException import InvalidOperationException
from model.exception.UnauthorizedAccessException import UnauthorizedAccessException
from model.Animal import Cat, Dog, Rabbit

class AdoptionCentre:
    def __init__(self):
       # seed data 
        seed_animals = Animals().insert_seed_data()
        self.animals = seed_animals
        
        self.users = Users().insert_seed_data(seed_animals)

    def login_customer(self, name, email):
        for u in self.users.get_users():
            if isinstance(u, Customer) and u.name == name and u.email == email:
                return u
        raise InvalidOperationException("Invalid customer credentials")

    def login_manager(self, manager_id):
        return self.users.validate_manager(manager_id)

    def get_adoptable_animals(self):
        return [a for a in self.animals.get_animals() if not a.is_already_adopted()]

    def get_all_animals(self):
        return list(self.animals.get_animals())

    def get_animal_types(self):
        """Return sorted list of unique animal type names."""
        return sorted({a.type for a in self.animals.get_animals()})

    def adopt_animal(self, user, animal_name):
        target = self.animals.animal(animal_name)
        if not target:
            raise InvalidOperationException(f"Animal '{animal_name}' not found")
        if target.is_already_adopted():
            raise InvalidOperationException(f"'{animal_name}' has already been adopted")
        if not user.can_adopt(target):
            raise InvalidOperationException("You have reached your adoption limit for this animal type")
        target.adopt()
        user.get_adopted_animals().add(target)

    def get_user_adoptions(self, user):
        return list(user.get_adopted_animals().get_animals())

    def add_animal(self, type_str, name, age):
        if self.animals.animal(name) is not None:
            raise InvalidOperationException("An animal with this name already exists")
        mapping = {'Cat': Cat, 'Dog': Dog, 'Rabbit': Rabbit}
        if type_str not in mapping:
            raise InvalidOperationException("Invalid animal type")
        if not isinstance(age, int):
            raise InvalidOperationException("Age must be an integer")
        self.animals.add(mapping[type_str](name, age))

    def remove_animal(self, name):
        target = self.animals.animal(name)
        if not target:
            raise InvalidOperationException(f"Animal '{name}' not found")
        if target.is_already_adopted():
            raise InvalidOperationException("Cannot remove an adopted animal")
        self.animals.remove(target)

