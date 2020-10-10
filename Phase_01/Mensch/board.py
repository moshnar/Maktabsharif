# board.py
# Author: Johnny Rocketfingers

# tracks information on players and their pieces,
# aswell as the board details (size, number of pieces, etc)

import players
import random

board = {}

def query_playernames():
    board["player_names"] = []

    no_of_players = input("Input the number of players: ")
    for i in range(0, no_of_players):
        board["player_names"].append(input("Player %s: " % i))

def create_board(no_of_fields=40, no_of_pieces=4):
    board["no_of_pieces"] = no_of_pieces
    board["no_of_fields"] = no_of_fields
    board["players"] = players.prepare_players(**board)

    board["active_player"] = board["players"].pop(0) # take the first player

    board["current_roll"] = None

def get_player():
    return board["active_player"]

def next_player():
    board["players"].append(board["active_player"])
    board["active_player"] = board["players"].pop(0)

def display_current_player():
    print(board["active_player"]["name"])

def roll():
    if board["current_roll"] is None:
        board["current_roll"] = random.randint(1, 6)

    return board["current_roll"]

def display_current_roll():
    print("%s has rolled %s" % (board["active_player"]["name"],
                                board["current_roll"]))

