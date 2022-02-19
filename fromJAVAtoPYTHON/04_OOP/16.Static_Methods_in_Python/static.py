class Player:
    count = 0

    def __init__(self, name) -> None:
        self.name = name
        Player.count += 1

    @staticmethod
    def get_count():
        return Player.count

messi = Player('Messi')
ronaldo = Player('Ronaldo')

print(messi.get_count())
print(ronaldo.get_count())
print(Player.get_count())