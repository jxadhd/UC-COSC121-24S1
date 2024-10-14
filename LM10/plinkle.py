""" LM10 Q13
    Author: Josh Cross
    15/05/2024
    """

class Plinkle:
    """Plinkle, as defined in Q13"""

    def __init__(self, role, name, health):
        if role not in ['Greebling', 'Throve', 'Plaguelet']:
            raise ValueError("Invalid Plinkle role")
        self.role = role
        self.name = name
        self.health = max(0, health)

    def __str__(self):
        """Returns str of Plinkle deets"""
        return f"{self.name} ({self.role}), health = {self.health:.1f}"

    def inflict(self, amount):
        """Reduces Plinkle's health by amount to minimum 0"""
        self.health = max(0, self.health - amount)

    def drink_health_potion(self, amount):
        """Increases Plinkle health by amount"""
        self.health += amount
