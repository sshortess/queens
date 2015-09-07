


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
      self.bm = 0    # board mask
      self.rollback_count = 0
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

   def next_slot(self, row, col, row_limited = False):
      """
         option to limit to current row only
      """
      #compute given location
      loc = row*self.size + col   # row/col point to this spot
      if row_limited:
         loc +=1  # start with next square
         loc_end = row*self.size + 7
      else:
         loc_end = self.size * self.size

      board = self.gen_board()

      #scan board for next open space
      try:
         nxt_loc = board.index('0',loc,loc_end)
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

   def next_slot_nextRow(self,row,col):
      """
      """
      #compute start next row
      loc = (row+1)*self.size

      # gen current board string for search
      board = self.gen_board()
      try:
         nxt_loc = board.index('0',loc,loc+7)
         r1 = int(nxt_loc / self.size)
         c1 = nxt_loc % self.size
         return r1,c1
      except ValueError:
         print 'Oopsie - next row'
         return None,None

      print 'Outta here - next row'
      return None,None

   #~~~~~~~~~~~~~~~~~~~~~~~~

   def roll_back(self, n=1):
      """
         roll back (remove) one queen from list & 
         regen the board mask
      """
   
      self.rollback_count += 1

      for i in xrange(n):
         if len(self.queen_list) > 0:
            self.queen_list.pop()

      self.bm = 0
      for q in self.queen_list:
         self.bm |= q.mask









