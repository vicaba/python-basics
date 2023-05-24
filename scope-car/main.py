from car import Car

def main():
    my_car = Car("Toyota", "Camry", 2022)

    print(my_car._make)
    print(my_car._year)

    print(my_car._Car__model)

    print(my_car.__model)

    my_car.accelerate()

if __name__ == "__main__":
    main()