class XOX:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    def add_element(self, chanse):
        while True:
            i = int(input("Enter row (0-2): "))
            j = int(input("Enter column (0-2): "))
            if 0 <= i <= 2 and 0 <= j <= 2 and self.board[i][j] == '-':
                break
            else:
                print("Invalid move. Try again.")
        self.board[i][j] = "X" if chanse % 2 == 1 else "O"

    def board_display(self):
        for row in self.board:
            print("  ".join(row))
        print()

    def win_check(self):
        b = self.board
        lines = [
            [b[0][0], b[0][1], b[0][2]],
            [b[1][0], b[1][1], b[1][2]],
            [b[2][0], b[2][1], b[2][2]],
            [b[0][0], b[1][0], b[2][0]],
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]],
            [b[0][2], b[1][1], b[2][0]]
        ]
        for line in lines:
            if line[0] != '-' and line[0] == line[1] == line[2]:
                return True
        return False

# --- Game starts here ---

game = XOX()
chanse = 1

while chanse <= 9:
    player = 1 if chanse % 2 == 1 else 2
    choice = int(input(f"Player {player}, enter 1 to continue or 0 to quit: "))
    
    if choice == 1:
        game.add_element(chanse)
        game.board_display()
        if game.win_check():
            print(f"Player {player} wins!!")
            break
        chanse += 1
    elif choice == 0:
        print("Exit success.")
        break
    else:
        print("Invalid input. Please enter 1 or 0.")

if chanse > 9:
    print("It's a draw!")
