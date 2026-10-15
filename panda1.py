# PANDAS (REALLY INTERESTING LIBRARY AND CAN BE USED IN REAL LIFE )

# pandas numpy ke upar hi bana h

# Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.

# DATA SAMJHNE KE LIYE USKE ANALYSIS KRKE KE LIYE PANDA USE HOTA H

# PANDA OBJECT MOST IMPORTANT -> 1.) SERIES AND 2.) DATAFRAME

# panda series is 1d data jaha kisi type ka datatype store kr sakte ho
# A Pandas Series is like a column in a table. It is a 1-D array holding data of any type.
import numpy as np # recommended ki pandas import to numpy bhi import
import pandas as pd

# SERIES FROM LISTS

country = ['India','Pakistan','USA','Nepal','Srilanka'] # SO IS LIST KA MAIN SERIES BANANA CHAHTA HU

print(pd.Series(country)) # index wise assign ho jata h
# 0       India
# 1    Pakistan
# 2         USA
# 3       Nepal
# 4    Srilanka
# dtype: str
# kabhi kabhi str as object show hota h dtype me

# integers
runs = [13,24,56,78,100]
runs_ser = pd.Series(runs)

# custom indexing
marks = [67,57,89,100]
subjects = ['maths','english','science','hindi']

print(pd.Series(marks,index=subjects))
# maths       67
# english     57
# science     89
# hindi      100
# dtype: int64


# setting a name
marks = pd.Series(marks,index=subjects,name='Nitish ke marks')
# maths       67
# english     57
# science     89
# hindi      100
# Name: Nitish ke marks, dtype: int64

# SERIES FROM DICT

marks = {
    'maths':67,
    'english':57,
    'science':89,
    'hindi':100
}

marks_series = pd.Series(marks,name='nitish ke marks') # MARKS LIKH KE DONO AA GYE KEY AND items

# maths       67
# english     57
# science     89
# hindi      100
# Name: nitish ke marks, dtype: int64

# SERIES ATTRIBUTES

# 1.) SIZE
marks_series.size # key value pairs ka size return kr deta h
# so 4

# 2.) DTYPE
marks_series.dtype # dtype('int64')
# yeh item ka datatype return krta h

# 3.) name
marks_series.name
# nitish ke marks

# 4.) isunique
# yeh saare elements check krke deta h ki koi item repeat nhi kr rha ... agar repeat kiya to False
marks_series.is_unique # True coz koi item repeat nhi kr rha
pd.Series([1,1,2,3,4,5]).is_unique # false coz repeat


# 5.) index
marks_series.index
# Index(['maths', 'english', 'science','hindi'], dtype='object')
# saare index return krta h with their dtype ..agar object dikha to samjh jana string hi h

# 6.) values
marks_series.values
# array([ 67,  57,  89, 100])



# SERIES USING READ_CSV(ISKA KAAM CSV FILE KO READ KRNA  )

# CSV ARE DATASETS OF COMMA SEPERATED VALUES

# CSV FILE
# EmployeeID,FirstName,LastName,Department,Salary
# 101,John,Smith,Sales,55000
# 102,Jane,Doe,Marketing,62000
# 103,Alex,Jones,IT,75000
# 104,Maria,Garcia,HR,58000

# ab hum subs.csv ko series pe convert krenge series me

# csv file with 1 column (subs gain)
pd.read_csv('/workspaces/pylib/subs.csv') # csv file pe jake copy path kro
# pd.read_csv data ko default dataframe format me lata h

# so hume explicitely data ko series me convert krenge

subs = pd.read_csv('/workspaces/pylib/subs.csv').squeeze("columns") # isse series me convert ho jayega
print(subs)
# 0       48
# 1       57
# 2       40
# 3       43
# 4       44
#       ...
# 360    231
# 361    226
# 362    155
# 363    144
# 364    172
# Name: Subscribers gained, Length: 365, dtype: int64


# so yeh upar ke 5 and niche ke 5 dikhata h coz pure data load me dikkat aa sakti h

# with 2 columns (matchno and runs)
vk = pd.read_csv('/workspaces/pylib/kohli_ipl.csv',index_col = 'match_no').squeeze("columns") # index column se yeh hota h ki konsa col index banega
print(vk)

# movie and lead
movies = pd.read_csv('/workspaces/pylib/bollywood.csv',index_col = 'movie').squeeze("columns")

print(movies)
# movie
# Uri: The Surgical Strike                   Vicky Kaushal
# Battalion 609                                Vicky Ahuja
# The Accidental Prime Minister (film)         Anupam Kher
# Why Cheat India                            Emraan Hashmi
# Evening Shadows                         Mona Ambegaonkar
#                                               ...
# Hum Tumhare Hain Sanam                    Shah Rukh Khan
# Aankhen (2002 film)                     Amitabh Bachchan
# Saathiya (film)                             Vivek Oberoi
# Company (film)                                Ajay Devgn
# Awara Paagal Deewana                        Akshay Kumar
# Name: lead, Length: 1500, dtype: str



# SERIES METHODS

# 1.)  head(upar ke 5 rows dega ) and tail(niche ke ) ..
print(subs.head())
# 0    48
# 1    57
# 2    40
# 3    43
# 4    44
# Name: Subscribers gained, dtype: int64

# vice versa for tail

# supose 3 head chaiye
print(vk.head(3))
# 1     1
# 2    23
# 3    13
# Name: runs, dtype: int64

# 2.) Sample
movies.sample() # randomly one row nikalta h

movies.sample(5) # randomly 5 value chaiye

# randomly seelect krne ke liye use hota h

# 3.) value_counts

movies.value_counts() # data me har item ka frequency nikal ke deta h

# so if i want ki har actor ne kitne movie ki h

# Akshay Kumar        48
# Amitabh Bachchan    45
# Ajay Devgn          38
# Salman Khan         31
# Sanjay Dutt         26
#                     ..
# Diganth              1
# Parveen Kaur         1
# Seema Azmi           1
# Akanksha Puri        1
# Edwin Fernandes      1
# Name: lead, Length: 566, dtype: int64

# automatically descending order me return krta h


# 4.) sort_values -> inplace
print(vk.sort_values()) # ascending order me sort
#match_no
# 8        0
# 87       0
# 93       0
# 91       0
# 206      0
#       ...
# 164    100
# 120    100
# 123    108
# 126    109
# 128    113
# Name: runs, Length: 215, dtype: int64

# descending sort
vk.sort_values(ascending = False).head(1).values
# head(1) se top row bas dedega...
# values se us top row ki value de dega

# is vk.sort_values se orignal change nhi hota bas sorted return hota h agar tu original change krna chahta h to .. vk.sort_values(inplace = True) isse ho jayega


# 5.) sort_index -> inplace -> movies

movies.sort_index(ascending=False,inplace=True)
# index descending order me sort hoga   z->a
# and 9 -> 0
print(movies)
# movie
# Zor Lagaa Ke...Haiya!            Meghan Jadhav
# Zokkomon                       Darsheel Safary
# Zindagi Tere Naam           Mithun Chakraborty
# Zindagi Na Milegi Dobara        Hrithik Roshan
# Zindagi 50-50                      Veena Malik
#                                    ...
# 2 States (2014 film)              Arjun Kapoor
# 1971 (2007 film)                Manoj Bajpayee
# 1920: The Evil Returns             Vicky Ahuja
# 1920: London                     Sharman Joshi
# 1920 (film)                   Rajniesh Duggall
# Name: lead, Length: 1500, dtype: str


# SERIES MATHS METHODS
# count (nan ko count nhi krta but size count krta h)
vk.count()
# 215

# sum -> product
subs.sum() # saari values ka sum nikal ke de

subs.product() # saari values ka product

# mean -> median -> std -> var
subs.mean()
vk.median()
movies.mode()
subs.std() # standard deviation
vk.var() # variance

# min / max
subs.max() # 396
# kis din max subscriber gain kiya


# describe
print(vk.describe())
# count    215.000000
# mean      30.855814
# std       26.229801
# min        0.000000
# 25%        9.000000
# 50%       24.000000
# 75%       48.000000
# max      113.000000
# Name: runs, dtype: float64


# SERIES INDEXING

# integer indexing
x = pd.Series([12,13,14,35,46,57,58,79,9])
# x[0] -> 12

# negative indexing not worj
# x[-1] error

# so jaise lead  h usko movies index se bhi fetch kr sakte and movies[0] bhi work krega first ko fetch ke liye

# and agar tumhara index agar string h to negative indexing uspe work krega


# SLICING (multiple items fetch krna)

vk[5:16] # 5 se 16 ke andar ke data denhe

vk[-5:] # last 5 elements -> -5 se leke last tak

# slicing as it is work krta h jaise python me krta h


# FANCING INDEXING
vk[[1,3,4,5]] # koi pattern nhi ban rha hume wahi chaiye jo hum mang rhe



# EDITING ITEM INSIDE A SERIES

# abhi tak hum read kr rhe the ab hum write kr rhe although yeh krna nhi chaite but seekh lete h

print(marks_series)
# maths       67
# english     57
# science     89
# hindi      100
# Name: nitish ke marks, dtype: int64

marks_series['english'] = 100

# english ka marks 100 ho gye

# what if an index doesnt exist

marks_series['sst'] = 22
# agar marks_series[1] = 100 ->  1 key pe 100 aa jata
# so agar read krte to error deta but write krte time sst add krke uska value 22 kr dega

print(marks_series)

# maths       67
# english    100
# science     89
# hindi      100
# sst         22
# Name: nitish ke marks, dtype: int64


# slicing
print(runs_ser)
# 0     13
# 1     24
# 2     56
# 3     78
# 4    100
# dtype: int64

runs_ser[2:4] = [100,100]
print(runs_ser)
# 0     13
# 1     24
# 2    100
# 3    100
# 4    100
# dtype: int64

# aese hi fancy indexing
runs_ser[[0,3,4]] = [0,0,0]

# using index label
movies['2 States (2014 film)'] = 'Alia bhatt'
print(movies)
# movie
# Zor Lagaa Ke...Haiya!            Meghan Jadhav
# Zokkomon                       Darsheel Safary
# Zindagi Tere Naam           Mithun Chakraborty
# Zindagi Na Milegi Dobara        Hrithik Roshan
# Zindagi 50-50                      Veena Malik
#                                    ...
# 2 States (2014 film)                Alia bhatt
# 1971 (2007 film)                Manoj Bajpayee
# 1920: The Evil Returns             Vicky Ahuja
# 1920: London                     Sharman Joshi
# 1920 (film)                   Rajniesh Duggall
# Name: lead, Length: 1500, dtype: str

# SERIES WITH PYTHON FUNCTIONALITIES

# len/type/dir/sorted/max/min
print(len(subs)) # 365 items in subs series
print(type(subs)) # <class 'pandas.core.series.Series'>
print(dir(subs)) # series ke saare atributes and methods dikhega
print(sorted(subs)) # ascending me sorted subsriber gained
print(min(subs)) # max subs
print(max(subs)) # min subs gained


# TYPE CONVERSION
print(marks_series)
# maths       67
# english    100
# science     89
# hindi      100
# sst         22
# Name: nitish ke marks, dtype: int64

# if i want to convert this into list  list
print(list(marks_series)) #[67, 100, 89, 100, 22].   values list me store ho jayengi
print(dict(marks_series))
# {'maths': np.int64(67), 'english': np.int64(100), 'science': np.int64(89), 'hindi': np.int64(100), 'sst': np.int64(22)}


# membership operator

'2 States (2014 film)' in movies # yeh sirf keys pe kaam krta h na ki values pe

# True

# for values
'Alia bhatt' in movies.values
# true


# LOOPING
for i in movies:
    print(i)
# saari values print ho jayegi keys nhi hogi

# for index printing
for i in movies.index:
    print(i)
# saari keys print ho jayegi


# ARITHMETIC OPERATORS (broadcasting)


# we want har subject me 100 se kitne kam marks aaye
print(100 - marks_series) # har subject me 100 lane ke liye kitne number chaiye
# maths      33
# english     0
# science    11
# hindi       0
# sst        78
# Name: nitish ke marks, dtype: int64



# RELATIONAL OPERATORS

# kitne matches me virat ne 5 se zyada score kiya
print(vk >= 50)
# match_no
# 1      False
# 2      False
# 3      False
# 4      False
# 5      False
#        ...
# 211    False
# 212    False
# 213     True
# 214    False
# 215    False
# Name: runs, Length: 215, dtype: bool


# Boolean Indexing on Series

# Find no of 50's and 100's scored by kohli
vk[vk >= 50].size # true vali values vk me store ho gyi and return krega
# 50

# find number of ducks
vk[vk == 0].size
# 9

# Count number of day when I had more than 200 subs a day
subs[subs > 200].size
# 59


# find actors who have done more than 20 movies
num_movies = movies.value_counts() # har actor ke number of moveies count ho jayega and num_movies me store ho jayega

print(num_movies[num_movies > 20])
# lead
# Akshay Kumar        48
# Amitabh Bachchan    45
# Ajay Devgn          38
# Salman Khan         31
# Sanjay Dutt         26
# Shah Rukh Khan      22
# Emraan Hashmi       21
# Name: count, dtype: int64



# PLOTTING GRAPH ON SERIES

# suppose i want to plot a graph of subscriber gained per day graph

import matplotlib.pyplot as plt
subs.plot()
plt.savefig("seriesgraph")
# ban gya grpah

movies.value_counts().head(20).plot(kind='pie')
plt.savefig("seriespie")
# movies.value_counts series ke head ke 20 element ka pie graph ban gya

#Some Important Series Methods

# astype
# between
# clip
# drop_duplicates
# isnull
# dropna
# fillna
# isin
# apply
# copy

