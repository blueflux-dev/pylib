import numpy as np

# numpy array vs Python list
# list speed
a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c = []
import time

start = time.time()
for i in range(len(a)):
  c.append(a[i] + b[i])
print(time.time()-start) # kirna time laga
# approx 2 sec laga

# numpy speeed
import numpy as np
a = np.arange(10000000)
b = np.arange(10000000,20000000)

start = time.time()
c = a + b
print(time.time()-start)
# approx 0.16 sec

# numpy bahut hi jaldi kr deta h element dalne me

# list memory

a = [i for i in range(10000000)]
import sys

print(sys.getsizeof(a)) # 89095160 bytes storage

a = np.arange(10000000)
print(sys.getsizeof(a)) # 80000112


# Advanced Indexing

a = np.arange(24).reshape(6,4)
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11],
#        [12, 13, 14, 15],
#        [16, 17, 18, 19],
#        [20, 21, 22, 23]])

# 1.) fancy indexing
# so mera question h mujhe 1 3 4 rows chaite agar bolta ki 1 3 chaite so a[::2] easily you can achieve

a[[0,2,3]] # list provide krte h andar jisme likhte h kon row chaiye

# particular columns
a[:,[0,2,3]]

# bahut use hota h pandas me

# 2.) *** Boolean Indexing ***
print("dgchsdvcsdvcjksvjsvv")
# humesa index ke position se access krte h kabhi kabhi condition ke wajah se bhi access kr sakte h

# give number that are even or greater than 50

a = np.random.randint(1,100,24).reshape(6,4) # 1,100 ke beech ke 24 number randomly
#suppoose
# a ->
# array([[76, 98, 99, 39],
#        [91, 46, 88, 23],
#        [45,  6, 83,  1],
#        [37, 43, 78, 85],
#        [54, 73, 61, 53],
#        [40, 93, 85, 77]])

print(a > 50)
# [[False False  True False]
#  [False False  True  True]
#  [ True False  True False]
#  [ True False False False]
#  [ True  True  True False]
#  [ True False False False]]

# but if you want ki array me store ho jaye wahi element jo 50 se zyada h to
b = a[a>50] # 1d ke format me return krta h
print(b)
b = a[(a>50) & (a%2==0)] # jo 50 se zyada and even
print(b)

# BROADCASTING
# it describe how numpy treats array of different shape during arithmetic operations

# same shape
a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

print(a)
print(b)

print(a+b) # because they are of same shape you can add them easily

# [[0 1 2]
#  [3 4 5]]
# [[ 6  7  8]
#  [ 9 10 11]]

# [[ 6  8 10]
#  [12 14 16]]

#different shape
a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)

print(a)
print(b)

print(a+b)

# [[0 1 2] b1
#  [3 4 5]] b2
# [[0 1 2]] a

# [[0 2 4] a+b1
#  [3 5 7]] a+b2 so addition is possible

print("very good EXAMPLES OF BROADCASTING")
# max row and max column result me aata h

a = np.arange(3)+5
b = np.ones((3,3)) + np.arange(3)
c = np.arange(3).reshape((3,1)) + np.arange(3)
print("a",a)

print("b",b)

print("c",c)

# more examples

a = np.arange(12).reshape(4,3) # agar reshape hota 3,4 to workk nhi krta
b = np.arange(3) # is same as np.arange(3).reshape(1,3) so yaha hum 1 ko increase krke 4 kr denge jisse addition ho jayega
print(a)
print(b)

print(a+b)


a = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4,1)

print(a)
print(b)

print(a + b)
# [[0 1 2]]
# [[0]
#  [1]
#  [2]
#  [3]]

# [[0 1 2]
#  [1 2 3]
#  [2 3 4]
#  [3 4 5]]

# agar confuse hua broadcasting me to sir ki video dekh lena trick h


# WORKING WITH MATHEMATICAL FORMULAS

a = np.arange(10)
b = np.sum(a) # saare elemenets jhud jayenge

# SIGMIOD (DEEP LEARNING ME AATA H )

# given number ka sigmoid nikalne ka formula
# S(x) = 1/1+e^(-x)
# s sigmoid function e is euler's number

def sigmoid(array):
  return 1/(1+np.exp(-(array)))
a = np.arange(10)
b = sigmoid(a)
print(b) # [0.5        0.73105858 0.88079708 0.95257413 0.98201379 0.99330715
#  0.99752738 0.99908895 0.99966465 0.99987661]

# mean squared error ka formula banate h
# summation of 1 to n 1/n * (yi - yi^)^2
# n = total number of data points # mean
# yi = actual (observed ) vallue
# yi^ = system predicted value

actual = np.random.randint(1,50,25) # 1 se 50 ke beech ke 25 elements
predicted = np.random.randint(1,50,25)

def mse(actual , predicted):
  return np.mean((actual - predicted)**2)
b = mse(actual , predicted)
print(b)

# aese hi koi bhi mathematical function easily bana sakte ho


# WORKING WITH MISSING VALUE
# DATA MISSSING AATA H DATA ANALYSTIC KE PAAS
a = np.array([1,2,3,4,np.nan,6]) # nan missing value h
# array([ 1.,  2.,  3.,  4., nan,  6.])

# so kaise yeh missing value ko hateye
# now we do boolean indexing

np.isnan(a) # har elements se puchta h kya tu missing value ho
# [false,false,false,false,true,false]

# ab hume missing value ko hatana h
# so
b = a[~np.isnan(a)] # isme jab missing valye na ho tabhi true matlab value store hogi

print(a)
print(b)

# PLOTTING GRAPHS (NUMPY KA USE KRKE DUNIYA KA KOI GRAPH PLOT KR SAKTE HO )

# plotting a 2D plot
# x = y
x = np.linspace(-10,10,100) # -10 and 10 ke beech me 98 numbers
y = x
# so hum iska graph use krne wale h

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.savefig("grajh.png") # isse ek folder ban jayega and jisme graph plot ho jayega

x = np.linspace(-10,10,100)
y = x**2
plt.plot(x,y)
plt.savefig("graph x^2")
# aese hi sin ka graph ban jayega

y = np.sin(x)

y = x * np.log(x)

# aese hi kisi bhi function ka graph bana sakte ho 
