import math

pieceArray = [
    [-5,-4,-3,-2,-6,-3,-4,-5],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0, 0, 0, 0],
    [ 1, 1, 1, 1, 1, 1, 1, 1],
    [ 5, 4, 3, 2, 6, 3, 4, 5]
]

pieceValues = {
    1 : 1,
    4 : 3,
    3 : 3,
    5 : 5,
    2 : 9,
    6 : 0,
    
    -1 : -1,
    -2: -9,
    -3: -3,
    -4: -3,
    -5: -5,
    -6: 0,
}

KING_ENDGAME_TABLE = [
    [-0.5, -0.4, -0.3, -0.2, -0.2, -0.3, -0.4, -0.5],
    [-0.3, -0.2, -0.1, -0.0, -0.0, -0.1, -0.2, -0.3],
    [-0.2, -0.1,  0.1,  0.2,  0.2,  0.1, -0.1, -0.2],
    [-0.1,  0.0,  0.2,  0.3,  0.3,  0.2,  0.0, -0.1],
    [-0.1,  0.0,  0.2,  0.3,  0.3,  0.2,  0.0, -0.1],
    [-0.2, -0.1,  0.1,  0.2,  0.2,  0.1, -0.1, -0.2],
    [-0.3, -0.2, -0.1,  0.0,  0.0, -0.1, -0.2, -0.3],
    [-0.5, -0.4, -0.3, -0.2, -0.2, -0.3, -0.4, -0.5]
]

PAWN_TABLE = [
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.1, 0.1, 0.2, 0.3, 0.3, 0.2, 0.1, 0.1],
    [0.05, 0.05, 0.1, 0.25, 0.25, 0.1, 0.05, 0.05],
    [0.0, 0.0, 0.0, 0.2, 0.2, 0.0, 0.0, 0.0],
    [0.05, -0.05, -0.1, 0.0, 0.0, -0.1, -0.05, 0.05],
    [0.05, 0.1, 0.1, -0.2, -0.2, 0.1, 0.1, 0.05],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
]


KNIGHT_TABLE = [
    [-0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5],
    [-0.4, -0.2, 0.0, 0.0, 0.0, 0.0, -0.2, -0.4],
    [-0.3, 0.0, 0.2, 0.25, 0.25, 0.2, 0.0, -0.3],
    [-0.3, 0.05, 0.25, 0.3, 0.3, 0.25, 0.05, -0.3],
    [-0.3, 0.0, 0.25, 0.3, 0.3, 0.25, 0.0, -0.3],
    [-0.3, 0.05, 0.2, 0.25, 0.25, 0.2, 0.05, -0.3],
    [-0.4, -0.2, 0.0, 0.05, 0.05, 0.0, -0.2, -0.4],
    [-0.5, -0.4, -0.3, -0.3, -0.3, -0.3, -0.4, -0.5]
]


BISHOP_TABLE = [
    [-0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2],
    [-0.1, 0.0, 0.0, 0.05, 0.05, 0.0, 0.0, -0.1],
    [-0.1, 0.0, 0.05, 0.1, 0.1, 0.05, 0.0, -0.1],
    [-0.1, 0.05, 0.05, 0.1, 0.1, 0.05, 0.05, -0.1],
    [-0.1, 0.0, 0.1, 0.1, 0.1, 0.1, 0.0, -0.1],
    [-0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, -0.1],
    [-0.1, 0.05, 0.0, 0.0, 0.0, 0.0, 0.05, -0.1],
    [-0.2, -0.1, -0.1, -0.1, -0.1, -0.1, -0.1, -0.2]
]


ROOK_TABLE = [
    [0.0, 0.0, 0.0, 0.05, 0.05, 0.0, 0.0, 0.0],
    [0.0, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.0],
    [0.0, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.05, 0.05, 0.0, 0.0, 0.05, 0.05, 0.0],
    [0.0, 0.05, 0.05, 0.0, 0.0, 0.05, 0.05, 0.0],
    [0.0, 0.0, 0.0, 0.05, 0.05, 0.0, 0.0, 0.0]
]


QUEEN_TABLE = [
    [-0.2, -0.1, -0.1, 0.0, 0.0, -0.1, -0.1, -0.2],
    [-0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1],
    [-0.1, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1],
    [0.0, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, 0.0],
    [0.0, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, 0.0],
    [-0.1, 0.0, 0.05, 0.05, 0.05, 0.05, 0.0, -0.1],
    [-0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1],
    [-0.2, -0.1, -0.1, 0.0, 0.0, -0.1, -0.1, -0.2]
]


KING_TABLE = [
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.3, -0.4, -0.4, -0.5, -0.5, -0.4, -0.4, -0.3],
    [-0.2, -0.3, -0.3, -0.4, -0.4, -0.3, -0.3, -0.2],
    [-0.1, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.1],
    [0.0, -0.1, -0.1, 0.0, 0.0, -0.1, -0.1, 0.0],
    [0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1],
    [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
    [0.2, 0.3, 0.1, 0.0, 0.0, 0.1, 0.3, 0.2]
]

def evaluate_board(board, is_valid_move, move_leaves_king_in_check, is_in_check, can_attack_square):

    score = 0.0

    game_phase = calculate_game_phase(board)

    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if piece == 0:
                continue

            score += pieceValues[piece]

            table = get_piece_table(piece)

            if piece > 0:
                score += table[row][col]
            else:
                score -= table[7 - row][col]

    score += evaluate_mobility(board, is_valid_move, move_leaves_king_in_check, game_phase)

    score += evaluate_king_safety(board, is_in_check, can_attack_square, game_phase)

    score += evaluate_pawn_structure(board, game_phase)

    score += evaluate_king_activity(board, game_phase)

    score += evaluate_bishop_pair(board)

    return round(score, 2)

def get_piece_table(piece, game_phase = 1.0):
    piece_type = abs(piece)
    if piece_type == 1:
        return PAWN_TABLE

    if piece_type == 2:
        return QUEEN_TABLE

    if piece_type == 3: 
        return BISHOP_TABLE

    if piece_type == 4:
        return KNIGHT_TABLE

    if piece_type == 5:
        return ROOK_TABLE

    if piece_type == 6:
        return KING_TABLE

    return None

def evaluate_mobility(board, is_valid_move, move_leaves_king_in_check, game_phase):

    white_moves = 0
    black_moves = 0

    for old_row in range(8):
        for old_col in range(8):

            piece = board[old_row][old_col]

            if piece == 0:
                continue

            if piece > 0:
                player = 1

            else:
                player = -1

            for new_row in range(8):
                for new_col in range(8):

                    if is_valid_move(old_row, old_col, new_row, new_col, check_turn=False):

                        if not move_leaves_king_in_check(old_row, old_col, new_row, new_col):

                            if player == 1:
                                white_moves += 1
                            else:
                                black_moves += 1

    mobility_difference = white_moves - black_moves

    mobility_weight = 0.015 + (game_phase * 0.01)
    return mobility_difference * mobility_weight


def find_king(board, king):

    for row in range(8):
        for col in range(8):

            if board[row][col] == king:
                return row, col

    return None


def king_attack_count(board, king, can_attack_square):

    king_position = find_king(board, king)

    if king_position is None:
        return 0

    king_row, king_col = king_position

    enemy = -1 if king == 6 else 1

    count = 0

    for row_change in [-1, 0, 1]:
        for col_change in [-1, 0, 1]:

            if row_change == 0 and col_change == 0:
                continue

            row = king_row + row_change
            col = king_col + col_change

            if 0 <= row < 8 and 0 <= col < 8:

                if can_attack_square(row, col, enemy):
                    count += 1

    return count

def evaluate_king_safety(board, is_in_check, can_attack_square, game_phase):
    score = 0.0
    safety_multiplier = 0.5 + (game_phase * 0.5)
    if is_in_check(6):
        score -= 0.8 * safety_multiplier
    white_attacked = king_attack_count(board, 6, can_attack_square)
    score -= white_attacked * 0.15 * safety_multiplier

    if is_in_check(-6):
        score += 0.8 * safety_multiplier
    black_attacked = king_attack_count(board, -6, can_attack_square)

    score += black_attacked * 0.15 * safety_multiplier

    return score


def is_passed_pawn(board, row, col):

    piece = board[row][col]

    if abs(piece) != 1:
        return False

    if piece > 0:

        for check_row in range(0, row):

            for check_col in range(
                max(0, col - 1),
                min(8, col + 2)
            ):

                if board[check_row][check_col] == -1:
                    return False

    else:

        for check_row in range(row + 1, 8):

            for check_col in range(
                max(0, col - 1),
                min(8, col + 2)
            ):

                if board[check_row][check_col] == 1:
                    return False

    return True

def evaluate_passed_pawns(board, game_phase):
    score = 0.0 
    endgame_multiplier = 1.0 + (1.0 - game_phase)
    for row in range(8):
        for col in range(8):
            piece = board[row][col]

            if abs(piece) != 1:
                continue

            if not is_passed_pawn(board, row, col):
                continue
            if piece > 0: 
                advancement = 7 - row
                score += (0.15 + advancement * 0.05) * endgame_multiplier
            else:
                advancement = row
                score -= (0.15 + advancement * 0.05) * endgame_multiplier
    return score

def evaluate_doubled_pawns(board):
    score = 0.0 
    for col in range(8):
        white_pawns = 0
        black_pawns = 0
        for row in range(8):
            if board[row][col] == 1:
                white_pawns += 1
            elif board[row][col] == -1:
                black_pawns += 1
        if white_pawns > 1:
            score -= (white_pawns - 1) * 0.15
        if black_pawns > 1:
            score += (black_pawns - 1) * 0.15
    return score

def is_isolated_pawn(board, row, col):

    piece = board[row][col]

    if abs(piece) != 1:
        return False

    for adjacent_col in [col - 1, col + 1]:

        if not 0 <= adjacent_col < 8:
            continue

        for check_row in range(8):

            if board[check_row][adjacent_col] == piece:
                return False

    return True

def evaluate_isolated_pawns(board):

    score = 0.0

    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if abs(piece) != 1:
                continue

            if is_isolated_pawn(board, row, col):

                if piece > 0:
                    score -= 0.15
                else:
                    score += 0.15

    return score

def evaluate_connected_pawns(board):
    score = 0.0 
    for row in range(8):
        for col in range(8):

            piece = board[row][col]

            if abs(piece) != 1:
                continue

            for adjacent_col in [col -1, col + 1]:
                if not 0 <= adjacent_col < 8:
                    continue
                if board[row][adjacent_col] == piece:
                    if piece > 0: 
                        score += 0.05
                    elif piece < 0:
                        score -= 0.05
                    break
    return score


def evaluate_pawn_structure(board, game_phase):

    score = 0.0

    score += evaluate_passed_pawns(board, game_phase)
    score += evaluate_doubled_pawns(board)
    score += evaluate_connected_pawns(board)
    score += evaluate_isolated_pawns(board)
    return score


def evaluate_bishop_pair(board):
    white_bishops = 0
    black_bishops = 0
    for row in range(8):
        for col in range(8):

            if board[row][col] == 3:
                white_bishops +=1
            elif board[row][col] == -3:
                black_bishops += 1

    score = 0.0
    if white_bishops >= 2:
        score += 0.25
    if black_bishops >= 2:
        score -= 0.25
    return score

def calculate_game_phase(board):

    phase_values = {
        2: 4,
        5: 2,
        3: 1,
        4: 1
    }

    phase = 0

    for row in range(8):
        for col in range(8):

            piece = abs(board[row][col])

            if piece in phase_values:
                phase += phase_values[piece]

    phase = min(phase, 24)

    return phase / 24

def get_king_position_score(board, row, col, piece, game_phase):

    if piece > 0:

        opening_score = KING_TABLE[row][col]
        endgame_score = KING_ENDGAME_TABLE[row][col]

    else:

        opening_score = KING_TABLE[7-row][col]
        endgame_score = KING_ENDGAME_TABLE[7-row][col]

    return (opening_score * game_phase + endgame_score * (1 - game_phase))

def evaluate_king_activity(board, game_phase):
    endgame_weight = 1.0 - game_phase
    if endgame_weight <= 0:
        return 0.0
    score = 0.0
    white_king = find_king(board, -6)
    black_king = find_king(board, -6)

    if white_king is not None:
        row, col = white_king
        distance = abs(row - 3.5) + abs(col - 3.5)
        white_activity = 3.5 - distance / 2
        score += white_activity * 0.1 * endgame_weight
    if black_king is not None:
        row, col = black_king
        distance = abs(row - 3.5) + abs(col - 3.5)
        black_activity = 3.5 - distance / 2
        score -= black_activity * 0.1 * endgame_weight
    return score