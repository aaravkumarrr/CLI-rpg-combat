from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health, max_health, attack_power):
        self.name = name
        self._health = health
        self.max_health = max_health
        self.attack_power = attack_power
    
    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, value):
        self._health = max(0, min(value, self.max_health))

    @abstractmethod
    def attack(self, target):
        pass

    @abstractmethod
    def special_ability(self, target):
        pass

    def take_damage(self, amount):
        self.health -= amount

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def __str__(self):
        return f"{self.name} | HP: {self.health}/{self.max_health}"
