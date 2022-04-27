import game_flow

print("Welcome to Yuval and Shachar's tic tac toe game!!")

players = game_flow.read_participents('participents.txt')
player1, player2 = game_flow.choose_players(players)
game_flow.game([player1, player2])
