"""File to define Bear class."""


class Bear:
    """Class for Bear."""
    age = int
    hunger_score = int

    def __init__(self):
        """Setting up the age and hunger score."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """Manages the days of the bears."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Manages the eating numbers for fish."""
        self.hunger_score += num_fish
