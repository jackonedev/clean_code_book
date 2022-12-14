# Descriptors 
# pag-238-.pdf
# 1. Property builders
# 2. property descriptors

# 1
class Traveler_1:
    def __init__(self, name, current_city):
        self.name = name
        self._current_city = current_city
        self._cities_visited = [current_city]

    @property
    def current_city(self):
        return self._current_city

    @current_city.setter
    def current_city(self, new_city):
        if new_city != self._current_city:
            self._cities_visited.append(new_city)
        self._current_city = new_city

    @property
    def cities_visited(self):
        return self._cities_visited


# 2
## AHORA VAMOS A REESCRIBIR LA CLASE PERO USANDO DESCRIPTORES
from package.property_descriptor import HistoryTracedAttribute
class Traveler_2:
    current_city = HistoryTracedAttribute("cities_visited")

    def __init__(self, name: str, current_city: str) -> None:
        self.name = name
        self.current_city = current_city

"""
pag-239.pdf
As another solution to this problem, we can use the __setattr__ magic method that
was introduced in Chapter 2, Pythonic Code. We have already seen solutions of this
kind in the previous chapter when we discussed class decorators as an alternative
to using __getattr__.
"""

def main_1():
    alice = Traveler_1('Alice', 'Barcelona')
    alice.current_city = 'Paris'
    alice.current_city = 'Bruselas'
    alice.current_city = 'Amsterdam'

    print (alice.cities_visited)


def main_2():
    alice = Traveler_2('Alice', 'Barcelona')
    alice.current_city = 'Paris'
    alice.current_city = 'Bruselas'
    alice.current_city = 'Amsterdam'

    print (alice.cities_visited)


if __name__ == '__main__':
    main_1()
    print()
    main_2()