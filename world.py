class Grid():
    def __init__(self, size):
        self._map = [[[]]*size]*size
    
    def move_player(self, player: object, direction):
        player.move(direction)
        
    def __str__(self):
        output_string = ""
        for item in self._map:
            output_string += str(item) + "\n"
        return output_string
        


test_grid=Grid(5)
print(test_grid)