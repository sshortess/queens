

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
      print len(str_msk), str_msk
      print hex(self.mask)

      #do column
      str_msk = '0'
      for i in xrange(self.size):
         str_msk += '1'
         str_msk += '0'*(self.size-1) 
      str_msk = str_msk[1:]
      self.mask |= int(str_msk,2) >> self.col
      # shift to proper location (?) 
      self.mask = self.mask
      #print len(str_msk), str_msk
      #print hex(self.mask)

      #do upper left leg

      #do upper right leg

      #do lower left

      #do lower right
      row = self.row
      col = self.col
      str_msk = '0'*(row*8 +col) #initialize the mask
      str_msk += '1'
      while row < (self.size -1) and col < (self.size -1):
         str_msk += '0'*(self.size)
         str_msk += '1'
         row += 1
         col += 1

      if len(str_msk) < (self.size*self.size):
         l = self.size * self.size
         pad = l - len(str_msk)
         str_msk += '0' * pad

      self.mask |= int(str_msk,2)
      print len(str_msk), str_msk
      print hex(self.mask)


