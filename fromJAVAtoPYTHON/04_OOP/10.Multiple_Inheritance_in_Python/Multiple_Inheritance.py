class LandAnimals:
    def walk(self):
        print('walk')


class WaterAnimal:
    def swim(self):
        print('swim')


class Amphibian(LandAnimals, WaterAnimal):
    pass

frog = Amphibian()

frog.walk()
frog.swim()