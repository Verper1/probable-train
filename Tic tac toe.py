#  ТЗ: Написать игру "Крестики-нолики"

def initialize_board() -> list[str]:
    """Returns an initialized Tic Tac Toe board."""
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def print_board(board: list[str]) -> None:
    """Prints the Tic Tac Toe board."""
    print("---------")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("---------")


def check_win(board: list[str], player: str) -> bool:
    """Checks if the given player has won."""
    win_conditions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 4, 8),
        (6, 4, 2),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8)
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def check_draw(board: list[str]) -> bool:
    """Checks if the game is a draw."""
    return all(cell in ['X', 'O'] for cell in board)


def get_player_move(board: list[str], player: str) -> int:
    """Gets the player's move and validates it."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move < 0 or move >= 9:
                print("Invalid move, try again.")
            elif board[move] in ['X', 'O']:
                print("Cell already occupied, try again.")
            else:
                return move
        except ValueError:
            print("Invalid input, try again.")


def player_to_player(board: list[str]):
    """Runs a game of Tic Tac Toe between two players."""
    players = ['X', 'O']
    current_player = 0
    game_over = False

    while not game_over:
        print_board(board)
        move = get_player_move(board, players[current_player])
        board[move] = players[current_player]

        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            game_over = True
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            game_over = True

        current_player = (current_player + 1) % 2


def main():
    """Runs the main game loop."""
    board = initialize_board()
    player_to_player(board)


if __name__ == "__main__":
    main()
