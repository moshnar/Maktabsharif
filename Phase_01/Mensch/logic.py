# logic.py
# Author: Johnny Rocketfingers

import players
import board

def move(player, steps):
    end_location = player["location"] + steps

    target = board.piece_at(end_location)
    if target is not None:
        players.piece_out(target)         # pun totally intended, not even sorry

def play_turn(players, player_index):
    steps = dice.roll()
    move(players[player_index], steps)

