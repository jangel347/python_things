# -*- coding: utf-8 -*-
from Supervisor import Supervisor
from Animal import Animal
import time


class ZooSupervisor(Supervisor):
    def __init__(self, name="Carlitos 16"):
        self.name = name
        self.animalsInCharge = []

    def notify(self, action):
        print(f"{self.name}: Avisando a los animales...")
        time.sleep(1)
        for animal in self.animalsInCharge:
            animal.reactToSomething(action)
            time.sleep(1)

    def takeAnimal(self, animal: Animal) -> None:
        self.animalsInCharge.append(animal)

    def somethingHappened(self, action="suena sirena del zoológico") -> None:
        print("Algo sucede...")
        time.sleep(3)
        print(f"¡¡¡{action.upper()}!!!")
        time.sleep(3)
        self.notify(action)
