from cat import Cat
from dog import Dog
from cow import Cow

def main():
    # Create a list of animals
    animals = [Dog("Fido"), Cat("Whiskers"), Cow("Bessie")]

    # Iterate over the list and make sounds
    for animal in animals:
        print(animal.name + ": " + animal.make_sound())

if __name__ == "__main__":
    main()