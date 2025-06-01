from model.Animal import Cat, Dog, Rabbit

class Animals:
    def __init__(self):
        self.animals = []

    def add(self, animal):
        # adds animals
        self.animals.append(animal)
        return self

    def remove(self, animal):
        self.animals.remove(animal)

    def get_animals(self):
        # list of animals 
        return list(self.animals)

    def get_animals_by_filter(self, filter):
        # Animal filters 
        if filter.lower() == "all":
            return list(self.animals)
        return [a for a in self.animals if type(a).__name__ == filter]

    def animal(self, name):
        #Lookup an animal by name )
        for a in self.animals:
            if a.name == name:
                return a
        return None

    def insert_seed_data(self):
        #Pre-populate with the required demo animals.
         
        self.add(Cat("Jiu Jiu", 5)) \
            .add(Cat("Abby",    8)) \
            .add(Cat("Nimo",    6)) \
            .add(Cat("Whiskers",3)) \
            .add(Cat("Luna",    7)) \
            .add(Cat("Oliver",  2)) \
            .add(Cat("Mochi",   1)) \
            .add(Cat("Simba",   6))

       
        self.add(Dog("Charlie",2)) \
            .add(Dog("Buddy",  4)) \
            .add(Dog("Bella",  1)) \
            .add(Dog("Max",    7)) \
            .add(Dog("Rocky",  8)) \
            .add(Dog("Milo",   5))

        
        self.add(Rabbit("Carrots",1)) \
            .add(Rabbit("Coco",   6)) \
            .add(Rabbit("BunBun", 2)) \
            .add(Rabbit("Hazel",  2)) \
            .add(Rabbit("Peanut", 3))

        return self

