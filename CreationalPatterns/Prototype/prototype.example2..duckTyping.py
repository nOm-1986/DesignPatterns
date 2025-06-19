import copy

class Monster:
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def attack(self): pass

  def clone(self):
    return copy.deepcopy(self)
  

# Mommy
class Mommy(Monster):
  def __init__(self, id: int, name: str, damage: int, bandage: int):
    super().__init__(id, name)
    self.damage = damage
    self.bandage = bandage

  def attack(self):
    print(f"Mummy {self.id} ({self.name}) attacks with {self.damage} and {self.bandage} (health) bandage of points")

# Vampire
class Vampire(Monster):
  def __init__(self, id: int, name: str, damage: int, bloodlust: int):
    super().__init__(id, name)
    self.damage = damage
    self.bloodlust = bloodlust
  
  def attack(self):
    print(f"Vampire {self.id} ({self.name}) attacks with {self.damage} and {self.bloodlust} (health) bloodlust of points")


# Zombie
class Zombie(Monster):
  def __init__(self, id: int, name: str, damage: int, health: int):
    super().__init__(id, name)
    self.damage = damage
    self.health = health
  
  def attack(self):
    print(f"Zombie {self.id} ({self.name}) attacks with {self.damage} and {self.health} health of points")


mommy = Mommy(1, 'Firts Mommy', 15, 250)
vampire = Vampire(2, 'Draculita', 25, 150)
zombie = Zombie(3, "Zombie 1",8, 400)
mommy.attack()
vampire.attack()
zombie.attack()
print("==="*15)

print("Using Mommy.clone() to implement Prototype pattern")
mommy_copied = mommy.clone()
mommy_copied.id = 4
mommy_copied.name = "2da Mommy"
mommy_copied.damage = 16
mommy_copied.attack()
mommy.attack()
print("==="*15)

print("Using Vampire.clone()")
vampire_c = vampire.clone()
vampire_c.id = 5
vampire_c.name = "Vampire 2"
vampire_c.damage = 30
vampire_c.bloodlust = 110
vampire_c.attack()
vampire.attack()
print("==="*15)

print("Using Zombie.clone()")
zombie_c = zombie.clone()
zombie_c.id = 6
zombie_c.name = "2snd Zombie"
zombie_c.damage = 10
zombie_c.health = 350
zombie_c.attack()
zombie.attack()