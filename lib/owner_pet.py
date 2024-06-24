class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type '{pet_type}'. Allowed types are {', '.join(Pet.PET_TYPES)}.")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)

        # If an owner is provided, add this pet to the owner's pets list
        if owner:
            owner.add_pet(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added as pets.")
        if pet not in self._pets:  # Prevent adding the same pet multiple times
            self._pets.append(pet)
            pet.owner = self

    def get_sorted_pets(self):
        sorted_pets = sorted(self._pets, key=lambda pet: pet.name)
        return sorted_pets
