from Animal import Animal

class Bear(Animal):
    
    def __init__(self, name="Yoggi"):
        self.name = name
    
    def makeSound(self):
        return f"Wrauu hace el oso {self.name}"
        
    def reactToSomething(self, action)-> None:
        print(f"El oso {self.name} reacciona a: {action}")
