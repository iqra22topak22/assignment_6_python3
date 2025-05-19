class Engine:
    def start(self):
        return "Engine start ho gaya!"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def drive(self):
        return f"Car chal rahi hai: {self.engine.start()}"

my_engine = Engine()
my_car = Car(my_engine)
print(my_car.drive())


