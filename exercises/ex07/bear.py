"""File to define Bear class."""

__author__ = "730765442"


class Bear:
    """Represents a bear living by the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a Bear with age and hunger_score set to 0."""
        self.age: int = 0
        self.hunger_score: int = 0

    def one_day(self):
        """Age the bear by 1 day and decrease hunger by 1."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Increase hunger_score by num_fish."""
        self.hunger_score += num_fish
