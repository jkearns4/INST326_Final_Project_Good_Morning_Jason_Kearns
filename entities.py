import sys
from abc import ABC, abstractmethod

class Player():
    def __init__(self, name: str) -> None:
        self._name = name
        self._health = 100
        self._inventory = []
        self._location = [0,0]
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str):
            raise ValueError("Invalid value for name")
        self._name = new_name
    
    @property
    def health(self):
        return self._health
        
    @health.setter
    def health(self, new_health: int):
        if not isinstance(new_health, int):
            raise ValueError("Invalid value for health")
        self._health = new_health
        
    @property
    def inventory(self):
        self._inventory.sort(key=lambda c:c.name)
        inv_string = f"Player {self.name}'s Inventory:\n"

        if not self._inventory:
            return "Your inventory is empty.\n"
        else:
            for clue in self._inventory:
                inv_string += f"{clue.name}: {clue.message}\n"
            return inv_string
    
    @property
    def location(self):
        return self._location

    def show_status(self):
        return f"Player: {self.name}\nHealth: {self.health}\nInventory: {self.inventory}Location: {self.location}"
    
    def collect_clue(self, clue):
        self._inventory.append(clue)
        print(f"You ({self.name}) just found the {clue.name}! It has been added to your inventory")
    
    def take_damage(self, damage: int):
        self.health -= damage
        if self.health<=0: self.health=0
        print(f"You ({self.name}) just took {damage} damage! You now have {self.health} health left!")
        
            
            
    def move(self, direction: str):
        direction =  direction.lower()
        if not direction in ["up", "down", "left", "right"]:
            raise ValueError("Invalid input for moving")
        else:
            if direction == "up":
                self._location[0]-=1
            elif direction == "down":
                self._location[0]+=1
            elif direction == "left":
                self._location[1]-=1
            elif direction == "right":
                self._location[1]+=1
                
    
class Item(ABC):
    @abstractmethod
    def interact():
        """Initiate action with the item"""
        pass
    

class Clue(Item):
    def __init__(self, name: str, message: str):
        self._name = name
        self._message = message
        self._used = False
        
    @property
    def name(self):
        return self._name
    
    @property
    def message(self):
        return self._message
    
    def interact(self):
        print(self._message)
        self.mark_used()
        
    def mark_used(self):
        self._used = True


class Trap(Item):
    def __init__(self, name, damage):
        self._name = name
        self._damage = damage
    
    def interact(self, player):
        player.take_damage(self._damage)
    
    def __str__(self):
        return f"This is a {self._name} trap and it deals {self._damage} damage!"
    
    
class Treasure(Item):
    def __init__(self):
        self._message = "You have found the treasure! You win! Congratulations!"
    
    def interact(self):
        print(f"{self._message}")
        

"""
jones = Player("Jones", 100)
jones.take_damage(10)

direction_clue =  Clue("Direction", "The treasure is north from the starting point!")

jones.collect_clue(direction_clue)
print(jones.inventory)


jones.move("up")
jones.move("left")
print(jones.location)
"""
