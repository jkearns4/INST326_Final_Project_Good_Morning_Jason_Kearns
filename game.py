import argparse
import world as w
import entities as e

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
    
    print(f"Starting a game for player {args.player_name} on a {args.size} by {args.size} grid\nThe valid are directions (up/down/left/right)")
    
    player = e.Player(args.player_name)
    grid = w.Grid(args.size, player)
    
    grid.generate_entities()

    while True:
        print(grid)
        user_input = input("Input a move to make on the grid: ")
        while not grid.is_valid_move(player.location, user_input):
            user_input = input("That is not a valid input, please enter a valid input here: ")
        grid.move_player(player, user_input)
         

if __name__ == "__main__":
    main()
