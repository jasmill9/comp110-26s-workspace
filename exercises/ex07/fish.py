"""File to define Fish class."""

__author__ = "730765442"


class Fish:
    """Represents a fish living in the river."""

    age: int

    def __init__(self):
        """Initialize a Fish with age set to 0."""
        self.age: int = 0

    def one_day(self):
        """Age the fish by 1 day."""
        self.age += 1
