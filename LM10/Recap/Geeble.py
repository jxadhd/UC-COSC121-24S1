class Geeble:
    """Defines the Geeble class"""
    def __init__(self, classification, name, health):
        if classification not in ['Warbler', 'Throve', 'Plaguelet']:
            raise ValueError("Invalid Geeble classification")
        if health < 0:
            health = 0
        self.name = name
        self.health = round(health, 1)
        self.classification = classification

    def __str__(self):
        """Returns string of Geeble's deets"""
        ret = f'{self.name} ({self.classification}), health = {self.health:.1f}'
        return ret
    
    def pain(self, damage):
        """Geeble in pain :O"""
        if self.health - damage < 0:
            self.health = 0
        else:
            self.health -= damage

#Test
fester = Geeble('Throve', 'Walter', 10.500)
print(fester)