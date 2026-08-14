import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,640))
pygame.display.set_caption('Chess')

WBishop = pygame.transform.scale(pygame.image.load('images/WBishop.png'), (80,80))
BBishop = pygame.transform.scale(pygame.image.load('images/BBishop.png'), (80,80))
WKing = pygame.transform.scale(pygame.image.load('images/WKing.png'), (80,80))
BKing = pygame.transform.scale(pygame.image.load('images/BKing.png'), (80,80))
WQueen = pygame.transform.scale(pygame.image.load('images/WQueen.png'), (80,80))
BQueen = pygame.transform.scale(pygame.image.load('images/BQueen.png'), (80,80))
WKnight = pygame.transform.scale(pygame.image.load('images/WKnight.png'), (80,80))
BKnight = pygame.transform.scale(pygame.image.load('images/BKnight.png'), (80,80))
WPawn = pygame.transform.scale(pygame.image.load('images/WPawn.png'), (80,80))
BPawn = pygame.transform.scale(pygame.image.load('images/BPawn.png'), (80,80))
WRook = pygame.transform.scale(pygame.image.load('images/WRook.png') , (80,80))
BRook = pygame.transform.scale(pygame.image.load('images/BRook.png'), (80,80))

turn = 0

game_over = False

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

pieces = {
    -6: BKing,
    -5: BRook,
    -4: BKnight,
    -3: BBishop,
    -2: BQueen,
    -1: BPawn,

    1: WPawn,
    2: WQueen,
    3: WBishop,
    4: WKnight,
    5: WRook,
    6: WKing
}

def path_clear(old_row, old_col, new_row, new_col):

    row_change = new_row - old_row
    col_change = new_col - old_col

    if row_change != 0 and col_change != 0:
        if abs(row_change) != abs(col_change):
            return False

    # Determine direction
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

    # Start one square away from the original square
    current_row = old_row + row_step
    current_col = old_col + col_step

    # Check every square before the destination
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

            # Don't bother with empty squares
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

            # Enemy pawn must be beside it
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
    # Nothing selected
    if piece == 0:
        return False

    if can_en_passant(old_row, old_col, new_row, new_col):
        return True


    # Difference in rows and columns
    row_change = new_row - old_row
    col_change = new_col - old_col

    # Pawn
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

    # Knight
    if abs(piece) == 4:
        if (abs(row_change), abs(col_change)) in [(2, 1), (1, 2)]:
            return True
        return False

    # Bishop
    if abs(piece) == 3:
        if abs(row_change) == abs(col_change):
            return path_clear(old_row, old_col, new_row, new_col)
        return False

    # Rook
    if abs(piece) == 5:
        if row_change == 0 or col_change == 0:
            return path_clear(old_row, old_col, new_row, new_col)
        return False

    # Queen
    if abs(piece) == 2:
        if row_change == 0 or col_change == 0:
            return path_clear(old_row, old_col, new_row, new_col)

        if abs(row_change) == abs(col_change):
            return path_clear(old_row, old_col, new_row, new_col)

        return False

    # King
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



LIGHT = (240,217,181)
DARK = (181,136,99)
WHITE = (255,255,255)

selected_square = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            row = mouse_y // 80
            col = mouse_x // 80

            if selected_square is None:
                if pieceArray[row][col] != 0:
                    selected_square = (row,col)
            else:
                old_row, old_col = selected_square

                if is_valid_move(old_row, old_col, row, col):
                    if not move_leaves_king_in_check(old_row, old_col, row, col):
                        moving_piece = pieceArray[old_row][old_col]
                        is_en_passant = can_en_passant(old_row, old_col, row, col)
                        pieceArray[row][col] = pieceArray[old_row][old_col]
                        pieceArray[old_row][old_col] = 0

                        if is_en_passant:
                            pieceArray[old_row][col] = 0

                        if pieceArray[row][col] == 6 and old_row == 7 and old_col == 4 and row == 7 and col == 6:
                            pieceArray[7][5] = pieceArray[7][7]
                            pieceArray[7][7] = 0

                        elif pieceArray[row][col] == 6 and old_row == 7 and old_col == 4 and row == 7 and col == 2:
                            pieceArray[7][3] = pieceArray[7][0]
                            pieceArray[7][0] = 0

                        elif pieceArray[row][col] == -6 and old_row == 0 and old_col == 4 and row == 0 and col == 6:
                            pieceArray[0][5] = pieceArray[0][7]
                            pieceArray[0][7] = 0
                        elif pieceArray[row][col] == -6 and old_row == 0 and old_col == 4 and row == 0 and col == 2:
                            pieceArray[0][3] = pieceArray[0][0]
                            pieceArray[0][0] = 0

                        en_passant_target = None

                        if moving_piece == 1 and old_row == 6 and row == 4:
                            en_passant_target = (5, col)
                        elif moving_piece == -1 and old_row == 1 and row == 3:
                            en_passant_target = (2, col)
                        
                        turn += 1
                        if turn % 2 == 0:
                            player = 1
                        else:
                            player = -1

                        if is_checkmate(player):
                            print(f"Checkmate! {"Black" if player == 1 else "White"} wins!")
                            game_over = True
                        elif is_stalemate(player):
                            print("Draw! Stalemate")
                            game_over = True
                        elif is_in_check(6 if player == 1 else -6):
                            print(f"Check from {"Black" if player == 1 else "White"}!")

                for i in range(8):
                    if pieceArray[7][i] == -1:
                        pieceArray[7][i] = -2
                    elif pieceArray[0][i] == 1:
                        pieceArray[0][i] = 2
                selected_square = None
    
    screen.fill(WHITE)

    for rows in range(8):
        for cols in range(8):
            if (rows+cols) % 2 == 0:
                color = LIGHT 
            else: 
                color = DARK

            x = cols * 80
            y = rows * 80

            pygame.draw.rect(screen,color, (x,y,80,80))
            piece = pieceArray[rows][cols]
            if piece != 0:
                screen.blit(pieces[piece], (x,y))

    pygame.display.flip()
pygame.quit()