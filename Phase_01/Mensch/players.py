# players.py
# Author: Johnny Rocketfingers

_invalid = -1

def prepare_players(player_names=["red", "green", "blue", "yellow"],
                    no_of_pieces=4,
                    **extra_args):
    if len(player_names) not in range(1, 5):
        raise Exception("Number of players must be in range 1-4!")

    players = []

    for player_name in player_names:
        player = {}

        player["name"] = player_name
        player["pieces_out"] = [{}] * 4
        player["pieces_in"] = []

        for piece in player["pieces_out"]:
            piece["location"] = _invalid    # invalid global location
            piece["progress"] = 0           # progress towards the end of the tour
            piece["player"] = player        # reverse reference
                                            # reduces argument passing

        players.append(player)

    return players

def piece_out(target):
    target["location"] = -1
    target["progress"] = 0

def piece_in(player):
    piece = player["pieces_out"].pop()
    player["pieces_in"]

