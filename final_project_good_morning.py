class Player():
    def __init__(self, name, health):
        self._name = name
        self._health = health
        self._inventory = []
        self._location = [0,0]
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Invalid value for name")
        self._name = new_name
    
    @property
    def health(self):
        return self._health
        
    @health.setter
    def health(self, new_health):
        if not isinstance(new_health, int):
            raise ValueError("Invalid value for health")
        self._health = new_health
        
    @property
    def inventory(self):
        inv_string = ""
        for clue in self._inventory:
            inv_string += f"{clue.name}\n"
        return inv_string
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, axis, units):
        if not isinstance(axis, str):
            raise ValueError("Invalid value for axis")
        
        axis = axis.lower()
        
        if not axis in ["x", "y"]:
            raise ValueError("Invalid value for axis")
        
        if axis = "x":
            self._location[0]+=units
        else:
            self._location[1]+=units
        
        
        
    def show_status(self):
        return f"Player {self.name}:\nHealth: {self.health}\nInventory: {self.inventory}\nLocation: {self.location}"
    
    def collect_clue(self, clue):
        self._inventory.append(clue)
    
    def take_damage(self, damage):
        self.health -= damage
        print(f"You ({name}) just took {damage} damage!")
        
    def move(self, direction):
        direction =  direction.lower()
        if not direction in ["up", "down", "left", "right"]:
            raise ValueError("Invalid input for moving")
        else:
            if direction = "up":
                self.location+=1
                
    


class Clue():
    def __init__(self, name, message, used):
        self._name = name
        self._message = message
        self._used = used
        
    @property
    def name(self):
        return self._name
    
    def show_clue(self):
        print(self._message)
        self.mark_used()
        
    def mark_used(self):
        self._used = True
        
