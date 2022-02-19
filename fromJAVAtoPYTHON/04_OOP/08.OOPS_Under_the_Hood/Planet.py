class Planet:
    def __init__(self, name, distance_from_sun) -> None:
        self.name = name
        self.distance_from_sun = distance_from_sun

earth = Planet('Earth', 200)
mars = Planet('Mars', 500)

earth.speed = 10000

print(earth.name)
print(earth.speed)

print(mars.name)