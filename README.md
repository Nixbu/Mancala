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

## Contributing

Feel free to contribute to the improvement of this Mancala game. You can open an issue for bugs or suggestions, or fork the repository and create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
