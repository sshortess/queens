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

   q = queens.queen(3,0,n)
   q.mak_mask()
   b.add_queen(q)

   b.print_board()

   q2 = queens.queen(2,1,n)
   q2.mak_mask()
   b.add_queen(q2)

   b.print_board()
   b.roll_back()
   b.print_board()

   q3 = queens.queen(5,6,n)
   q3.mak_mask()
   b.add_queen(q3)

   row,col = b.next_slot(5,6)
   print row,col


   b.print_board()

   print ''
