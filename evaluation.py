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

def evaluate_board(board, is_valid_move, move_leaves_king_in_check, is_in_check, can_attack_square
):

    score = 0.0

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

    score += evaluate_mobility( board, is_valid_move, move_leaves_king_in_check)

    score += evaluate_king_safety(board, is_in_check, can_attack_square)

    return round(score, 2)

def get_piece_table(piece):
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

def evaluate_mobility(board, is_valid_move, move_leaves_king_in_check):

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

                    if is_valid_move(
                        old_row,
                        old_col,
                        new_row,
                        new_col,
                        check_turn=False
                    ):

                        if not move_leaves_king_in_check(
                            old_row,
                            old_col,
                            new_row,
                            new_col
                        ):

                            if player == 1:
                                white_moves += 1
                            else:
                                black_moves += 1

    mobility_difference = white_moves - black_moves

    return mobility_difference * 0.02


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

def evaluate_king_safety(board, is_in_check, can_attack_square):
    score = 0.0

    if is_in_check(6):
        score -= 0.8
    white_attacked = king_attack_count(board, 6, can_attack_square)
    score -= white_attacked * 0.15

    if is_in_check(-6):
        score += 0.8
    black_attacked = king_attack_count(board, -6, can_attack_square)

    score += black_attacked * 0.15

    return score