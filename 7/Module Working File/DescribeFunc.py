"""Demo of keyword arguments. """

def describe(name="Unknown name", species="unknown creature", location="unknown"):
    """Creates the output prescribed in LM7.17"""
    print(f"{name} is a {species}, location: {location}.")

def main():
    """Test the describe function """
    describe(name='Angus', species='chipmunk')
    print(30 * '=')
    describe(species='human', name='Marina')
    print(30 * '=')
    describe(location='Auckland')
    print(30 * '=')
    describe('Peter', 'penguin', 'Antarctica')

main()