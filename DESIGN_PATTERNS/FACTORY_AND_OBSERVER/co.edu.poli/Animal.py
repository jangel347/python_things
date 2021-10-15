from abc import ABC, abstractmethod

from AnimalBehavior import AnimalBehavior

class Animal(AnimalBehavior,ABC):
    def __init__(self):
        self.name = None

    @abstractmethod
    def makeSound(self):
        pass

