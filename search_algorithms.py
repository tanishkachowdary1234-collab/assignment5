import math
import random
from copy import deepcopy

# TIC TAC TOE CLASS

class TicTacToe:

    def __init__(self):
        self.board = [" "] * 9

    def print_board(self):
        print()
        for i in range(0, 9, 3):
            print(self.board[i], "|", self.board[i+1], "|", self.board[i+2])
        print()


    def available_moves(self):
        moves = []

        for i in range(9):
            if self.board[i] == " ":
                moves.append(i)

        return moves

    def make_move(self, position, player):
        self.board[position] = player

    def undo_move(self, position):
        self.board[position] = " "

    def is_winner(self, player):

        winning_positions = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for combo in winning_positions:
            if (self.board[combo[0]] == player and
                self.board[combo[1]] == player and
                self.board[combo[2]] == player):
                return True

        return False

    def is_draw(self):
        return " " not in self.board


    def game_over(self):
        return (
            self.is_winner("X") or
            self.is_winner("O") or
            self.is_draw()
        )

# MINIMAX ALGORITHM

def minimax(game, maximizing_player):

    if game.is_winner("X"):
        return 1

    if game.is_winner("O"):
        return -1

    if game.is_draw():
        return 0

  
    if maximizing_player:

        best_score = -math.inf

        for move in game.available_moves():
            game.make_move(move, "X")

            score = minimax(game, False)

            game.undo_move(move)

            best_score = max(best_score, score)

        return best_score

  
    else:

        best_score = math.inf

        for move in game.available_moves():
            game.make_move(move, "O")

            score = minimax(game, True)

            game.undo_move(move)

            best_score = min(best_score, score)

        return best_score


def best_move_minimax(game):

    best_score = -math.inf
    best_move = None

    for move in game.available_moves():

        game.make_move(move, "X")

        score = minimax(game, False)

        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move

# ALPHA BETA PRUNING

def alpha_beta(game, alpha, beta, maximizing_player):

    if game.is_winner("X"):
        return 1

    if game.is_winner("O"):
        return -1

    if game.is_draw():
        return 0

    if maximizing_player:

        best_score = -math.inf

        for move in game.available_moves():
            game.make_move(move, "X")

            score = alpha_beta(game, alpha, beta, False)

            game.undo_move(move)

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            if beta <= alpha:
                break

        return best_score

    else:

        best_score = math.inf

        for move in game.available_moves():
            game.make_move(move, "O")

            score = alpha_beta(game, alpha, beta, True)

            game.undo_move(move)

            best_score = min(best_score, score)

            beta = min(beta, best_score)

            if beta <= alpha:
                break

        return best_score


def best_move_alpha_beta(game):

    best_score = -math.inf
    best_move = None

    for move in game.available_moves():

        game.make_move(move, "X")

        score = alpha_beta(
            game,
            -math.inf,
            math.inf,
            False
        )

        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# HEURISTIC FUNCTION

def evaluate_board(game):

    if game.is_winner("X"):
        return 100

    if game.is_winner("O"):
        return -100

    score = 0

    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_positions:

        values = [
            game.board[combo[0]],
            game.board[combo[1]],
            game.board[combo[2]]
        ]

        
        if values.count("X") == 2 and values.count(" ") == 1:
            score += 10

        
        if values.count("O") == 2 and values.count(" ") == 1:
            score -= 10

    return score

# HEURISTIC ALPHA BETA

def heuristic_alpha_beta(
        game,
        depth,
        alpha,
        beta,
        maximizing_player,
        max_depth=3):

    if depth == max_depth or game.game_over():
        return evaluate_board(game)

    if maximizing_player:

        best_score = -math.inf

        for move in game.available_moves():

            game.make_move(move, "X")

            score = heuristic_alpha_beta(
                game,
                depth + 1,
                alpha,
                beta,
                False,
                max_depth
            )

            game.undo_move(move)

            best_score = max(best_score, score)

            alpha = max(alpha, best_score)

            if beta <= alpha:
                break

        return best_score

    else:

        best_score = math.inf

        for move in game.available_moves():

            game.make_move(move, "O")

            score = heuristic_alpha_beta(
                game,
                depth + 1,
                alpha,
                beta,
                True,
                max_depth
            )

            game.undo_move(move)

            best_score = min(best_score, score)

            beta = min(beta, best_score)

            if beta <= alpha:
                break

        return best_score


def best_move_heuristic(game):

    best_score = -math.inf
    best_move = None

    for move in game.available_moves():

        game.make_move(move, "X")

        score = heuristic_alpha_beta(
            game,
            0,
            -math.inf,
            math.inf,
            False
        )

        game.undo_move(move)

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# MONTE CARLO TREE SEARCH 

def random_playout(game, current_player):

    temp_game = deepcopy(game)

    while not temp_game.game_over():

        move = random.choice(temp_game.available_moves())

        temp_game.make_move(move, current_player)

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

    if temp_game.is_winner("X"):
        return 1

    elif temp_game.is_winner("O"):
        return -1

    return 0


def monte_carlo_tree_search(game, simulations=300):

    move_scores = {}

    for move in game.available_moves():

        total_score = 0

        for _ in range(simulations):

            temp_game = deepcopy(game)

            temp_game.make_move(move, "X")

            result = random_playout(
                temp_game,
                "O"
            )

            total_score += result

        move_scores[move] = total_score

    best_move = max(move_scores, key=move_scores.get)

    return best_move
