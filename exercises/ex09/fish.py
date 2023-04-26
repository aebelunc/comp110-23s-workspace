"""File to define Fish class."""


class Fish:
    """Class for fish."""
    age = int
    
    def __init__(self):
        """New fish with age."""
        self.age = 0
        return None
    
    def one_day(self):
        """Iterates through the age."""
        self.age += 1
        return None