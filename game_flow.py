import sys


def read_participents(participents):
    try:
        f = open(participents, "r")
    except OSError:
        print(f"error opening the file {participents}")
        exit(-1)
    else:
        names = f.read().strip()
        # covert str to list
        names = list(names.split("\n"))
        return names


def choose_players(players_file):
    print(f"The players are: ")
    print(*players_file)
    #הוספנו * כדי שיודפס ללא חלוקה לתאים של הרשימה
    players_file = [f.lower() for f in players_file]
    #קיצרנו את ההתניה לשורה אחת
    while True:
        player1 = input("\nPlease select the first player: ").strip().lower()
        #strip() =השתמשנו בו כדי לנטרל רווחים מיותרים ולמנוע שגיאות
        if player1 in players_file:
            break
        print(f"{player1} is not a player in our participents, try again!")
    while True:
        player2 = input("Please select the second player: ").strip().lower()
        if player2 not in players_file:
            print(f"{player2} is not a player in our participents, please try again!")
        elif player1 == player2:
            print(f"{player2} please choose a different player")
        else:
            break
    return player1, player2


def display_board(board):
    print('   |   |')
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2])
    print('   |   |')


def one_move(player, icon, board):
    print(f"\n---{player}'s turn---")
    while True:
        try:
            row = int(input("please choose row from 0 to 2: "))
            col = int(input("please choose column from 0 to 2: "))
        except ValueError:
            print("Oops! That was not a valid number. Try again...")
            continue
        try:
            if board[row][col] != ' ':
                print(f"Position {row},{col} is already taken. Please try again")
                continue
            board[row][col] = icon
            #ה-icon איקס או עיגול בתוך הלוח לפי טור ושורה
        except IndexError:
            print("this position is outside our game board, please try again")
        else:
            display_board(board)
            break


def isTie(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
            #במידה ואין תיקו מוחזר F כדי שלולאת המשחק תמשיך
    return True


def isWin(board):
    row1 = [board[0][0], board[0][1], board[0][2]]
    row2 = [board[1][0], board[1][1], board[1][2]]
    row3 = [board[2][0], board[2][1], board[2][2]]
    col1 = [board[0][0], board[1][0], board[2][0]]
    col2 = [board[0][1], board[1][1], board[2][1]]
    col3 = [board[0][2], board[1][2], board[2][2]]
    cross1 = [board[0][0], board[1][1], board[2][2]]
    cross2 = [board[0][2], board[1][1], board[2][0]]
    options_to_win = [row1, row2, row3, col1, col2, col3, cross1, cross2]
    for option in options_to_win:
        if all(ele == option[0] and ele != ' ' for ele in option):
            return True
    return False


def stop_play():
    while True:
        option = input("please enter 'yes' if you want to play again. Otherwise enter 'exit': ")
        option = option.lower().strip()
        if option == 'exit':
            return True
        elif option == 'yes':
            return False
        else:
            print("wrong answer, try again")


def game(players):
    icons = ['X', 'O']
    scores = [0, 0]
    while True:
        # כך בנינו את הלוח:
        # 00 01 02
        # 10 11 12
        # 20 21 22
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        display_board(board)
        i = 1
        print("Let the game begin!")
        while not isTie(board) and not isWin(board):
            i = (i + 1) % 2
            one_move(players[i], icons[i], board)
            #מהלך אחד של השחקן הרלוונטי עם האייקון שהוקצה לו בלוח המשחק
        if isTie(board):
            print("It's a tie!")
            scores[0] += 1
            scores[1] += 1
        else:
            print(f"{players[i]} wins!")
            scores[i] += 3
        if stop_play():
            break
    print(f"{players[0]}'s score: {scores[0]} points")
    print(f"{players[1]}'s score: {scores[1]} points")
    print("Thank you for playing and goodbye :)")
