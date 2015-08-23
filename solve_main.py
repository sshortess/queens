#!/usr/bin/env python



"""

   Figure out how many queens can reside on an NxN board
   row,col = 0,0 is upper left
   row,col = max,max is lower right
   squares/board number (bn) starts upper left across top, then row by row

"""

import board
import queens







if __name__ == '__main__':

   n = 8
   
   b = board.board(n)
   q = queens.queen(1,1,n)

   b.print_board()

   q.mak_mask()
   b.add_queen(q)

   print hex(b.bm)

   b.print_board()
