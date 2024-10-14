class Taganeran:
    """Defines the Taganeran class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_nose of type bool    
    """

    def __init__(self, name, height, has_nose=False):
        """Taganeran constructor"""
        self.name = name
        self.height = height
        self.has_nose = has_nose
        self.jujubes = int(0)
    
    def __str__(self):
        """Returns a string"""
        msg1 = f"{self.name} is a {self.height:.2f} m tall Taganeran!"
        msg2 = f'{self.name} is a {self.height:.2f} m tall Taganeran with a nose!'
        if self.has_nose:
            return msg2
        else:
            return msg1

    def say_hello(self):
        """Prints a hello message!"""
        msg = f"Hello. My name is {self.name}."
        if not self.has_nose:
            print(msg)
        else:
            print(msg.upper())
    
    def collect_jujubes(self, number=1):
        """Taganeran collects jujubes"""
        if not number:
            self.jujubes += 1
        else:
            self.jujubes += number
    
    def eat(self):
        """Taganeran eats 1 jujube and grows 0.2m"""
        if self.jujubes > 0:
            self.jujubes -= 1
            self.height += 0.2
        else:
            print("I don't have any jujubes to eat!")
    
    def feast(self):
        """Taganeran hungry. consumes 5"""
        if self.jujubes < 5:
            print("I don't have enough jujubes to feast!")
        elif not self.has_nose:
            self.has_nose = True
            self.jujubes -= 5
        else:
            self.height += self.height * 0.5
            self.jujubes -= 5



#Test
first_alien = Taganeran("Jeff", 1.6)
first_alien.say_hello()
mighty_alien = Taganeran("Tania", 3.14, True)
mighty_alien.say_hello()
first_alien = Taganeran("Jeff", 1.6)
print(first_alien)
mighty_alien = Taganeran("Tania", 3.14, True)
print(mighty_alien)

mighty_alien = Taganeran("Tania", 3.14, True)
print("Jujubes: {}".format(mighty_alien.jujubes))
mighty_alien.collect_jujubes(9)
print("Jujubes: {}".format(mighty_alien.jujubes))
mighty_alien.feast()
print("Jujubes: {}".format(mighty_alien.jujubes))
print(mighty_alien)