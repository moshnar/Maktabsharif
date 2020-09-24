import  numpy as np
import pandas as pd
class Piece:
    def __init__(self,name,position,color):
        self.x = position[0]
        self.y = position[1]
        self.name = name
        self.color = color
        self.total = 16
        self.board = pd.DataFrame(np.zeros((8, 8)), [0, 1, 2, 3, 4, 5, 6, 7, ], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

    def Move(self,newposition):

            self.x = newposition[0]
            self.y = newposition[1]



class Pawn(Piece):
    def __init__(self):
        super().__init__()
        self.n = 8

    # def is_valid(self,x,y):
    #
    #     if self.x in board[:1,] or self.x in board[6:,] :
    #         elif x==self.x + 2 and y==self.y + 2:
    #             return True
    #             else :
    #             return False





    def Move(self):
        super().Move()


class Bishop(Piece):
    def __init__(self):
        super().__init__()
        self.n = 2

    def Move(self,newposition):
        super().Move()


class Knight (Piece):
    def __init__(self):
        super().__init__()
        self.n = 2
    def Move(self):
        super().Move()

class Rook(Piece):
    def __init__(self):
        super().__init__()
        self.n = 2
    def Move(self):
        super().Move()

class Queen(Piece):
    def __init__(self):
        super().__init__()
    def Move(self):
        super().Move()

class King(Piece):
    def __init__(self):
        super().__init__()
    def Move(self):
        super().Move()
    def is_check(self):
        pass
    def is_mate(self):
        pass

