from model.Customer import Customer
from model.Manager import Manager
from model.exception.InvalidOperationException import InvalidOperationException
from model.exception.UnauthorizedAccessException import UnauthorizedAccessException

class Users:
    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)
        return self

    def get_users(self):
        return list(self.users)

    def insert_seed_data(self, seed_animals):
        # managers
        self.add( Manager("Alice Admin",  12345) ) \
            .add( Manager("Bob Boss",     98765) )

        # customers
        cust1 = Customer("Dahyun Kim",    "dahyun@twice.com")
        cust2 = Customer("Jane Example",  "jane@example.com")
        self.add(cust1).add(cust2)

        # Pre-adopt “Whiskers” for demonstration
        for a in seed_animals.get_animals():
            if a.name == "Whiskers":
                cust1.get_adopted_animals().add(a)
                a.adopt()
                break

        return self

    def validate_manager(self, manager_id):
        # Correct credentials only
        try:
            mid = int(manager_id)
        except ValueError:
            raise InvalidOperationException("Manager ID must be an integer")
        for u in self.users:
            if isinstance(u, Manager) and u.id == mid:
                return u
        raise UnauthorizedAccessException("Invalid manager ID")
