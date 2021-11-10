import random
from ability import Ability
class Weapon(Ability):
  def attack(self):
    random_value = random.randint((self.max_damage//2),self.max_damage)
    return random_value


