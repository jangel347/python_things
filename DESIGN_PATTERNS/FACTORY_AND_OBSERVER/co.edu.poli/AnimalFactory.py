from Animal import Animal
from Cow import Cow
from Fish import Fish
from Bear import Bear


class AnimalFactory:
    def getAnimal(self, animal_type, animal_name=""):
        targetclass = animal_type.capitalize()
        if animal_name == "":
            return globals()[targetclass]()
        else:
            return globals()[targetclass](animal_name)
