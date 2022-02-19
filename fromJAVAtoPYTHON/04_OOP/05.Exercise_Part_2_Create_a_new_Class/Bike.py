class Bike:
    # constructor
    def __init__(self, gear, speed) -> None:
        self.gear = gear
        self.speed = speed

    #toString
    def __repr__(self) -> str:
        return repr((self.gear, self.speed))

#instances
honda = Bike(3, 50)
ducati = Bike(1, 10)

print(honda)
print(ducati)