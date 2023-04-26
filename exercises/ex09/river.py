"""File to define River class."""
from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear
__author__ = "730621434"


class River:
    """River class setup."""
    
    day: int = 0
    bears: list[Bear] = []
    fish: list[Fish] = []

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the age of the animals and fish and adds survivors to new list."""
        # remove fish that are too old
        new_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish
        # remove bears that are too old
        new_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears
        return None
    
    def remove_fish(self, amount: int) -> None:
        """Function to remove fish amount."""
        for i in range(amount):
            if self.fish:
                self.fish.pop(0)

    def bears_eating(self):
        """Simulates the bears eating and removing the necessary fish amount."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None
    
    def check_hunger(self):
        """Checks the hunger_score of every Bear in the river."""
        bear_survivors = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                bear_survivors.append(bear)
        self.bears = bear_survivors
        return None
        
    def repopulate_fish(self):
        """Repopulating the fishies!"""
        # Get the number of fish
        num_fish = len(self.fish)
        # Get the number of baby fish
        num_baby_fish = num_fish // 2 * 4
        # Adding new baby fish to the list
        for i in range(num_baby_fish):
            new_fish = Fish()
            self.fish.append(new_fish)
        return None
    
    def repopulate_bears(self):
        """Repopulating our Bear friends!"""
        # To get the number of bears
        num_bears = len(self.bears)
        # Get the number of cubs
        num_cubs = num_bears // 2
        # Adding the cubs to the list
        for i in range(num_cubs):
            new_bear = Bear()
            self.bears.append(new_bear)
        return None
    
    def view_river(self):
        """Prints the current day and amount of animals in the River."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Simulate one week of life at the river."""
        for _ in range(7):
            self.one_river_day()