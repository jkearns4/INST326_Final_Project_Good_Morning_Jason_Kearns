class Grid():
    def __init__(self, size):
        self._map = [[[]]*size]*size
    
    def move_player(self, player, direction):
        player.move(direction)

    def is_valid_move(self, location, direction):
        row = location[0]
        col = location[1]

        if direction == "up":
            self.is_in_bounds(row, col+1)
            col += 1
        elif direction == "down":
            self.is_in_bounds(row, col-1)
            col -= 1
        elif direction == "left":
            self.is_in_bounds(row-1, col)
            row -= 1
        elif direction == "right":
            self.is_in_bounds(row+1, col)
            row += 1
        else:
            return False

        return True 
        
    def __str__(self):
        output_string = ""
        for item in self._map:
            output_string += str(item) + "\n"
        return output_string

    def place_clue(self, row, col, clue):
        self.is_in_bounds(row, col)
        
        self._map[row][col].append(clue)
        
    def place_trap(self, row, col, trap):
        self.is_in_bounds(row, col)
        
        self._map[row][col].append(trap)
        
    def place_treasure(self, row, col, treasure):
        self.is_in_bounds(row, col)
        
        self._map[row][col].append(treasure)
    
    def search_location(self, player):
        row, col = player.location
        
        self.is_in_bounds(row, col)
        
        found_items = self._map[row][col][:]
        
        for item in found_items:
            if isinstance(item, Clue):
                player.collect_clue(item)
            elif isinstance(item, Trap):
                item.trigger(player)
            elif isinstance(item, Treasure):
                item.interact()
        
        self._map[row][col] = []
        return found_items
        
    def is_in_bounds(self, row, col):
        if not (0 <= row < len(self._map) and 0 <= col < len(self._map)):
            raise ValueError("This position is out of bounds.")
        
    

   
test_grid=Grid(5)
print(test_grid)
