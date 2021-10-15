from Animal import Animal

class Cow(Animal):
    def __init__(self, name="Lola"):
        self.name = name
    
    def makeSound(self):
        return f"Muuu! hace la vaca {self.name}"
        
    def reactToSomething(self, action)-> None:
        print(f"La vaca {self.name} reacciona a: {action}")
