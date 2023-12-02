from .SimulatedBoard import *
from math import inf

class AIPlayer:
    def __init__(self, board, depth, player):
        self.board = board
        self.depth = depth

    def choose_best_move(self):
        best_move = -1
        best_eval = -inf
        sim_board = SimulatedBoard(self.board, False)

        for move in range(6):
            if sim_board.current_pits[move] != 0:
                new_sim_board = sim_board.create_copy()
                new_sim_board.make_move(move)
                evaluation = minimax(new_sim_board, self.depth, True)

                if evaluation > best_eval:
                    best_eval = evaluation
                    best_move = move

        return best_move

def minimax(sim_board, depth, maximizing_player):
    """
    Minimax algorithm to determine the best move in a mancala game
    :param sim_board: SimulatedBoard object, to simplify the board state
    :param depth: How many moves into the future to check
    :param maximizing_player: To know if it needs to maximize or minimize evaluation
    :return:
    """
    if depth == 0 or sim_board.is_over():
        return sim_board.evaluate()

    if maximizing_player:
        max_eval = -inf
        for move in range(6):
            if sim_board.current_pits[move] != 0:
                sim_board.make_move(move)
                evaluation = minimax(sim_board, depth - 1, sim_board.turn)
                max_eval = max(max_eval, evaluation)

        return max_eval

    else:
        min_eval = inf
        for move in range(6):
            if sim_board.current_pits[move] != 0:
                sim_board.make_move(move)
                evaluation = minimax(sim_board, depth - 1, sim_board.turn)
                min_eval = min(min_eval, evaluation)

        return min_eval
