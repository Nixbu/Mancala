# Mancala Game

Welcome to the Mancala game! This is a Python implementation of the Mancala board game with options for two people to play together, play against an AI, or watch AI vs. AI simulations.

## Features

- **Player vs. Player:** Challenge a friend to a classic game of Mancala.
- **AI vs. Player:** Test your skills against a computer player using the Minimax algorithm with alpha-beta pruning.
- **AI vs. AI Simulation:** Watch two AI players battle it out in a simulated game.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Nixbu/Mancala.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Mancala
   ```

3. Run the game:

   ```bash
   python Mancala.py
   ```

## How to Play

- The game starts with a board containing six stones in each pit.
- Players take turns choosing a pit and distributing its stones counterclockwise.
- The game continues until one player's side is empty.
- The winner is the player with the bigger amount of stones when the game ends.

## AI Algorithm

The AI player is implemented using the Minimax algorithm with alpha-beta pruning. This ensures optimal decision-making and efficient computation, making the AI a challenging opponent.

## File Structure

The project follows the following file structure:

- **`Mancala.py`**: Main script to run the Mancala game.

- **`License`**: MIT License file specifying the terms under which the software is distributed.

- **`README.md`**: Project documentation providing an overview, instructions, and information about the file structure.

### classes/
- **`AI_Player.py`**: Class representing an AI player using the Minimax algorithm with alpha-beta pruning. It includes methods for choosing the best move and the Minimax algorithm.

- **`Bead.py`**: Class representing a bead in the game. It includes methods for drawing and updating the bead.

- **`Board.py`**: Class representing the Mancala game board. It includes methods for initializing the board, making moves, and drawing the board.

- **`Button.py`**: Class representing a button in the game. It includes methods for drawing the button and checking if it's clicked.

- **`CirclePit.py`**: Class representing a circular pit in the game. It extends the `Pit` class and includes methods for drawing and updating bead positions.

- **`Game.py`**: Class representing the Mancala game. It includes methods for drawing the game, making moves, and checking game-related conditions.

- **`Pit.py`**: Class representing a pit in the game. It includes methods for removing beads and checking if a pit is clicked.

- **`SimulatedBoard.py`**: Class representing a simplified board state for AI simulation. It includes methods for initializing, making moves, and evaluating the board state.

- **`Store.py`**: Class representing a store in the game. It extends the `Pit` class and includes methods for drawing and updating bead positions.

### utils/
- **`__init__.py`**: Initialization file for the utils package.

- **`Settings.py`**: Configuration file containing settings and paths used in the game. It includes settings for the screen, backgrounds, beads, pits, stores, fonts, and colors.

Feel free to explore each file for detailed documentation on its functionality and implementation details.

## Contributing

Feel free to contribute to the improvement of this Mancala game. You can open an issue for bugs or suggestions, or fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project Images
### Main Screen
![alt text](https://raw.githubusercontent.com/Nixbu/Mancala/master/Images/main_screen.PNG)

### AI vs Player Game
![alt text](https://raw.githubusercontent.com/Nixbu/Mancala/master/Images/aivsp2.PNG)

### Player vs Player Game


### AI vs AI Game
![alt text](https://raw.githubusercontent.com/Nixbu/Mancala/master/Images/aivsai.PNG)
