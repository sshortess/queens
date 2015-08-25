


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
      #self.board = '0' *(size*size)
      #self.bm = int(self.board,2)
      self.bm = 0
      self.queen_list = []

   def print_board(self):

      board = bin(self.bm)[2:].zfill(self.size*self.size)

      board_list = list(board)

      for q in self.queen_list:
         qp = q[0]*8 + q[1]
         board_list[qp] = 'q'
         

      for spot in xrange(self.size * self.size):
         if (spot % self.size) == 0:
            print ''
         print ' %c' % board_list[spot],
      print ''
      

   #~~~~~~~~~~~~~~~~~~~~~~~~

   def add_queen(self,queen):
      """
      """
      self.bm |= queen.mask
      self.queen_list.append([queen.row,queen.col])


