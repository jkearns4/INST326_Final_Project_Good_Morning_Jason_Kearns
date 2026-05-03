import entities as e

class Grid():
    def __init__(self, size, player):
        self._real_map = [[[] for _ in range(size)] for _ in range(size)]
        self._visible_map = [[[] for _ in range(size)] for _ in range(size)]
        player._location = [size//2, size//2]
        self._visible_map[player.location[0]][player.location[1]] = ["P"]
    
    def move_player(self, player, direction):
        player.move(direction)
        self._visible_map[player.location[0]][player.location[1]] = ["P"]


    def is_valid_move(self, location, direction):
        row = location[0]
        col = location[1]

        if direction == "up":
            self.is_in_bounds(row-1, col)
        elif direction == "down":
            self.is_in_bounds(row+1, col)
        elif direction == "left":
            self.is_in_bounds(row, col-1)
        elif direction == "right":
            self.is_in_bounds(row, col+1)
        else:
            return False

        return True 
        
    def __str__(self):
        output_string = ""
        for item in self._visible_map:
            output_string += str(item) + "\n"
        return output_string

    def place_clue(self, row, col, clue):
        self.is_in_bounds(row, col)
        
        self._real_map[row][col].append(clue)
        
    def place_trap(self, row, col, trap):
        self.is_in_bounds(row, col)
        
        self._map[row][col].append(trap)
        
    def place_treasure(self, row, col, treasure):
        self.is_in_bounds(row, col)
        
        self._map[row][col].append(treasure)
    
    def search_location(self, player):
        row, col = player.location
        
        self.is_in_bounds(row, col)
        
        found_items = self._real_map[row][col][:]
        
        for item in found_items:
            if isinstance(item, e.Clue):
                player.collect_clue(item)
            elif isinstance(item, e.Trap):
                item.trigger(player)
            elif isinstance(item, e.Treasure):
                item.interact()
        
        self._real_map[row][col] = []
        self._visible_map[row][col] = ["x"]
        return found_items
        
    def is_in_bounds(self, row, col):
        if not (0 <= row < len(self._visible_map) and 0 <= col < len(self._visible_map)):
            raise ValueError("This position is out of bounds.")
        
    

test_player = e.Player("Jones", 100)
test_grid=Grid(5, test_player)
new_clue = e.Clue("Directional Clue", "The Treasure Is North!")
print(test_grid)
test_grid.place_clue(0, 0, new_clue)
print(test_grid)
test_grid.search_location(test_player)
print(test_grid)
test_grid.move_player(test_player, "up")
print(test_grid)


