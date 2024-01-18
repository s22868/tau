import unittest

from game import (
    create_game,
    move_player,
    OBSTACLE_SYMBOL,
    START_SYMBOL,
    END_SYMBOL,
    EMPTY_SYMBOL,
    PLAYER_SYMBOL,
    BOARD_SIZE,
    MOVE_UP,
    MOVE_DOWN,
    MOVE_RIGHT,
)


class TestGameLogic(unittest.TestCase):
    def test_create_game(self):
        board, start_row, start_col, end_row, end_col = create_game()

        # Check board size
        self.assertEqual(len(board), BOARD_SIZE)
        self.assertEqual(len(board[0]), BOARD_SIZE)

        # Check start and end positions
        self.assertEqual(board[start_row][start_col], START_SYMBOL)
        self.assertEqual(board[end_row][end_col], END_SYMBOL)

        # Check obstacle count
        obstacle_count = sum(row.count(OBSTACLE_SYMBOL) for row in board)
        self.assertEqual(obstacle_count, 7)

    def test_move_player_valid(self):
        game_board = [
            [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
            [EMPTY_SYMBOL, START_SYMBOL, EMPTY_SYMBOL],
            [EMPTY_SYMBOL, END_SYMBOL, EMPTY_SYMBOL],
        ]
        current_row, current_col = 1, 1
        initial_row, initial_col = 1, 1

        new_row, new_col, _, _ = move_player(
            game_board, MOVE_RIGHT, current_row, current_col, initial_row, initial_col
        )

        self.assertEqual(new_row, 1)
        self.assertEqual(new_col, 2)
        self.assertEqual(game_board[current_row][current_col], EMPTY_SYMBOL)
        self.assertEqual(game_board[new_row][new_col], PLAYER_SYMBOL)

    def test_move_player_invalid_obstacle(self):
        game_board = [
            [EMPTY_SYMBOL, OBSTACLE_SYMBOL, EMPTY_SYMBOL],
            [EMPTY_SYMBOL, START_SYMBOL, EMPTY_SYMBOL],
            [EMPTY_SYMBOL, END_SYMBOL, EMPTY_SYMBOL],
        ]
        current_row, current_col = 1, 1
        initial_row, initial_col = 1, 1

        new_row, new_col, _, _ = move_player(
            game_board, MOVE_UP, current_row, current_col, initial_row, initial_col
        )

        self.assertEqual(new_row, current_row)
        self.assertEqual(new_col, current_col)
        self.assertEqual(game_board[current_row][current_col], START_SYMBOL)
        self.assertEqual(game_board[new_row][new_col], START_SYMBOL)

    def test_move_player_invalid_out_of_bounds(self):
        game_board = [
            [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
            [EMPTY_SYMBOL, START_SYMBOL, EMPTY_SYMBOL],
            [EMPTY_SYMBOL, END_SYMBOL, EMPTY_SYMBOL],
        ]
        current_row, current_col = 2, 1
        initial_row, initial_col = 1, 1

        new_row, new_col, _, _ = move_player(
            game_board, MOVE_DOWN, current_row, current_col, initial_row, initial_col
        )

        self.assertEqual(new_row, current_row)
        self.assertEqual(new_col, current_col)
        self.assertEqual(game_board[current_row][current_col], PLAYER_SYMBOL)
        self.assertEqual(game_board[new_row][new_col], PLAYER_SYMBOL)

    def test_move_player_invalid_direction(self):
        game_board = [
            [EMPTY_SYMBOL, EMPTY_SYMBOL, EMPTY_SYMBOL],
            [EMPTY_SYMBOL, START_SYMBOL, EMPTY_SYMBOL],
            [EMPTY_SYMBOL, END_SYMBOL, EMPTY_SYMBOL],
        ]
        current_row, current_col = 1, 1
        initial_row, initial_col = 1, 1

        new_row, new_col, _, _ = move_player(
            game_board,
            "invalid_direction",
            current_row,
            current_col,
            initial_row,
            initial_col,
        )

        self.assertEqual(new_row, current_row)
        self.assertEqual(new_col, current_col)
        self.assertEqual(game_board[current_row][current_col], PLAYER_SYMBOL)
        self.assertEqual(game_board[new_row][new_col], PLAYER_SYMBOL)


if __name__ == "__main__":
    unittest.main()
