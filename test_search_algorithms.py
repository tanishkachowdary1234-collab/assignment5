from search_algorithms import *


# TEST CASE 1 - WINNING MOVE

print("TEST CASE 1 : WINNING MOVE")

game = TicTacToe()

game.board = [
    "X", "X", " ",
    "O", "O", " ",
    " ", " ", " "
]

game.print_board()

print("Minimax Move:", best_move_minimax(game))
print("Alpha Beta Move:", best_move_alpha_beta(game))
print("Heuristic Alpha Beta Move:", best_move_heuristic(game))
print("MCTS Move:", monte_carlo_tree_search(game))

print("-" * 50)



# TEST CASE 2 - BLOCK OPPONENT

print("TEST CASE 2 : BLOCK OPPONENT")

game = TicTacToe()

game.board = [
    "O", "O", " ",
    "X", " ", " ",
    " ", "X", " "
]

game.print_board()

print("Minimax Move:", best_move_minimax(game))
print("Alpha Beta Move:", best_move_alpha_beta(game))
print("Heuristic Alpha Beta Move:", best_move_heuristic(game))
print("MCTS Move:", monte_carlo_tree_search(game))

print("-" * 50)



# TEST CASE 3 - EMPTY BOARD

print("TEST CASE 3 : EMPTY BOARD")

game = TicTacToe()

game.print_board()

print("Minimax Move:", best_move_minimax(game))
print("Alpha Beta Move:", best_move_alpha_beta(game))
print("Heuristic Alpha Beta Move:", best_move_heuristic(game))
print("MCTS Move:", monte_carlo_tree_search(game))

print("-" * 50)


# TEST CASE 4 - DRAW SITUATION

print("TEST CASE 4 : DRAW STATE")

game = TicTacToe()

game.board = [
    "X", "O", "X",
    "X", "O", "O",
    "O", "X", " "
]

game.print_board()

print("Minimax Move:", best_move_minimax(game))
print("Alpha Beta Move:", best_move_alpha_beta(game))
print("Heuristic Alpha Beta Move:", best_move_heuristic(game))
print("MCTS Move:", monte_carlo_tree_search(game))
