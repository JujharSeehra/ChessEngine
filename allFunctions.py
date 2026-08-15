turn = 0

white_king_moved = False
black_king_moved = False

white_left_rook_moved = False
white_right_rook_moved = False

black_left_rook_moved = False
black_right_rook_moved = False

en_passant_target = None

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

def path_clear(old_row, old_col, new_row, new_col):

    row_change = new_row - old_row
    col_change = new_col - old_col

    if row_change != 0 and col_change != 0:
        if abs(row_change) != abs(col_change):
            return False

    if row_change > 0:
        row_step = 1
    elif row_change < 0:
        row_step = -1
    else:
        row_step = 0

    if col_change > 0:
        col_step = 1
    elif col_change < 0:
        col_step = -1
    else:
        col_step = 0

    current_row = old_row + row_step
    current_col = old_col + col_step

    while (current_row, current_col) != (new_row, new_col):

        if pieceArray[current_row][current_col] != 0:
            return False

        current_row += row_step
        current_col += col_step

    return True


def can_attack(old_row, old_col, new_row, new_col):
    piece = pieceArray[old_row][old_col]

    if piece == 0:
        return False

    row_change = new_row - old_row
    col_change = new_col - old_col

    if abs(piece) == 1:

        if piece > 0:
            if row_change == -1 and abs(col_change) == 1:
                return True
        else: 
            if row_change == 1 and abs(col_change) == 1:
                return True
        return False

    if abs(piece) == 4:
        if (abs(row_change), abs(col_change)) in [(2,1),(1,2)]:
            return True
        return False

    if abs(piece) == 3:
        if abs(row_change) == abs(col_change):
            return path_clear(old_row,old_col,new_row, new_col)
        return False

    if abs(piece) == 5:
        if row_change == 0 or col_change == 0:
            return path_clear(old_row,old_col,new_row,new_col)
        return False


    if abs(piece) == 2:
        if row_change == 0 or col_change == 0:
            return path_clear(
                old_row,
                old_col,
                new_row,
                new_col
            )

        if abs(row_change) == abs(col_change):
            return path_clear(
                old_row,
                old_col,
                new_row,
                new_col
            )

        return False

    if abs(piece) == 6:

        if abs(row_change) <= 1 and abs(col_change) <= 1:
            return True

        return False

    return False        

def find_piece(x):
    for i in range(8):
        for j in range(8):
            if pieceArray[i][j] == x:
                return i,j

def is_in_check(x):

    pieceRow, pieceCol = find_piece(x)

    for i in range(8):
        for j in range(8):

            piece = pieceArray[i][j]

            if piece == 0:
                continue

            if x == 6 and piece < 0:

                if can_attack(i, j, pieceRow, pieceCol):
                    return True

            elif x == -6 and piece > 0:

                if can_attack(i, j, pieceRow, pieceCol):
                    return True

    return False

def can_attack_square(row, col, enemy):
    for i in range(8):
        for j in range(8):
            piece = pieceArray[i][j]

            if piece == 0:
                continue

            if enemy == 1 and piece > 0:
                if can_attack(i,j,row,col):
                    return True

            elif enemy == -1 and piece < 0:
                if can_attack(i, j, row, col):
                    return True
    return False

def move_leaves_king_in_check(old_row, old_col, new_row, new_col):
    captured_piece = pieceArray[new_row][new_col]
    moving_piece = pieceArray[old_row][old_col]

    is_en_passant = can_en_passant(old_row, old_col, new_row, new_col)

    pieceArray[new_row][new_col] = moving_piece
    pieceArray[old_row][old_col] = 0

    en_passant_captured = 0
    if is_en_passant:
        en_passant_captured = pieceArray[old_row][new_col]
        pieceArray[old_row][new_col]= 0

    if moving_piece > 0:
        king = 6
    else:
        king = -6

    in_check = is_in_check(king)    

    pieceArray[old_row][old_col] = moving_piece
    pieceArray[new_row][new_col] = captured_piece

    if is_en_passant:
        pieceArray[old_row][new_col] = en_passant_captured

    return in_check

def can_en_passant(old_row, old_col, new_row, new_col):

    piece = pieceArray[old_row][old_col]

    if abs(piece) != 1:
        return False

    if en_passant_target != (new_row, new_col):
        return False

    if piece > 0:
        if old_row - new_row == 1 and abs(new_col - old_col) == 1:

            if pieceArray[old_row][new_col] == -1:
                return True

    else:
        if new_row - old_row == 1 and abs(new_col - old_col) == 1:

            if pieceArray[old_row][new_col] == 1:
                return True

    return False

def is_valid_move(old_row, old_col, new_row, new_col, check_turn = True):
    piece = pieceArray[old_row][old_col]

    if abs(pieceArray[new_row][new_col]) == 6:
        return False

    if pieceArray[old_row][old_col] > 0 and pieceArray[new_row][new_col] > 0:
        return False
    elif pieceArray[old_row][old_col] < 0 and pieceArray[new_row][new_col] < 0:
        return False

    if check_turn:
        if pieceArray[old_row][old_col] > 0 and turn % 2 == 1:
            return False
        elif pieceArray[old_row][old_col] < 0 and turn % 2 == 0:
            return False

    if old_row == new_row and old_col == new_col:
        return False
    if piece == 0:
        return False

    if can_en_passant(old_row, old_col, new_row, new_col):
        return True

    row_change = new_row - old_row
    col_change = new_col - old_col

    if abs(piece) == 1:
        if piece > 0:

            if col_change == 0 and row_change == -1:
                if pieceArray[new_row][new_col] == 0:
                    return True

            if old_row == 6 and col_change == 0 and row_change == -2:
                if pieceArray[old_row - 1][old_col] == 0 and pieceArray[new_row][new_col] == 0:
                    return True

        elif piece < 0:

            if col_change == 0 and row_change == 1:
                if pieceArray[new_row][new_col] == 0:
                    return True

            if old_row == 1 and col_change == 0 and row_change == 2:
                if pieceArray[old_row + 1][old_col] == 0 and pieceArray[new_row][new_col] == 0:
                    return True

        
        if pieceArray[new_row][new_col] > 0:
            if row_change == 1 and abs(col_change) == 1:
                return True
        elif pieceArray[new_row][new_col] < 0:
            if row_change == -1 and abs(col_change) == 1:
                return True
        
        return False

    if abs(piece) == 4:
        if (abs(row_change), abs(col_change)) in [(2, 1), (1, 2)]:
            return True
        return False

    if abs(piece) == 3:
        if abs(row_change) == abs(col_change):
            return path_clear(old_row, old_col, new_row, new_col)
        return False

    if abs(piece) == 5:
        if row_change == 0 or col_change == 0:
            return path_clear(old_row, old_col, new_row, new_col)
        return False

    if abs(piece) == 2:
        if row_change == 0 or col_change == 0:
            return path_clear(old_row, old_col, new_row, new_col)

        if abs(row_change) == abs(col_change):
            return path_clear(old_row, old_col, new_row, new_col)

        return False

    if abs(piece) == 6:
        if abs(row_change) <= 1 and abs(col_change) <= 1:
            return True

        if row_change == 0 and abs(col_change) == 2:
            if col_change > 0:
                return can_castle(old_row, old_col, new_row, new_col, "right")
        if row_change == 0 and abs(col_change) == 3:
            return can_castle(old_row, old_col, new_row, new_col, "left")

        return False

    return False

def has_legal_move(player):

    for old_row in range(8):
        for old_col in range(8):

            piece = pieceArray[old_row][old_col]

            if piece == 0:
                continue
            if player == 1 and piece < 0:
                continue
            if player == -1 and piece > 0:
                continue

            for new_row in range(8):
                for new_col in range(8):
                    if is_valid_move(old_row, old_col, new_row, new_col, check_turn = False):
                        if not move_leaves_king_in_check(old_row, old_col, new_row, new_col):
                            return True
    return False

def is_checkmate(player):
    if player == 1:
        king = 6
    else:
        king = -6

    if not is_in_check(king):
        return False
    if has_legal_move(player):
        return False
    
    return True

def check_game_status():
    if turn % 2 == 0:
        player = 1
        king = 6
    else:
        player = -1
        king = -6
    if is_checkmate(player):
        return "checkmate"
    elif is_in_check(player):
        return "check"
    if is_stalemate(player):
        return "stalemate"
    return "normal"


def is_stalemate(player):
    if player == 1:
        king = 6
    else: 
        king = -6
    if is_in_check(king):
        return False
    if has_legal_move(player):
        return False
    return True

def can_castle(old_row, old_col, new_row, new_col, direction):
    if pieceArray[old_row][old_col] == 6:
        if old_row != 7 or old_col != 4:
            return False

        if white_king_moved:
            return False

        if direction == "right":

            if white_right_rook_moved:
                return False

            if pieceArray[7][7] != 5:
                return False

            if pieceArray[7][5] != 0 or pieceArray[7][6] != 0:
                return False

            if is_in_check(6):
                return False

            if can_attack_square(7,5,-1):
                return False

            return new_row == 7 and new_col == 6

        if direction == "left":
            if white_left_rook_moved:
                return False

            if pieceArray[7][0] != 5:
                return False

            if ((pieceArray[7][1] or pieceArray[7][2] or pieceArray[7][3]) != 0):
                return False

            if is_in_check(6):
                return False

            if can_attack_square(7,3,-1):
                return False

            if can_attack_square(7,2,-1):
                return False

            return new_row == 7 and new_col == 2

    if pieceArray[old_row][old_col] == -6:
        if old_row != 0 or old_col != 4: 
            return False

        if black_king_moved:
            return False

        if direction == "right":
            if black_right_rook_moved:
                return False
            if pieceArray[0][7] != -5:
                return False
            if pieceArray[0][5] != 0 or pieceArray[0][6] != 0:
                return False
            if pieceArray[0][5] != 0 or pieceArray[0][6] != 0:
                return False
            if is_in_check(-6):
                return False
            if can_attack_square(0,5,1):
                return False
            if can_attack_square(0,6,1):
                return False
            return new_row == 0 and new_col == 6

        if direction == "left":
            if black_left_rook_moved:
                return False
            if pieceArray[0][0] != -5:
                return False
            if ((pieceArray[0][1] or pieceArray[0][2] or pieceArray[0][3]) != 0):
                return False
            if is_in_check(-6):
                return False
            if can_attack_square(0,3,1):
                return False
            if can_attack_square(0,2,1):
                return False

            return new_row == 0 and new_col == 2

    return False


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
    white_king = find_king(board, 6)
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

def save_game_state():

    return {"board": [row[:] for row in pieceArray],

        "turn": turn,

        "white_king_moved": white_king_moved,
        "black_king_moved": black_king_moved,

        "white_left_rook_moved": white_left_rook_moved,
        "white_right_rook_moved": white_right_rook_moved,

        "black_left_rook_moved": black_left_rook_moved,
        "black_right_rook_moved": black_right_rook_moved,

        "en_passant_target": en_passant_target}

def restore_game_state(state):

    global pieceArray
    global turn

    global white_king_moved
    global black_king_moved

    global white_left_rook_moved
    global white_right_rook_moved

    global black_left_rook_moved
    global black_right_rook_moved

    global en_passant_target

    pieceArray = [row[:] for row in state["board"]]

    turn = state["turn"]

    white_king_moved = state["white_king_moved"]
    black_king_moved = state["black_king_moved"]

    white_left_rook_moved = state["white_left_rook_moved"]
    white_right_rook_moved = state["white_right_rook_moved"]

    black_left_rook_moved = state["black_left_rook_moved"]
    black_right_rook_moved = state["black_right_rook_moved"]

    en_passant_target = state["en_passant_target"]

def make_engine_move(old_row, old_col, new_row, new_col):

    global turn
    global en_passant_target

    moving_piece = pieceArray[old_row][old_col]

    is_en_passant = can_en_passant(old_row, old_col, new_row, new_col)

    pieceArray[new_row][new_col] = moving_piece
    pieceArray[old_row][old_col] = 0

    if is_en_passant:
        pieceArray[old_row][new_col] = 0

    if moving_piece == 6:

        if old_row == 7 and old_col == 4:

            if new_row == 7 and new_col == 6:
                pieceArray[7][5] = pieceArray[7][7]
                pieceArray[7][7] = 0

            elif new_row == 7 and new_col == 2:
                pieceArray[7][3] = pieceArray[7][0]
                pieceArray[7][0] = 0

    elif moving_piece == -6:

        if old_row == 0 and old_col == 4:

            if new_row == 0 and new_col == 6:
                pieceArray[0][5] = pieceArray[0][7]
                pieceArray[0][7] = 0

            elif new_row == 0 and new_col == 2:
                pieceArray[0][3] = pieceArray[0][0]
                pieceArray[0][0] = 0

    en_passant_target = None

    if moving_piece == 1 and old_row == 6 and new_row == 4:
        en_passant_target = (5, old_col)

    elif moving_piece == -1 and old_row == 1 and new_row == 3:
        en_passant_target = (2, old_col)

    update_castling_rights( moving_piece, old_row, old_col, new_row, new_col)

    turn += 1

def update_castling_rights(moving_piece, old_row, old_col, new_row, new_col):

    global white_king_moved
    global black_king_moved

    global white_left_rook_moved
    global white_right_rook_moved

    global black_left_rook_moved
    global black_right_rook_moved

    if moving_piece == 6:
        white_king_moved = True

    elif moving_piece == -6:
        black_king_moved = True

    elif moving_piece == 5:

        if old_row == 7 and old_col == 0:
            white_left_rook_moved = True

        elif old_row == 7 and old_col == 7:
            white_right_rook_moved = True

    elif moving_piece == -5:

        if old_row == 0 and old_col == 0:
            black_left_rook_moved = True

        elif old_row == 0 and old_col == 7:
            black_right_rook_moved = True

    if new_row == 7 and new_col == 0:
        if pieceArray[new_row][new_col] == 5:
            white_left_rook_moved = True

    if new_row == 7 and new_col == 7:
        if pieceArray[new_row][new_col] == 5:
            white_right_rook_moved = True

    if new_row == 0 and new_col == 0:
        if pieceArray[new_row][new_col] == -5:
            black_left_rook_moved = True

    if new_row == 0 and new_col == 7:
        if pieceArray[new_row][new_col] == -5:
            black_right_rook_moved = True

def generate_legal_moves(player):

    legal_moves = []

    for old_row in range(8):
        for old_col in range(8):

            piece = pieceArray[old_row][old_col]

            if piece == 0:
                continue

            if player == 1 and piece < 0:
                continue

            if player == -1 and piece > 0:
                continue

            for new_row in range(8):
                for new_col in range(8):

                    if not is_valid_move(old_row, old_col, new_row, new_col, check_turn=False):
                        continue

                    if move_leaves_king_in_check(old_row, old_col, new_row, new_col):
                        continue

                    legal_moves.append((old_row, old_col, new_row, new_col))

    return legal_moves


def get_move_score(move):

    old_row, old_col, new_row, new_col = move

    moving_piece = pieceArray[old_row][old_col]
    captured_piece = pieceArray[new_row][new_col]

    score = 0

    if captured_piece != 0:

        victim_value = abs(pieceValues[captured_piece])
        attacker_value = abs(pieceValues[moving_piece])
        score += victim_value * 10
        score -= attacker_value

    if abs(moving_piece) == 1:

        if new_row == 0 or new_row == 7:
            score += 90

    return score


def order_moves(moves):

    scored_moves = []

    for move in moves:

        score = get_move_score(move)

        scored_moves.append((score, move))

    scored_moves.sort(key=lambda x: x[0], reverse=True)

    return [move for score, move in scored_moves]