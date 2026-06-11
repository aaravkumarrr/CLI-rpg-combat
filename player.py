import character
import random

class Warrior(character.Character):
    def __init__(self, name):
        self.max_health = 120
        self.health = 120
        self.attack_power = 15
        super().__init__(name, self.health, self.max_health, self.attack_power)
    
    def attack(self, target):
        print(f"{self.name} attacked {target.name}")
        target.take_damage(self.attack_power)
    
    def special_ability(self, target):
        print(f"{self.name} used Shield Bash on {target.name}")
        target.take_damage(self.attack_power * 1.5)

class Mage(character.Character):
    def __init__(self, name):
        self.max_health = 70
        self.health = 70
        self.attack_power = 25
        self.fireball_used = False
        super().__init__(name, self.health, self.max_health, self.attack_power)
    
    def attack(self, target):
        print(f"{self.name} attacked {target.name}")
        target.take_damage(self.attack_power)
    
    def special_ability(self, target):
        if not self.fireball_used:
            print(f"{self.name} used Fireball on {target.name}")
            target.take_damage(self.attack_power * 2)
            self.fireball_used = True
        else:
            print("Fireball has been used already.")

class Rogue(character.Character):
    def __init__(self, name):
        self.max_health = 70
        self.health = 90
        self.attack_power = 18
        super().__init__(name, self.health, self.max_health, self.attack_power)
    
    def attack(self, target):
        print(f"{self.name} attacked {target.name}")
        target.take_damage(self.attack_power)
    
    def special_ability(self, target):
        print(f"{self.name} used Critical Strike on {target.name}")
        chance = random.randint(1,10)
        if chance <= 4:
            print(f"It worked!")
            target.take_damage(self.attack_power * 3)
        else:
            print("It failed!")
            target.take_damage(self.attack_power)
