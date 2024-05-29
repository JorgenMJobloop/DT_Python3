import random

def main():
    board = [" " for i in range(9)] # list comprehension

    def print_board(board):
        for row in [board[i * 3:(i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def check_winner(board, player):
        win_condition = [
            [board[0], board[1], [board[2]]],
            [board[3], board[4], [board[5]]],
            [board[6], board[7], [board[8]]],
            [board[0], board[3], [board[6]]],
            [board[1], board[4], [board[7]]],
            [board[2], board[5], [board[8]]],
            [board[0], board[4], [board[8]]],
            [board[2], board[4], [board[6]]]
            
            ]
        return [player, player, player] in win_condition

    def check_for_draw(board):
        return ' ' not in board
    
    def player_move(board):
        while True:
            move = int(input("Pick a position (1,9): ")) - 1
            if move < 0 or move >= 9 or board[move] != " ":
                print("Illegal move! Pick again!")
            else:
                board[move] = "X"
                break
                
    
    def ai(board):
        # the AI will try to beat the player
        # makes a new move
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                if check_winner(board, "O"):
                    return
                else:
                    board[i] = " "
        # attempts to block the players moves
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                if check_winner(board, "X"):
                    board[i] = "O"
                    return
                else:
                    board[i] = " "
        # make a random choice
        move = random.choice([i for i in range(9) if board[i] == " "])
        board[move] = "O"

    def game_loop():
        print_board(board)
        while True:
            player_move(board)
            print_board(board)
            if check_winner(board, "X"):
                print("You won!")
                break
            if check_for_draw(board):
                print("You tied with the AI!")
                break
            ai(board)
            print_board(board)
            if check_winner(board, "O"):
                print("The AI won!")
                break
            if check_for_draw(board):
                print("It was a draw!")
                break
    game_loop()

if __name__ == "__main__":
    main()            
    