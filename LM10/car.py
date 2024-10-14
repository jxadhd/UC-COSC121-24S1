class Car:
    """Attributes: model eg Toyota
                   year eg 2000
                   speed (currently)
    """
    def __init__(self, model, year, speed=0):
        """Initialiser
        """
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        """Accelerates (increase) speed by 5 at each call
        """
        self.speed += 5

    def brake(self):
        """Brakes (decreases) speed by 5 at each call
        """
        if self.speed <= 0:
            self.speed -= 0
        elif self.speed > 0:
            self.speed -= 5

    def honk_horn(self):
        """Does a wee toot"""
        model = self.model
        print(f"{model} goes 'beep beep'")

    def __str__(self):
        """Returns a small summary"""
        model = self.model
        year = self.year
        speed = self.speed
        return f"{model} ({year}), moving at {speed} km/h."
