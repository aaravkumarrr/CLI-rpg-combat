import character
import random

class Enemy(character.Character):
    def take_turn(self, target):
        action = random.choice([self.attack,self.special_ability])
        action(target)
    

class Goblin(Enemy):
    def __init__(self):
        self.name = "Goblin"
        self.max_health = 50
        self.health = 50
        self.attack_power = 8
        super().__init__(self.name, self.health, self.max_health, self.attack_power)
    
    def attack(self, target):
        print(f"{self.name} attacked {target.name}")
        target.take_damage(self.attack_power)
    
    def special_ability(self, target):
        print(f"{self.name} dodges the attack.")

class Dragon(Enemy):
    def __init__(self):
        self.name = "Dragon"
        self.max_health = 200
        self.health = 200
        self.attack_power = 20
        super().__init__(self.name, self.health, self.max_health, self.attack_power)
    
    def attack(self, target):
        print(f"{self.name} attacked {target.name}")
        target.take_damage(self.attack_power)

    def special_ability(self, target):
        print(f"{self.name} breathes fire.")
        target.take_damage(self.attack_power * 2)

