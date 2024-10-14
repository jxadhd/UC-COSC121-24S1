def is_fashionable(tie_colour, shirt_colour):
    """Fashion? What's that?"""
    if shirt_colour == 'black':
        if tie_colour == 'brown':
            return False
        elif tie_colour == 'ochre':
            return True
    elif shirt_colour == "silver":
        if tie_colour == 'brown':
            return True
        elif tie_colour == "ochre":
            return True
#Test
print(is_fashionable('brown', 'silver'))
