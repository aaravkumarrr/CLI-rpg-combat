from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health, max_health, attack_power):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack_power = attack_power
    
    @abstractmethod
    def attack():
        pass

    @abstractmethod
    def special_ability():
        pass

    def take_damage(self,amount):
        self.health = max(0, self.health - amount)

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.name} | HP: {self.health}/{self.max_health} | Power: {self.attack_power}"