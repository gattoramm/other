from abc import ABC, abstractmethod


class GamingConsole(ABC):

    @abstractmethod
    def up(self): pass

    @abstractmethod
    def down(self): pass

    @abstractmethod
    def left(self): pass

    @abstractmethod
    def right(self): pass


class Mario_Game(GamingConsole):
    def up(self): print('Mario_Game up')

    def down(self): print('Mario_Game down')

    def left(self): print('Mario_Game left')

    def right(self): print('Mario_Game right')


class Chess_Game(GamingConsole):
    def up(self): print('Chess_Game up')

    def down(self): print('Chess_Game down')

    def left(self): print('Chess_Game left')

    def right(self): print('Chess_Game right')

games = [Mario_Game(), Chess_Game()]
for game in games:
    game.up()