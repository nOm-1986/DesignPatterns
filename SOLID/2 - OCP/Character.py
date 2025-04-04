from abc import ABC, abstractmethod

class Character(ABC):
    
    def __init__(self, name: str, level: int = 1, experience: str=0, max_exp:int = 50, exp_per_attack: int = 1):
        self._name = name
        self._level = level
        self._experience = experience
        self._max_exp = max_exp
        self._exp_per_attact = exp_per_attack

    # This method go againts OCP - because if we need to add another way to attack there will be to add another if conditional
    # def attack(self):
    #     if self._type == "fisico":
    #         print(f"{self.name} lanza un potente golpe")
    #     if self._type == "magico":
    #         print(f"{self._name} throw a Expelliarmus!!!!")
    
    @abstractmethod
    def attack(self):
        pass


class Warrior(Character):
    def __init__(self, name, exp_per_attack = 3):
        super().__init__(name, exp_per_attack = exp_per_attack)
        self._strong = 0
        self._resistance = 0
    
    def attack(self):
        print(f"{self._name} throw a strong hit!")
    

if __name__ == "__main__":
    firtsWarrior = Warrior('Fabian')
    firtsWarrior.attack()