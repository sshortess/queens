#!/usr/bin/env python



"""

   Figure out how many queens can reside on an NxN board
   row,col = 0,0 is upper left
   row,col = max,max is lower right
   squares/board number (bn) starts upper left across top, then row by row

"""

import board
import queens


def test_dev():
   """
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
   # print row,col


   b.print_board()

   print ''
   """

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def do_next_slot(b,row,col):

   row,col = b.next_slot_nextRow(row,col)
   #if row is None:
   while row is None:
      qb = b.queen_list[-1]
      #qb2 = b.queen_list[-2]
      b.roll_back(1)
      #b.roll_back(2)
      """ #
      print qb.row, qb.col
      #print qb2.row, qb2.col
      b.print_board()
      """ #
      row,col = b.next_slot(qb.row,qb.col,True)
      #row,col = b.next_slot(qb2.row,qb2.col,True)
   return row,col

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':

   n = 8
   

   print "start again"

   b = board.board(n)
   row = 0
   col = 0
   i = 0
   while len(b.queen_list) < (n): #target number of queens on board
   #for i in xrange(n+500):

      try:
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

      except KeyboardInterrupt:
         break

