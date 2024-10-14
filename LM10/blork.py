""" LM10 Blork exercise
    Author: Josh Cross
    """
class Blork:
    """Defines the Blork class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool    
    """

    def __init__(self, name, height, has_horns=False, baranges=0):
        """Creates a new Blork object"""
        self.name = name
        self.height = height
        self.has_horns = has_horns
        self.baranges = baranges

    def say_hello(self):
        """Makes Blork say hello!"""
        output = f"Hi! My name is {self.name}!"
        if self.has_horns:
            output = output.upper()
        print(output)

    def grow(self, amount):
        """Grows Blork by amount"""
        self.height += amount

    def __str__(self):
        """Returns a small description of blork!"""
        horns = self.has_horns
        name = self.name
        height = self.height
        if not horns:
            return f"{name} is a {height:.2f} m tall blork!"
        elif horns:
            return f"{name} is a {height:.2f} m tall horned blork!"

    def collect_baranges(self, num=1):
        """Blork collects more baranges"""
        self.baranges += num

    def eat(self):
        """Blork eats one barange and grows 0.1 m"""
        if self.baranges >= 1:
            self.baranges -= 1
            self.height += 0.1
        else:
            print("I don't have any baranges to eat!")

    def feast(self):
        """Blork consumes 5 baranges. Blork grows horns if it doesn't
        have them already. If it is horned, it grows by 50% instead"""
        if self.baranges >= 5:
            self.baranges -= 5
            if not self.has_horns:
                self.has_horns = True
            else:
                self.height += self.height * 0.5
        else:
            print("I don't have enough baranges to feast!")
