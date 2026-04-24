class Grid():
    def __init__(self, size):
        self._map = [[[]]*size]*size
    
    def move_player(self, player: object, direction):
        player.move(direction)

    def is_valid_move(self, location, direction):
        row = location[0]
        col = location[1]

        if direction == "up":
            col += 1
        elif direction == "down":
            col -= 1
        elif direction == "left":
            row -= 1
        elif direction == "right":
            row += 1
        else:
            return False

        return 0 <= row < len(self._map) and 0 <= col < len(self._map) 
        
    def __str__(self):
        output_string = ""
        for item in self._map:
            output_string += str(item) + "\n"
        return output_string
        
   
test_grid=Grid(5)
print(test_grid)
