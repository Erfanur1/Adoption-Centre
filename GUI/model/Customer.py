# model/Customer.py

from model.User import User
from model.Animals import Animals

class Customer(User):
    ADOPTION_LIMIT = 2

    def __init__(self, name: str, email: str):
        super().__init__(name)
        self.email = email
        # tracking what they have adopted 
        self.adopted_animals = Animals()

    @property
    def first_name(self) -> str:
        """Expose the first part of the full name."""
        return self.name.split()[0] if self.name else ""

    def get_adopted_animals(self) -> Animals:
        """Return the collection of animals this user has adopted."""
        return self.adopted_animals

    def get_email(self) -> str:
        return self.email

    def can_adopt(self, animal) -> bool:
        """Allow up to ADOPTION_LIMIT of each animal type."""
        same_type_count = sum(
            1 for a in self.adopted_animals.get_animals()
            if type(a) is type(animal)
        )
        return same_type_count < Customer.ADOPTION_LIMIT

    def __str__(self):
        return f"{self.name} ({self.email})"
