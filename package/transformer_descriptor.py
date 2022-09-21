# Descriptors - after decorators_1.py
# pag-247-248.pdf

from typing import Callable

class BaseFieldTransformation:
    def __init__(self, transformation: Callable[[],str]) -> None:
        self._name = None
        self.transformation = transformation

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        raw_value = instance.__dict__[self._name]
        return self.transformation(raw_value)

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value
