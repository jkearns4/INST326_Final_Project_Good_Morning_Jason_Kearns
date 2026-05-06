import entities as e
import random

class Grid():
    def __init__(self, size, player):
        self._real_map = [[[] for _ in range(size)] for _ in range(size)]
        self._visible_map = [[[" "] for _ in range(size)] for _ in range(size)]
        player._location = [size//2, size//2]
        self._visible_map[player.location[0]][player.location[1]] = ["P"]
        
    
    def move_player(self, player, direction):
        if not self.is_valid_move(player.location, direction):
            print("You can't move that way.")
            return False

        old_row, old_col = player.location
        self._visible_map[old_row][old_col] = ["x"]

        player.move(direction)

        new_row, new_col = player.location
        self._visible_map[new_row][new_col] = ["P"]
        self.location_collision(player)
        return True


    def is_valid_move(self, location, direction):
        row = location[0]
        col = location[1]

        if direction == "up":
            return self.is_in_bounds(row-1, col)    
        elif direction == "down":
            return self.is_in_bounds(row+1, col)
        elif direction == "left":
            return self.is_in_bounds(row, col-1)
        elif direction == "right":
            return self.is_in_bounds(row, col+1)
        else:
            return False
        
        
    def __str__(self):
        output_string = ""
        for item in self._visible_map:
            output_string += str(item) + "\n"
        return output_string

    def place_clue(self, row, col, clue):
        if not self.is_in_bounds(row, col):
            raise ValueError("Invalid grid location.")

        self._real_map[row][col].append(clue)

        
    def place_trap(self, row, col, trap):
        if not self.is_in_bounds(row, col):
            raise ValueError("Invalid grid location.")

        self._real_map[row][col].append(trap)
        
    def place_treasure(self, row, col, treasure):
        if not self.is_in_bounds(row, col):
            raise ValueError("Invalid grid location.")

        self._real_map[row][col].append(treasure)
    
    def location_collision(self, player):
        row, col = player.location
        
        if not self.is_in_bounds(row, col):
            raise ValueError("Player is outside the grid.")
    
        found_items = self._real_map[row][col][:]
        
        for item in found_items:
            if isinstance(item, e.Treasure):
                self._visible_map[row][col]="!"
                item.interact()
            elif isinstance(item, e.Trap):
                item.trigger(player)
            elif isinstance(item, e.Clue):
                item.show_clue()
                player.collect_clue(item)
        
        
        self._real_map[row][col] = []
        return found_items
    
        
    def is_in_bounds(self, row, col):
        if not (0 <= row < len(self._visible_map) and 0 <= col < len(self._visible_map)):
            return False
        
        return True
        
    def generate_entities(self):
        size = len(self._real_map)

        available_locations = [
            [row, col]
            for row in range(size)
            for col in range(size)
        ]
        
        #Shouldn't place objects at starting position. 
        available_locations.remove([2, 2])

        treasure_location = random.choice(available_locations)
        available_locations.remove(treasure_location)
        self.place_treasure(treasure_location[0], treasure_location[1], e.Treasure())

        clue_messages = [
            f"The treasure is on row {treasure_location[0]+1}.",
            "Watch your step. Some spaces may have traps.",
            f"The treasure is on column {treasure_location[1]+1}"
        ]

        for i in range(3):
            clue_location = random.choice(available_locations)
            available_locations.remove(clue_location)

            clue = e.Clue(f"Clue {i + 1}", clue_messages[i])
            self.place_clue(clue_location[0], clue_location[1], clue)

        for i in range(int((len(self._real_map)**2)*0.2)):
            trap_location = random.choice(available_locations)
            available_locations.remove(trap_location)

            trap = e.Trap(f"Trap {i + 1}", 20)
            self.place_trap(trap_location[0], trap_location[1], trap)
    
"""
test_player = e.Player("Jones")
test_grid=Grid(5, test_player)
new_clue = e.Clue("Directional Clue", "The Treasure Is North!")
new_trap = e.Trap("Spike Trap", 20)
new_treasure = e.Treasure()
test_grid.place_clue(1, 2, new_clue)
test_grid.place_trap(1, 2, new_trap)
test_grid.place_treasure(1, 2, new_treasure)
test_grid.location_collision(test_player)
print(test_grid)
test_grid.move_player(test_player, "up")
print(test_grid)
test_grid.move_player(test_player, "down")
print(test_grid)
print(test_player.inventory)
"""

