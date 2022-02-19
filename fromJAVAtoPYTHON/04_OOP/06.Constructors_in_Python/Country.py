class Country:
    # constructor
    def __init__(self) -> None:
        print('constructor1')
    
    def __init__(self, name='Default') -> None:
        self.name = name
        print('constructor2')
        print(name)

    def instance_method(self):
        print('instance method')

#instances
india1 = Country()
india2 = Country('India')
india1.instance_method()