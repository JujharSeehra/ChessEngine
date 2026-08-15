import allFunctions
from evaluation import evaluate_board

nodes_searched = 0

MATE_SCORE = 10000

def alpha_beta(depth, alpha, beta, player, ply):

    global nodes_searched

    nodes_searched += 1

    moves = allFunctions.generate_legal_moves(player)

    # No legal moves
    if len(moves) == 0:

        king = 6 if player == 1 else -6

        if allFunctions.is_in_check(king):

            # Checkmate
            if player == 1:
                return -MATE_SCORE + ply
            else:
                return MATE_SCORE - ply

        # Stalemate
        return 0

    # Search finished
    if depth == 0:

        return evaluate_board(
            allFunctions.pieceArray,
            allFunctions.is_valid_move,
            allFunctions.move_leaves_king_in_check,
            allFunctions.is_in_check,
            allFunctions.can_attack_square
        )

    moves = allFunctions.order_moves(moves)

    # White maximizes
    if player == 1:

        best_score = -float("inf")

        for move in moves:

            state = allFunctions.save_game_state()

            old_row, old_col, new_row, new_col = move

            allFunctions.make_engine_move(
                old_row,
                old_col,
                new_row,
                new_col
            )

            score = alpha_beta(
                depth - 1,
                alpha,
                beta,
                -1,
                ply + 1
            )

            allFunctions.restore_game_state(state)

            best_score = max(
                best_score,
                score
            )

            alpha = max(
                alpha,
                best_score
            )

            # Alpha-beta cutoff
            if beta <= alpha:
                break

        return best_score

    # Black minimizes
    else:

        best_score = float("inf")

        for move in moves:

            state = allFunctions.save_game_state()

            old_row, old_col, new_row, new_col = move

            allFunctions.make_engine_move(
                old_row,
                old_col,
                new_row,
                new_col
            )

            score = alpha_beta(
                depth - 1,
                alpha,
                beta,
                1,
                ply + 1
            )

            allFunctions.restore_game_state(state)

            best_score = min(
                best_score,
                score
            )

            beta = min(
                beta,
                best_score
            )

            # Alpha-beta cutoff
            if beta <= alpha:
                break

        return best_score

def find_best_move(depth=3):

    global nodes_searched

    nodes_searched = 0

    player = 1 if allFunctions.turn % 2 == 0 else -1

    moves = allFunctions.generate_legal_moves(player)

    if not moves:
        return None

    moves = allFunctions.order_moves(moves)

    best_move = None

    alpha = -float("inf")
    beta = float("inf")

    # White
    if player == 1:

        best_score = -float("inf")

        for move in moves:

            state = allFunctions.save_game_state()

            old_row, old_col, new_row, new_col = move

            allFunctions.make_engine_move(
                old_row,
                old_col,
                new_row,
                new_col
            )

            score = alpha_beta(
                depth - 1,
                alpha,
                beta,
                -1,
                1
            )

            allFunctions.restore_game_state(state)

            print(
                f"{move} -> {round(score, 2)}"
            )

            if score > best_score:

                best_score = score
                best_move = move

            alpha = max(
                alpha,
                best_score
            )

    # Black
    else:

        best_score = float("inf")

        for move in moves:

            state = allFunctions.save_game_state()

            old_row, old_col, new_row, new_col = move

            allFunctions.make_engine_move(
                old_row,
                old_col,
                new_row,
                new_col
            )

            score = alpha_beta(
                depth - 1,
                alpha,
                beta,
                1,
                1
            )

            allFunctions.restore_game_state(state)

            print(
                f"{move} -> {round(score, 2)}"
            )

            if score < best_score:

                best_score = score
                best_move = move

            beta = min(
                beta,
                best_score
            )

    print()
    print("Nodes searched:", nodes_searched)
    print("Best move:", best_move)
    print("Evaluation:", round(best_score, 2))

    return best_move