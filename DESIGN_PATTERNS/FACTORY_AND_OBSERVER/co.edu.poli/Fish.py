from Animal import Animal

class Fish(Animal):
    def __init__(self, name="Dory"):
        self.name = name
    
    def makeSound(self):
        return f"Blup hace el pez {self.name}"
        
    def reactToSomething(self, action)-> None:
        print(f"El pez {self.name} reacciona a: {action}")
