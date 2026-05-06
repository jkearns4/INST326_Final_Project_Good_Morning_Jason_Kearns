# INST326_Final_Project_Good_Morning_Jason_Kearns
INST326 Spring Group 19 "Good Morning" 


# Treasure Hunt Grid Game

## Game Description

This project is a grid-based treasure hunt game. The player starts in the middle of a hidden grid and moves around by typing directions. The objective is to find the treasure before losing all of their health.

In the game it has hidden treasure, traps, and clues. If the player lands on a trap, they lose health. If the player lands on a clue, the clue message is shown and the clue is added to the player’s inventory. If the player finds the treasure, the game ends with a win message.

The game is supposed to be able to be played again because the treasure, clues, and traps are randomly placed each time the game starts.

## Purpose of Each File

### game.py

This file runs the main game. It handles command line arguments, creates the player, creates the grid, generates the hidden objects, and starts the main game loop where the user enters movement commands.

### world.py

This file controls the game board. It contains the Grid class, which stores the hidden map and the visible map. It handles movement checking, placing treasure, placing clues, placing traps, checking what happens when the player lands on a space, and randomly generating entities.

### entities.py

Inside this file, it contains the main objects used in the game. The Player class stores the player’s name, health, inventory, and location. The Clue class stores clue messages. The Trap class damages the player. The Treasure class ends the game when found.

## How to Run the Program

Open the terminal in the project folder and run:

python game.py

Players have ability to choose a grid size and player name:

python game.py --size 7 --player-name Joe

If no options are given, the game uses a default grid size of 5 and the player name "Player."

## How to Use the Program

When the game starts, the player is placed in the middle of the grid. 

On the visible map, "P" means the player’s current location. An "x" means a space the player already visited. A blank space means the player has not visited that location yet.

To move, type one of these commands:

up
down
left
right

If a player goes outside the grid, the program asks for another input. When the player lands on a clue, the clue message is printed and the clue is added to the player’s inventory. If the player lands on a trap, the player loses health. If the player’s health reaches 0, the game ends. If the player finds the treasure, the player wins.

## Attribution Table


Method    Primary Author   Technique Claimed





## Annotated Bibliography
















































