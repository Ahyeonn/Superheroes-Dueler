from random import choice, random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  def __init__(self, name, starting_health=100):
    self.abilities = list()
    self.armors = list()
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health
    self.deaths = 0
    self.kills = 0
  
  def fight(self, opponent):
    if len(self.abilities) > 0 or len(opponent.abilities) > 0:
      while True:
        if self.is_alive():
          attack_damage = self.attack()
          opponent.take_damage(attack_damage)
        else:
          print(f"\n{opponent.name} won!")
          print(f"{self.name} lost!")
          self.add_death(1)
          opponent.add_kill(1)
          break

        if opponent.is_alive():
          attack_damage = opponent.attack()
          self.take_damage(attack_damage)
        else:
          print(f"\n{self.name} won!")
          print(f"{opponent.name} lost!")
          opponent.add_death(1)
          self.add_kill(1)
          break
        
    else:
      print("Draw")
       
  def add_ability(self, ability):
    self.abilities.append(ability)
  
  def add_weapon(self, weapon):
    self.abilities.append(weapon)

  def attack(self):
    total_damage = 0
    for ability in self.abilities:
        total_damage += ability.attack()
    return total_damage
  
  def add_armor(self, armor):
    self.armors.append(armor)
  
  def defend(self):
    total_armor = 0
    for armor in self.armors:
        total_armor += armor.block()
    return total_armor
  
  def take_damage(self, damage):
    self.current_health += self.defend()
    self.current_health -= damage
  
  def is_alive(self):  
    return self.current_health > 0
  
  def add_kill(self, num_kills):
    self.kills += num_kills
  
  def add_death(self, num_deaths):
    self.deaths += num_deaths


