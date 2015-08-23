


"""

   Figure out how many queens can reside on an NxN board
   row,col = 0,0 is upper left
   row,col = max,max is lower right
   squares/board number (bn) starts upper left across top, then row by row

"""


class board(object):

   """
      functions for the board
   """

   def __init__(self, size=8):
      self.size = size
      self.board = '0' *(size*size)
      self.bm = int(self.board,2)

   def print_board(self):

      self.board = bin(self.bm)[2:].zfill(self.size*self.size)

      for col in xrange(self.size):
         for row in xrange(self.size):
            print ' %c' % self.board[(row + (col *8))],
         print ''

   #~~~~~~~~~~~~~~~~~~~~~~~~

   def add_queen(self,queen):
      """
      """
      self.bm |= queen.mask
