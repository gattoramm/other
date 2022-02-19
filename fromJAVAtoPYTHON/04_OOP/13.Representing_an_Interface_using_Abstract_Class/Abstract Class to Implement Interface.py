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


game = Mario_Game()
game.up()