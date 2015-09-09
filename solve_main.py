#!/usr/bin/env python



"""

   Figure out how many queens can reside on an NxN board
   row,col = 0,0 is upper left
   row,col = max,max is lower right
   squares/board number (bn) starts upper left across top, then row by row

"""

import board
import queens



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def do_next_slot(b,row,col):

   row,col = b.next_slot_nextRow(row,col)
   while row is None and len(b.queen_list) >0:
      qb = b.queen_list[-1]
      b.roll_back(1)
      """ #
      print qb.row, qb.col
      #print qb2.row, qb2.col
      b.print_board()
      """ #
      row,col = b.next_slot(qb.row,qb.col,True)
   return row,col

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def do_solver(n):
   """
   """
   b = board.board(n)
   row = 0
   col = 0
   i = 0
   while len(b.queen_list) < (n): #target number of queens on board

      i +=1
      q = queens.queen(row,col,n)
      q.mak_mask()
      b.add_queen(q)
      """
      print "\niteration", i
      b.print_board()

      print "queens placed", len(b.queen_list)
      print ""
      """
      if len(b.queen_list) == n:
         print "\niteration", i
         b.print_board()

         print "queens placed", len(b.queen_list)
         print ""
         break

      row,col = do_next_slot(b,row,col)
      if row is None:
         print "\niteration", i
         b.print_board()

         print "queens placed", len(b.queen_list)
         print "\tout of squares\n"
         print ""
         break


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':

   n = 8

   print "start again"

   try:
      do_solver(n)
   except KeyboardInterrupt:
      pass

