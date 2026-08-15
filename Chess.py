import pygame
from sys import exit
from evaluation import evaluate_board
import allFunctions
import math
import engine


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

game_over = False


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



LIGHT = (240,217,181)
DARK = (181,136,99)
WHITE = (255,255,255)

selected_square = None

def computer_move():

    print("COMPUTER TURN START")

    move = engine.find_best_move(depth=3)

    if move is None:
        return

    old_row, old_col, new_row, new_col = move

    print(
        f"Computer moves "
        f"({old_row}, {old_col}) "
        f"-> "
        f"({new_row}, {new_col})"
    )

    allFunctions.make_engine_move(
        old_row,
        old_col,
        new_row,
        new_col
    )

    # Promotion
    for col in range(8):

        if allFunctions.pieceArray[7][col] == -1:
            allFunctions.pieceArray[7][col] = -2

        elif allFunctions.pieceArray[0][col] == 1:
            allFunctions.pieceArray[0][col] = 2

    print(f"Evaluation: {evaluate_board(allFunctions.pieceArray, allFunctions.is_valid_move, allFunctions.move_leaves_king_in_check, allFunctions.is_in_check, allFunctions.can_attack_square)}")

    status = allFunctions.check_game_status()
    if status == "checkmate":
        if allFunctions.turn % 2 == 1:
            winner = "White"
        else:
            winner = "Black"
        print(f"Checkmate! {winner} wins!")
    elif status == "stalemate":
        print("Stalemate!")
    elif status == 'check':
        print("Check!")

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
                if allFunctions.pieceArray[row][col] != 0:
                    selected_square = (row,col)
            else:
                old_row, old_col = selected_square

                if allFunctions.is_valid_move(old_row, old_col, row, col):
                    if not allFunctions.move_leaves_king_in_check(old_row, old_col, row, col):
                        moving_piece = allFunctions.pieceArray[old_row][old_col]
                        is_en_passant = allFunctions.can_en_passant(old_row, old_col, row, col)
                        allFunctions.pieceArray[row][col] = allFunctions.pieceArray[old_row][old_col]
                        allFunctions.pieceArray[old_row][old_col] = 0

                        if is_en_passant:
                            allFunctions.pieceArray[old_row][col] = 0

                        if allFunctions.pieceArray[row][col] == 6 and old_row == 7 and old_col == 4 and row == 7 and col == 6:
                            allFunctions.pieceArray[7][5] = allFunctions.pieceArray[7][7]
                            allFunctions.pieceArray[7][7] = 0

                        elif allFunctions.pieceArray[row][col] == 6 and old_row == 7 and old_col == 4 and row == 7 and col == 2:
                            allFunctions.pieceArray[7][3] = allFunctions.pieceArray[7][0]
                            allFunctions.pieceArray[7][0] = 0

                        elif allFunctions.pieceArray[row][col] == -6 and old_row == 0 and old_col == 4 and row == 0 and col == 6:
                            allFunctions.pieceArray[0][5] = allFunctions.pieceArray[0][7]
                            allFunctions.pieceArray[0][7] = 0
                        elif allFunctions.pieceArray[row][col] == -6 and old_row == 0 and old_col == 4 and row == 0 and col == 2:
                            allFunctions.pieceArray[0][3] = allFunctions.pieceArray[0][0]
                            allFunctions.pieceArray[0][0] = 0

                        en_passant_target = None

                        if moving_piece == 1 and old_row == 6 and row == 4:
                            en_passant_target = (5, col)
                        elif moving_piece == -1 and old_row == 1 and row == 3:
                            en_passant_target = (2, col)
                        
                        allFunctions.turn += 1
                        if allFunctions.turn % 2 == 0:
                            player = 1
                        else:
                            player = -1

                        evaluation = evaluate_board(allFunctions.pieceArray, allFunctions.is_valid_move, allFunctions.move_leaves_king_in_check, allFunctions.is_in_check, allFunctions.can_attack_square)

                        print(f"Evaluation: {evaluation}")

                        if allFunctions.is_checkmate(player):
                            print(f"Checkmate! {"Black" if player == 1 else "White"} wins!")
                            game_over = True
                        elif allFunctions.is_stalemate(player):
                            print("Draw! Stalemate")
                            game_over = True
                        elif allFunctions.is_in_check(6 if player == 1 else -6):
                            print(f"Check from {"Black" if player == 1 else "White"}!")

                        if allFunctions.turn % 2 == 1 and not game_over:
                            computer_move()

                        
                for i in range(8):
                    if allFunctions.pieceArray[7][i] == -1:
                        allFunctions.pieceArray[7][i] = -2
                    elif allFunctions.pieceArray[0][i] == 1:
                        allFunctions.pieceArray[0][i] = 2
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
            piece = allFunctions.pieceArray[rows][cols]
            if piece != 0:
                screen.blit(pieces[piece], (x,y))

    pygame.display.flip()
pygame.quit()