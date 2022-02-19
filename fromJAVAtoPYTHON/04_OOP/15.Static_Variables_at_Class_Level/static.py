class Player:
    count = 0

    def __init__(self, name) -> None:
        self.name = name
        Player.count += 1

messi = Player('Messi')
ronaldo = Player('Ronaldo')

print(Player.count)

print(messi.count)
print(ronaldo.count)

Player.count = 100

#messi.count = 100

print(Player.count)

print(messi.count)
print(ronaldo.count)