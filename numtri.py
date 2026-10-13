# SOME NUMPY FUNCTION THAT MAKE OUR WORK EASIER

import numpy as np
#1D
a = np.array([5, 2, 8, 1, 3])
print(np.sort(a))
#[1 2 3 5 8]
#2D
a = np.array([
    [5, 2, 8],
    [9, 1, 4]
])

print(np.sort(a)) # default row wise sorting krega np.sort(a,axis = 1)
# [[2 5 8]
#  [1 4 9]]
print(np.sort(a,axis = 0))
# [[5 1 4]
#  [9 2 8]]

# np.sort(a) new sorted array return krta h

# CANCATANATE()
#1D
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.concatenate((a,b)))
#[1 2 3 4 5 6]


#2D
a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [5,6],
    [7,8]
])

print(np.concatenate((a,b)))
# default axis = 0  rows wise add hongi
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
print(np.concatenate((a,b), axis=1))
# axis = 1 column wise add hongi
# [[1 2 5 6]
#  [3 4 7 8]]

# axis=0 → rows ke direction mein join
# axis=1 → columns ke direction mein join

# NP.UNIQUE()

# array ke unique element deta h just like set
a = np.array([1,2,2,3,3,3,4,4])
print(np.unique(a))
# [1 2 3 4]

# FREQUENCY BHI NIKAL SAKTE H
values, counts = np.unique(a,return_counts=True)
print(values)
print(counts)
# [1 2 3 4]
# [1 2 3 2]

# UNIQUE FOR 2D
a = np.array([
    [1,2],
    [2,3],
    [4,5]
])
print(np.unique(a)) # [1 2 3 4 5]
# default poore array ko cosider kr leta h

# NP.WHERE() ---->> BAHUT IMPORTANT TOPIC H

# Use 1: condition ke indices return krta h
a = np.array([10,20,30,40,50])
print(np.where(a > 25)) # default
# (array([2, 3, 4]),)

# 10 → false
# 20 → false
# 30 → true   index 2
# 40 → true   index 3
# 50 → true   index 4

# Use 2: condition ke basis par value choose karna
a = np.array([10,20,30,40,50])
result = np.where(a > 25, a, 0) # condition true then a matlab value return nhi to false matlab 0 return
print(result)
# [ 0  0 30 40 50]

# syntax : np.where(condition, value_if_true, value_if_false)


# NP.ARGMAX()
# Maximum value ka index deta hai.
a = np.array([10,50,20,80,30])

print(np.argmax(a)) # 3
# np.max 80 dega and yeh argmax uska index

a = np.array([
    [10,50,20],
    [80,30,40]
])

np.argmax(a) # 3
# default array ko flatten krke index deta h
# [10, 50, 20, 80, 30, 40]
#  0   1   2   3   4   5

print(np.argmax(a, axis=0)) # [1 0 1]
# har column wise max ka index


print(np.argmax(a, axis=1)) # [ 1 0]
# har row wise max ka index

# SAME CONCEPT FOR NP.ARGMIN

# NP.CLIP()
# Values ko ek minimum aur maximum boundary ke andar restrict karta ha

a = np.array([5,10,20,50,100])
print(np.clip(a, 10, 50)) # MIN AND MAX VALUE DONO INCLUDED
# [10 10 20 50 50]

# value < 10  → 10 MIN LIMIT AA JAYEGA
# 10-50       → same
# value > 50  → 50 MAX LIMIT AA JAYEGA

marks = np.array([-10, 20, 50, 110])
np.clip(marks, 0, 100)
# [  0  20  50 100]

# SO YEH NP.CLIP IS USEFUL FOR DATA CLEANING


# NP.PERCENTILE()
# matlab aesi value select kro jiske nhi n percentile elements liye kr
a = np.array([10,20,30,40,50])

print(np.percentile(a, 50)) # 50th percentile = median. so 50th percentile = 30
np.percentile(a, 25) # so 20 at 40 % so iske niche hi 25 % liye krega so
np.percentile(a, 75) # 40

np.percentile(a,50) # se approx median milega

# NP.CORRCOEF
# Do variables ke beech relationship kitna strong hai aur kis direction mein hai?

# Hours studied → Exam marks
# Agar student jitna zyada padhta hai, utne zyada marks aate hain, to positive correlation.

# Temperature ↑ → Heater usage ↓  NEGATIVE CORERELATION

x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])

np.corrcoef(x,y)
# [[1. 1.]
#  [1. 1.]]

# LET UNDERSTANT THE OUTPUT MATRIX
#           x     y
#        ┌─────┬─────┐
# x      │  1  │  1  │
#        ├─────┼─────┤
# y      │  1  │  1  │
#        └─────┴─────┘
# DIAGONAL ELEMENT HUMESA 1 HOGA COZ WO KHUD KE SAATH CORRELATION CHECK KR RHA
# EXAMPLE OUTPUT
# [[1.00, 0.87],
#  [0.87, 1.00]]



# -1        0        +1
# │---------│---------│
# negative  none    positive
# +1 PERFECT POSITIVE -1 PERFECT NEGATIVE
# 0.8
# 0.6
# 0.2
# -0.4
# -0.9
# YEH BHI SAB HO SAKTA H
