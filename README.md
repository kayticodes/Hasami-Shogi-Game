# Hasami Shogi Game

## Overview
This project implements a Hasami Shogi game in Python. Hasami Shogi is a traditional Japanese board game similar to Shogi (Japanese chess) but played on a smaller board. The objective of the game is to capture your opponent's pieces or move your own pieces to your opponent's starting area.

## Features
- Creation of `HasamiShogiGame` object and movement of pieces from their initial positions
- Accurate tracking and enforcement of player turns
- Correct tracking of captured pieces per player
- Validation of all valid moves and prevention of invalid moves in all scenarios
- Accurate retrieval of the color of a piece occupying a square
- Identification of win conditions and prevention of moves after the game is won
- Detection and recording of custodian captures, including capturing multiple pieces in a row or making multiple separate captures at once

## Usage
To play the game, follow these steps:
1. Clone the repository:
git clone https://github.com/kayticodes/hasami-shogi-game.git
2. Navigate to the project directory:
cd hasami-shogi-game
3. Run the game:
python hasami_shogi_game.py


## Implementation Details
- The game logic is implemented in Python.
- Piece movements and capturing rules are enforced according to the Hasami Shogi ruleset, specifically "Variant 1" as described on the Wikipedia page.
- The game class (`HasamiShogiGame`) manages the game state, player turns, piece captures, and move validations.
- Moves can only be made diagonally and horizontally.
- Custodian captures and corner captures are correctly identified and recorded.
- The game prevents moves after a win condition is met.

## Code Structure
- The main game logic is contained within the `HasamiShogiGame` class.
- Each method within the class handles specific aspects of the game, such as checking game state, validating moves, and tracking captured pieces.

## Contributions
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request or open an issue.

## Credits
This project was developed by Catherine Martens for the CS 162 course portfolio project.

## License
This project is licensed under the [MIT License](LICENSE).
