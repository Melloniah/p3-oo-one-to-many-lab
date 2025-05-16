class Pet:
    # Class variable: allowed pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    # Class variable: stores all Pet instances
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Set name
        self.name = name

        # Validate pet_type is in the allowed list
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self._pet_type = pet_type  # Use underscore to indicate internal attribute (encapsulation)

        # Optional: validate and set owner
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self._owner = owner

        # Add this Pet instance to the class-level list
        Pet.all.append(self)

    # Getter for pet_type (read-only)
    @property
    def pet_type(self):
        return self._pet_type

    # Getter for owner
    @property
    def owner(self):
        return self._owner

    # Setter for owner — also validates that the new owner is an Owner instance
    @owner.setter
    def owner(self, new_owner):
        if not isinstance(new_owner, Owner):
            raise Exception("Owner must be an instance of the Owner class.")
        self._owner = new_owner


class Owner:
    def __init__(self, name):
        # Set owner's name
        self.name = name

    def pets(self):
        """
        Returns a list of Pet instances that belong to this owner.
        Filters from Pet.all where the owner matches self.
        """
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """
        Assign this owner to the given pet.
        Raises exception if pet is not a Pet instance.
        """
        if not isinstance(pet, Pet):
            raise Exception("Argument must be a Pet instance.")
        pet.owner = self  # Use setter from Pet class

    def get_sorted_pets(self):
        """
        Returns a list of this owner's pets sorted alphabetically by pet name.
        """
        return sorted(self.pets(), key=lambda pet: pet.name)
