from character import Character
import random

class Enemy(Character):
    def __init__(self, name, health, max_health, attack_power):
        super().__init__(name, health, max_health, attack_power)
    
    def taketurn(self, target):
        pass
    
class Goblin(Enemy):
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.attack_power = 8

    def attack(self, target):
        print("Goblin has struck!")
        target.take_damage(self.attack_power)
        print("Goblin has struck again!")
        target.take_damage(self.attack_power)       

    def special_ability():
        print("Goblin dodges the attack.")
        pass 