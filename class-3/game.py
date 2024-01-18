# 1. Dowolna technologia - python
# 2. Wygenerować planszę AxB (min 5x5). Wylosować START i STOP przy krawędzi planszy (różne pola i nie obok siebie). Losowo generujemy przeszkody, które musimy ominać.
# 3. Plansza powinna być do wgladu, np. wyeksportowana do pliku, wyświetlona w terminalu itp., razem ze startem np. A, stopem np. B i przeszkodami oznaczonymi np. jako X, to dowolna konwencja. W pliku można też dać generowana ścieżkę od A do B.
# 4. Zasada gry jest prosta, przechodzimy od poczatku do końca planszy, omijajac przeszkody i nie wychodzac za nia. Długość drogi nie ma znaczenia.
# 5. Nie chodzi o implementację całej gry, a poszczególne metody, by móc je przetestować. Np. implementujemy ruch w prawo, lewo, górę i dół i testujemy ruch, np. czy można się przemieścić w tych kierunkach, czy nie ma tam przeszkód, czy nie wychodzimy za planszę itp. NIE MA potrzeby implementowania niczego innego poza logika gry, np. trybu graficznego, czy tekstowego/konsolowego.
# 6. Ocenie będzie podlegać całościowe podejście, czyli w mniejszym stopniu implementacja logiki, a większym rozważenie tego, co może się wydarzyć (corner case'y, np. wyjście poza planszę).

import random

OBSTACLE_SYMBOL = "X"
START_SYMBOL = "S"
END_SYMBOL = "Q"
EMPTY_SYMBOL = " "
PLAYER_SYMBOL = "#"
BOARD_SIZE = 7

MOVE_UP = "w"
MOVE_DOWN = "s"
MOVE_LEFT = "a"
MOVE_RIGHT = "d"


def create_game():
    board = [
        [EMPTY_SYMBOL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)
    ]  # Generating empty board
    # Random start point
    initial_row = random.randint(0, 6)
    initial_col = random.choice([0, 6])
    board[initial_row][initial_col] = START_SYMBOL

    # Random end point
    final_row = random.choice([0, 6])
    final_col = random.randint(0, 6)
    while board[final_row][final_col] != EMPTY_SYMBOL:
        final_row = random.choice([0, 6])
        final_col = random.randint(0, 6)
    board[final_row][final_col] = END_SYMBOL

    obstacles_count = 0
    while obstacles_count < 7:
        obstacle_row = random.randint(0, 6)
        obstacle_col = random.randint(0, 6)
        if board[obstacle_row][obstacle_col] == EMPTY_SYMBOL:
            board[obstacle_row][obstacle_col] = OBSTACLE_SYMBOL
            obstacles_count += 1

    return board, initial_row, initial_col, final_row, final_col


def move_player(
    game_board, direction, current_row, current_col, initial_row, initial_col
):
    new_row, new_col = current_row, current_col

    if direction == MOVE_UP and current_row > 0:
        new_row -= 1
    elif direction == MOVE_DOWN and current_row < len(game_board) - 1:
        new_row += 1
    elif direction == MOVE_LEFT and current_col > 0:
        new_col -= 1
    elif direction == MOVE_RIGHT and current_col < len(game_board[0]) - 1:
        new_col += 1

    if game_board[new_row][new_col] != OBSTACLE_SYMBOL:
        if game_board[new_row][new_col] != END_SYMBOL:
            game_board[current_row][current_col] = EMPTY_SYMBOL
        else:
            game_board[current_row][current_col] = END_SYMBOL
        game_board[new_row][new_col] = PLAYER_SYMBOL

        return new_row, new_col, initial_row, initial_col
    else:
        return current_row, current_col, initial_row, initial_col


def display_board(game_board):
    for row in game_board:
        print(" ".join(row))


def main():
    (
        current_game_board,
        current_player_row,
        current_player_col,
        final_row,
        final_col,
    ) = create_game()

    initial_row, initial_col = current_player_row, current_player_col
    # main loop
    while True:
        print("Plansza:")
        display_board(current_game_board)
        print("Punkt startowy: S")
        print("Punkt końcowy: E")
        print("Przeszkody: X")
        move = input("Ruch: (W A S D): ").lower()

        if move in [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]:
            (
                current_player_row,
                current_player_col,
                initial_row,
                initial_col,
            ) = move_player(
                current_game_board,
                move,
                current_player_row,
                current_player_col,
                initial_row,
                initial_col,
            )
            if current_player_row == final_row and current_player_col == final_col:
                current_game_board[current_player_row][
                    current_player_col
                ] = PLAYER_SYMBOL
                print("Gratulacje! Udało Ci się dojść do wyjścia!")
                break


if __name__ == "__main__":
    main()
