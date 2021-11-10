from random import choice, random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      abilities: List
      name: String
      armors: List
      starting_health: Integer
      current_health: Integer
    '''
    # abilities and armors don't have starting values,
    # and are set to empty lists on initialization
    self.abilities = list()
    self.armors = list()
    # we know the name of our hero, so we assign it here
    self.name = name
    # similarly, our starting health is passed in, just like name
    self.starting_health = starting_health
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = starting_health
    self.deaths = 0
    self.kills = 0
  
  def fight(self, opponent):
    ''' Current Hero will take turns fighting the opponent hero passed in.
    '''
     total_power = self.current_health + opponent.current_health

        if self.abilities == [] and opponent.abilities == []:
            print('DRAW')
            return

        #run the fighting while both heros are still alive
        while self.is_alive() == True and opponent.is_alive() == True:
            print('fighting')
            self.take_damage(opponent.attack())
            #print(f'slf: {self.current_health}')
            opponent.take_damage(self.attack())
            #print(f'opp: {opponent.current_health}')

        #print the results if both players die at the same time
        if self.current_health <= 0 and opponent.current_health <= 0:
            print('DRAW')
            self.add_kill(1)
            opponent.add_kill(1)
            self.add_death(1)
            opponent.add_death(1)

        #if SELF is the winner
        elif self.current_health > opponent.current_health:
            print(f'{self.name} defeats {opponent.name}.')
            self.add_kill(1)
            opponent.add_death(1)

        #if OPPONENT is the winner
        else:
            print(f'{opponent.name} defeats {self.name}.')
            opponent.add_kill(1)
            self.add_death(1)
    # TODO: Refactor this method to update the following:
    # 1) the number of kills the hero (self) has when the opponent dies.
    # 2) then number of kills the opponent has when the hero (self) dies
    # 3) the number of deaths of the opponent if they die    in the fight
    # 4) the number of deaths of the hero (self) if they die in the fight
       
  def add_ability(self, ability):
    ''' Add ability to abilities list 
    '''
    # We use the append method to add ability objects to our list.
    self.abilities.append(ability)

  def attack(self):
    '''Calculate the total damage from all ability attacks.
        return: total_damage:Int
    '''
  # start our total out at 0
    total_damage = 0
        # loop through all of our hero's abilities
    for ability in self.abilities:
        # add the damage of each attack to our running total
        total_damage += ability.attack()
        # return the total damage
    return total_damage
  
  def add_armor(self, armor):
    '''Add armor to self.armors
    Armor: Armor Object
    '''
  # TODO: Add armor object that is passed in to `self.armors`
    self.armors.append(armor)
  
  def defend(self):
    '''Calculate the total block amount from all armor blocks.
    return: total_block:Int
    '''
  # TODO: This method should run the block method on each armor in self.armors
    total_defense = 0
    if self.current_health != 0:
        for armor in self.armors:
            total_defense += armor.block()
    return total_defense
  
  def take_damage(self, damage):
    '''Updates self.current_health to reflect the damage minus the defense.
    '''
    # TODO: Create a method that updates self.current_health to the current
    # minus the the amount returned from calling self.defend(damage).
    # number = self.defend()
    # damage = 7
    # print(number)
    self.current_health += self.defend()
    self.current_health -= damage
  
  def is_alive(self):  
    '''Return True or False depending on whether the hero is alive or not.
    '''
    # TODO: Check the current_health of the hero.
    # if it is <= 0, then return False. Otherwise, they still have health
    # and are therefore alive, so return True
    if self.current_health >= 0:
      print(f"{self.name} Alive!")
      return True
    else:
      print(f"{self.name} Died!")
      return False

  def add_weapon(self, weapon):
    '''Add weapon to self.abilities'''
    # TODO: This method will append the weapon object passed in as an
    # argument to self.abilities.
    # This means that self.abilities will be a list of
    # abilities and weapons.
    self.abilities.append(weapon)
  
  def add_kill(self, num_kills):
    ''' Update self.kills by num_kills amount'''
    self.kills += num_kills
  
  def add_death(self, num_deaths):
    ''' Update deaths with num_deaths'''
    # TODO: This method should add the number of deaths to self.deaths
    self.kills += num_deaths

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block of code is executed.
    hero1 = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero1.add_weapon(weapon)
    print(hero1.attack())

