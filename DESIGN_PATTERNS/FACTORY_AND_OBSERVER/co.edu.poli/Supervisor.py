from abc import ABC, abstractmethod
from Animal import Animal

class Supervisor(ABC):

    @abstractmethod
    def notify(self, action):
        pass

    @abstractmethod
    def takeAnimal(self, animal: Animal):
        pass
