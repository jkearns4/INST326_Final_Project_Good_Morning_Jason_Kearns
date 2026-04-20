class Player():
    def __init__(self, name: str, health: int) -> None:
        self._name = name
        self._health = health
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
        inv_string = f"Player {self.name}'s Inventory:\n"

        if not self._inventory:
            return "Empty"
        else:
            for clue in self._inventory:
                inv_string += f"{clue.name}\n"
            inv_string=inv_string[:-1]
            return inv_string
    
    @property
    def location(self):
        return self._location

        
    def show_status(self):
        return f"Player: {self.name}\nHealth: {self.health}\nInventory: {self.inventory}Location: {self.location}"
    
    def collect_clue(self, clue: object):
        self._inventory.append(clue)
    
    def take_damage(self, damage: int):
        self.health -= damage
        print(f"You ({self.name}) just took {damage} damage! You now have {self.health} health left!")
        
    def move(self, direction: str, units = 1: int):
        direction =  direction.lower()
        if not direction in ["up", "down", "left", "right"]:
            raise ValueError("Invalid input for moving")
        else:
            if direction == "up":
                self._location[1]+=units
            elif direction == "down":
                self._location[1]-=units
            elif direction == "left":
                self._location[0]-=units
            elif direction == "right":
                self._location[0]+=units
                
    


class Clue():
    def __init__(self, name: str, message: str):
        self._name = name
        self._message = message
        self._used = False
        
    @property
    def name(self):
        return self._name
    
    def show_clue(self):
        print(self._message)
        self.mark_used()
        
    def mark_used(self):
        self._used = True
        

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