


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
      self.bm = 0    # biard mask
      self.queen_list = []

   def print_board(self):

      #board = bin(self.bm)[2:].zfill(self.size*self.size)
      board = self.gen_board()

      board_list = list(board)

      for q in self.queen_list:
         qp = q.row*self.size + q.col
         board_list[qp] = 'q'
         

      for spot in xrange(self.size * self.size):
         if (spot % self.size) == 0:
            print ''
         print ' %c' % board_list[spot],
      print ''
      


   #~~~~~~~~~~~~~~~~~~~~~~~~

   def gen_board(self):
      """
      """
      board = bin(self.bm)[2:].zfill(self.size*self.size)
      return board

   #~~~~~~~~~~~~~~~~~~~~~~~~

   def add_queen(self,queen):
      """
      """
      self.bm |= queen.mask
      self.queen_list.append(queen)


   #~~~~~~~~~~~~~~~~~~~~~~~~

   def next_slot(self, row, col):
      """
      """
      #compute given location
      loc = row*self.size + col

      #scan board for next open space
      board = self.gen_board()

      try:
         nxt_loc = board.index('0',loc)
         r1 = int(nxt_loc / self.size)
         c1 = nxt_loc % self.size
         #print nxt_loc
         return r1,c1
      except ValueError:
         print 'oopsie'
         return None,None
      
      print 'outa here'
      return None,None       #shouldn't happen


   #~~~~~~~~~~~~~~~~~~~~~~~~

   def roll_back(self, n=1):
      """
         roll back (remove) one queen from list & 
         regen the board mask
      """
   
      for i in xrange(n):
         if len(self.queen_list) > 0:
            self.queen_list.pop()

      self.bm = 0
      for q in self.queen_list:
         self.bm |= q.mask









