# LEARNING NUMPY
# it is library of python for scientific (mathematical) computing
# it is a n dimensional arrays of homogeneous data types
# aage khud dekh lena
# it is one of the most important library in python

# CREATING NUMPY ARRAY
import numpy as np
a = np.array([1,2,3]) # yeh 1D array h (vector)
b = np.array([[1,2,3],[7,2,6]]) # 2D array (matrix)
print(a)
print(b)
c = np.array([[[1,2],[3,4],[5,9]]]) # 3d array (tensor)
print(c)
d = np.array([1,2,4],dtype = float) # dtype se convert ho jate h ..... agar float ke jagah bool likha hota to output hota array([true , true , true]) coz non zero saari values ko python true ki tarah treat krta h
print(d)
# range in numpy as arange
e = np.arange(1,11,2) # [1,3,5,7,9] just like for loop 
print(e)

# reshape array
np.arange(1,11).reshape(2,5) # 2 rows and 5 columns wale matrix me convert kr deta h .....utna ko matrix only bana sakte ho jitna array me presesnt hoga .... jaise 10 element h tabhi 2 , 5 ka bana sakte h nhi to nhi

#np.ones
np.ones((3,4)) # 3 rows and 4 columns me sirf 1 values bhar dega
# use - neural network me bahut use hota h yeh

# np.zeroes same hota h as np.ones but zero bhar jata h

#np.random.random((3,4)) # yeh random number bhar deta utne hi rows and columns me .. do random isiliye coz random class bhi h and uska method bhi random hi h

# np.linspace
f = np.linspace(-10,10,7)# -10 initial value in array 10 is final value in that array and 7 matlab ki beech me random koi 5 points generate kr dega jisse array me 7 points ho jayenge
g = np.linspace(-10,10,7,dtype = int) # ab beech ki value integer hogi

print(f) # used in machine learning

# np.identity isse ek identity matrix ban jati h jiska # np.identity(3) 3*3 ke

# kahin bhi arguments me , dtype = jo bhi chaiye datatype daal do wohi return krega

# ARRAY ATTRIBUTES

h = np.identity(3,dtype = int) #3*3 array 2D
print(h.ndim) # ndim arrray ka dimension return krta h

print(h.shape) # (kitne matrix h agar 1 h to no value , unke rows , unke columns ) and sabke rows and columns same honi hi chaiye
print(h.size) # no. of elements returb krega

print(h.itemsize) # isse jo andar ke datatype ka byte size h wo return krega jaise for float it will return 8

print(h.dtype) # yeh batatype h tumhare elements ka datatype kya h

# CHANGING DATATYPES

# astype
# h ka dtype float64 matlab float value h and 64 size h ..so main agar age kisi ka kr rha and age 100 se zyada nhi jayegi so main kya krunga astype ka use krke 64 bit ko 32 bit kr dunga
s = h.astype(np.int32) # h.astype return krta h convert nhi krta h
print(s.dtype)

# ARRAY OPERATION
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

# scalar operation
#1.) Arithmetic operators
# so yeh scalar ke saath operation kr sakte h
print(a1*2) # saare elements 2 se multyply ho jayenge
# so python ke jitne bhi operators h yaha apply kr sakte ho
#2.) Relational operators
print(a2 > 15) # saare elements ke saath compare krega and boolean me ek matrix return krega

# vector operation
#1.) arithmetic
print(a1+a2) # saare element add ho jayenge ek doosre se
# saare arithmetic operation kr sakte ho

# ARRAY FUNCTION ... IT IS VERY IMPORTANT COZ NUMPY ME BAHUT SAARE FUNCTIONS H

a1 = np.random.random((3,3))
a1 = np.round(a1*100)
# a1 ek matrix h 3*3 ka jiske elements under 100 h rounded
np.max(a1) # max eleement nikal ke dega
np.min(a1) # min
np.sum(a1) # saare elements ka sum nikal ke dea
np.prod(a1) # saare elements ka product dega

# so i want suppose har row ka min element
# 0 -> column and 1 -> rows
np.max(a1,axis = 1) # rows wise max element
np.max(a1,axis = 0) # column wise
# jaise yeh rows and columns max ke liye kiya aese hi min , sum , prod ke liye bhi kr sakte h

# till 1:03:55

# aese hi kuch or mathematical function h
z = np.var(a1,axis = 1) # saari rows ka variance nikal lega
print(z)
np.sin(a1) # saare a1 ke elements ka sin le lega jaise agar element hua x1 so sin(x1)

a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)
np.dot(a2,a3) # isse dot product nikal jayega .....a2 * a3

np.exp(a1) # isse jo jo element h wo power ho jayenge jaise if an element is x so output for that is e^x

np.ceil(np.random.random((2,3))*100)

# round/floor/ceil

print(np.ceil(np.random.random((2,3))*100)) # so isme 2 rows and 3 columns pe random value generate hua and usko phir round off kiya 100 se so 100 ke andar ki value aa gyi and then ceil use kiye jisse us decimal value ke sabse nazdeek integer value ho jayega


