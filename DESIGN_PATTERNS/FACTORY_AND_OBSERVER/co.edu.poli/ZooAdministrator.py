# -*- coding: utf-8 -*-
from ZooSupervisor import ZooSupervisor
from AnimalFactory import AnimalFactory

class ZooAdministrator:
    def __init__(self):
        animal_factory = AnimalFactory()
        carlitos = ZooSupervisor()
        
        lola = animal_factory.getAnimal('cow')
        lolita = animal_factory.getAnimal('cow', 'Lolita')
        
        yoggi = animal_factory.getAnimal('bear')
        poo = animal_factory.getAnimal('bear','Poo')
        
        dory = animal_factory.getAnimal('fish')
        nemo = animal_factory.getAnimal('fish','Nemo')
        
        carlitos.takeAnimal(lola)
        carlitos.takeAnimal(lolita)
        carlitos.takeAnimal(yoggi)
        carlitos.takeAnimal(poo)
        carlitos.takeAnimal(dory)
        carlitos.takeAnimal(nemo)
        
        carlitos.somethingHappened('se cayó un faro')


