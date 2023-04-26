"""Simulate the River."""
from exercises.ex09.river import River


my_river: River = River(10, 2)

if __name__ == '__main__':
    my_river = River(num_fish=10, num_bears=2)
    my_river.one_river_week()