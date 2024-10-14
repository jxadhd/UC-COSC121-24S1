""" LM10 Q14
    Author: Josh Cross
    15/05/2024
    """
class SomeThing:
    """class SomeThing, per LM10, Q14"""
    def __init__(self, name, height, words):
        """Initialises new SomeThing obj"""
        self.name = name
        self.height = height
        self.words = words

    def taller_by(self, amount):
        """Grows by amount"""
        self.height += amount

    def learn (self, new_words):
        """Teaches SomeThing new words"""
        self.words.extend(new_words)

    def __str__(self):
        """Returns SomeThing's details as a str summary"""
        words_str = ', '.join(self.words) if self.words else ''
        return (
            f"Hi. I'm {self.name}. I'm {self.height} cm tall."
            f"\nWords I know: {words_str}" + ("." if words_str else ""))
