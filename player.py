from character import Character
import random

class Player(Character):
    def __init__(self, name, health, max_health, attack_power):
        super().__init__(name, health, max_health, attack_power)

class Warrior(Player):
    def __init__(self, name):
        self.name = name
        self.health = 120
        self.attack_power = 15

        def special_ability(target):
            print(f"{self.name} used Shield Bash!")
            target.take_damage(1.5*self.attack_power)
        
        def attack(target):
            print(self.name, " attacked ", target.name, " and dealt ", self.attack_power, " damage.")

class Mage(Player):
    ability_used = False
    
    def __init__(self, name):
        self.name = name
        self.health = 70
        self.attack_power = 25

    def special_ability(self, target):
        if not self.ability_used:
            print(f"{self.name} used Fireball!")
            target.take_damage(self.attack_power * 4)
            ability_used = True
    
    def attack(self, target):
        target.take_damage(self.attack_power)
        print(self.name, " attacked ", target.name, " and dealt ", self.attack_power, " damage.")
        

class Rogue(Player):

    def __init__(self, name):
        self.name = name
        self.health = 90
        self.attack_power = 18
    
    def special_ability(self, target):

        print(f"{self.name} used Critical Strike!")
        def damage():
            chance = random.randint(0,10)
            if chance <=4:
                return 3*self.attack_power
            else:
                return self.attack_power
        target.take_damage(damage())

    def attack(self, target):
        target.take_damage(self.attack_power)
        print(self.name, " attacked ", target.name, " and dealt ", self.attack_power, " damage.")
    