import argparse
import world as w
import entities as e
import sys

def parse_args():
    """Parses through user arguments to pass through the main function
    
    Author: Andy Huang
    """
    parser = argparse.ArgumentParser(description="Grid Game")
    parser.add_argument("--size", type=int, default=5, help="Grid size")
    parser.add_argument("--player-name", type=str, default="Player")
    return parser.parse_args()


def main():
    args = parse_args()
    
    print(f"Starting a game for player {args.player_name} on a {args.size} by {args.size} grid\nThe valid directions to move are (up/down/left/right)\nYou can also check your collected clues with 'inventory'")
    
    player = e.Player(args.player_name)
    grid = w.Grid(args.size, player)
    
    grid.generate_entities()
    """Checks if the player is on the tile with the treasure"""
    while player.location != grid.goal_tile:
        """If the player has no more health they die and the program exits"""
        if player.health<=0:
            print("You lost all your health! Game over!")
            sys.exit()
        
        print(grid)
        
        """Reads the users input for action"""
        user_input = input("Input an action: ")
        
        """If the user input is not valid, keep asking until a valid action is recieved"""
        while (not grid.is_valid_move(player.location, user_input)) and user_input.lower() != "inventory":
            user_input = input("That is not a valid input, please enter a valid input here: ")
        
        """Evaluate the action depending on the input"""
        grid.move_player(player, user_input) if user_input.lower() != "inventory" else print(player.inventory)
        

if __name__ == "__main__":
    main()
