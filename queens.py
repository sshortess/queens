

"""

   Figure out how many queens can reside on an NxN board
   row,col = 0,0 is upper left
   row,col = max,max is lower right
   squares/board number (bn) starts upper left across top, then row by row

"""

class queen(object):

   """
   """

   def __init__(self,row=0, col=0, size=8):
      self.col = col
      self.row = row
      self.bn = (row*size)+col    #board number
      self.mask = 0
      self.size = size  # value of N on a NxN board

   def set_row_col(self, row, col):
      self.row = row
      self.col = col

   def set_size(self,size):
      self.size = size

   def mak_mask(self):
      """
         make the map/mask of the squares this queen sees
           size is the 'order' of the square matrix 
      """

      #do row
      str_msk = '1'*self.size 
      str_msk = str_msk + ('0'*(self.size * (self.size-1)))
      self.mask = int(str_msk,2)
      # shift to proper location (?) 
      self.mask = self.mask >> (self.size * self.row)

      #do column
      str_msk = '0'
      for i in xrange(self.size):
         str_msk += '1'
         str_msk += '0'*(self.size-1) 
      str_msk = str_msk[1:]
      self.mask |= int(str_msk,2) >> self.col
      # shift to proper location (?) 


      # do diagnals

      qn = self.row * self.size + self.col
      mask = 0
      sm = '1' + '0'* 63
      bb = int(sm,2)
      #print 'location',self.row, self.col
      
      for row in xrange(self.size):
         if row == self.row:
            continue
         c_row = abs(self.row - row)
         c_col = self.col - c_row
         if c_col >=0:
            mask |= bb >> (row*8 + c_col)

         c_col = self.col + c_row
         if c_col < self.size:
            mask |= bb >> (row*8 + c_col)

      self.mask |= mask

         


