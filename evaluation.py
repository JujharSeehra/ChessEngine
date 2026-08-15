import math
import allFunctions 

def evaluate_board(board, is_valid_move, move_leaves_king_in_check, is_in_check, can_attack_square):

    score = 0.0

    game_phase = allFunctions.calculate_game_phase(board)

    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if piece == 0:
                continue

            score += allFunctions.pieceValues[piece]

            table = allFunctions.get_piece_table(piece)

            if piece > 0:
                score += table[row][col]
            else:
                score -= table[7 - row][col]

    score += allFunctions.evaluate_mobility(board, is_valid_move, move_leaves_king_in_check, game_phase)

    score += allFunctions.evaluate_king_safety(board, is_in_check, can_attack_square, game_phase)

    score += allFunctions.evaluate_pawn_structure(board, game_phase)

    score += allFunctions.evaluate_king_activity(board, game_phase)

    score += allFunctions.evaluate_bishop_pair(board)

    return round(score, 2)