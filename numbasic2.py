# indexing and slicing
import numpy as np
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2) # isse 3d array ... first 2 is number of blocks , second 2 is rows , and thrid 2 is columns

# INDEXING
# a3
# array([[[0, 1],
#         [2, 3]],

#        [[4, 5],
#         [6, 7]]])

# a1
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# a2
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

a2[1,0] # second row ka first element -> 4
a3[1,1,0] # second block ka second row ka first elemenet -> 6

# SLICING
# Slicing ka basic formula hota hai: [start : stop : step]
# a1
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a1[2:5:2] # array([2,4])

# a2
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

a2[0:2,1::2] # array([[1, 3],
#                    [5, 7]])    rows 0 and 1 and column 1 and 3

a2[::2,1::2] # array([[ 1,  3],
#                    [ 9, 11]])   rows 0 and 2 and column 1 and 3

a2[1,::3] # array([4,7])

a2[0,:] #  array([ 0,  1,  2,  3])

a2[:,2] # array([2,6,10])

a2[1:,1:3] # array([[ 5,  6],
#.                  [ 9, 10]])

a3 = np.arange(27).reshape(3,3,3)
# array([[[ 0,  1,  2],
#         [ 3,  4,  5],
#         [ 6,  7,  8]],

#        [[ 9, 10, 11],
#         [12, 13, 14],
#         [15, 16, 17]],

#        [[18, 19, 20],
#         [21, 22, 23],
#         [24, 25, 26]]])

a3[::2,0,::2] # array([[ 0,  2],
#                     [18, 20]])

a3[2,1:,1:] # array([[22, 23],
#                    [25, 26]])

a3[0,1,:] # array([3, 4, 5])

# Iterating

# 1d array iterating
for i in a1:
  print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# 2d array iterating
for i in a2:
  print(i)
# [0 1 2 3]
# [4 5 6 7]
# [ 8  9 10 11]

# 3d array iterating

for i in a3:
  print(i)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# [[ 9 10 11]
#  [12 13 14]
#  [15 16 17]]
# [[18 19 20]
#  [21 22 23]
#  [24 25 26]]

for i in np.nditer(a3): # jab sare element ko ek go me dekhna ho
  print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26

# RESHAPING

a = np.arange(12)
print(a)
b  = a.reshape(3,4) # reshape returns new array
# a.reshape(2,6)    # valid
# a.reshape(4,3)    # valid
# a.reshape(1,12)   # valid
# a.reshape(12,1)   # valid
# a.reshape(3,-1) -1 se khud dimension find krega fit krne ke liye wo elements
# and sirf ek -1 ho sakta h dono nhi ya to row ya to column
print(b)
a2 = np.arange(12).reshape(3,4)
print(a2)
a3 = np.transpose(a2) # rows changes to column
a3 = a2.T # method 2

print(a3)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]
a4 = a3.ravel() # yeh 1d array me convert krta h
print(a4)

# STACKING ( arrays ko jodna )

a4 = np.arange(12).reshape(3,4)
a5 = np.arange(12,24).reshape(3,4)

np.hstack((a4,a5)) # arrays ko add kr dega row wise columns as it is
# a4                    a5

# 0  1  2  3           12 13 14 15
# 4  5  6  7           16 17 18 19
# 8  9 10 11           20 21 22 23

# array([[ 0,  1,  2,  3, 12, 13, 14, 15],
      #  [ 4,  5,  6,  7, 16, 17, 18, 19],
      #  [ 8,  9, 10, 11, 20, 21, 22, 23]])

np.vstack((a4,a5)) # vice versa
# array([[ 0,  1,  2,  3],
      #  [ 4,  5,  6,  7],
      #  [ 8,  9, 10, 11],
      #  [12, 13, 14, 15],
      #  [16, 17, 18, 19],
      #  [20, 21, 22, 23]])

# SPLITTING (DIVIDE KRNA)

np.hsplit(a4,2) # a4 ko 2 horizonatal parts me todna
# 0  1  2  3
# 4  5  6  7
# 8  9 10 11

# Part 1       Part 2

# 0  1         2  3
# 4  5         6  7
# 8  9        10 11

np.vsplit(a5,3) # a5 ko vertically 3 parts me todna 

# 12 13 14 15
# 16 17 18 19
# 20 21 22 23

# Part 1:

# 12 13 14 15

# Part 2:

# 16 17 18 19

# Part 3:

# 20 21 22 23
