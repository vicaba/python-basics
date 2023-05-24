class Car:
    def __init__(self, make, model, year):
        self._make = make
        self.__model = model
        self._year = year

    def start_engine(self):
        print("Engine started.")

    def __drive(self):
        print("Car is being driven.")

    def accelerate(self):
        self.__drive()
        print("Car is accelerating.")