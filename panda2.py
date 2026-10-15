# Dataframe
import numpy as np
import pandas as pd

# 2d structure of data containing rows and columns i.e table are known as dataframe

# dataframe ke andar ka ek single column hi series hota h
# each rows and each col of datafrane are series

# CREATING DATAFRAME

# using lists
student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

a = pd.DataFrame(student_data,columns=['iq','marks','package'])
print(a)
#     iq  marks  package
# 0  100     80       10
# 1   90     70        7
# 2  120    100       14
# 3   80     50        2

# using dicts

student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

students = pd.DataFrame(student_dict)
students.set_index('name',inplace=True)
print(students)
#           iq  marks  package
# name
# nitish   100     80       10
# ankit     90     70        7
# rupesh   120    100       14
# rishabh   80     50        2
# amit       0      0        0
# ankita     0      0        0

# using read_csv
movies = pd.read_csv('movies.csv') # agar same directory me h tab
print(movies)

ipl = pd.read_csv('ipl-matches.csv')

# DataFrame Attributes and Methods

# shape
movies.shape # (1629,28) # rows and col
ipl.shape
# (950, 20)

# dtypes
movies.dtypes
ipl.dtypes
# sare volumn ks

# ID                   int64
# City                object
# Date                object
# Season              object
# MatchNumber         object
# Team1               object
# Team2               object
# Venue               object
# TossWinner          object
# TossDecision        object
# SuperOver           object
# WinningTeam         object
# WonBy               object
# Margin             float64
# method              object
# Player_of_Match     object
# Team1Players        object
# Team2Players        object
# Umpire1             object
# Umpire2             object
# dtype: object

# index
print(movies.index)
print(ipl.index)
# RangeIndex(start=0, stop=1629, step=1)
# RangeIndex(start=0, stop=950, step=1)

# columns
movies.columns # isme jitne bhi columns names h wo sab fetch kr ke dedega
ipl.columns
print(students.columns)
#Index(['iq', 'marks', 'package'], dtype='object')


# values. -> dataframe me jitne bhi values h wo return kr ke dedega
students.values
ipl.values # here multiple columns so 2d array return hoga

# head and tail
movies.head(2) # top 2 head ki rows mil jayega


# sample -> randomly row nikalke deta h
ipl.sample(5) # randomly 5 rows return krega

# info -> very important function
print(movies.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1629 entries, 0 to 1628
# Data columns (total 18 columns):
#  #   Column            Non-Null Count  Dtype
# ---  ------            --------------  -----
#  0   title_x           1629 non-null   object
#  1   imdb_id           1629 non-null   object
#  2   poster_path       1526 non-null   object
#  3   wiki_link         1629 non-null   object
#  4   title_y           1629 non-null   object
#  5   original_title    1629 non-null   object
#  6   is_adult          1629 non-null   int64
#  7   year_of_release   1629 non-null   int64
#  8   runtime           1629 non-null   object
#  9   genres            1629 non-null   object
#  10  imdb_rating       1629 non-null   float64
#  11  imdb_votes        1629 non-null   int64
#  12  story             1609 non-null   object
#  13  summary           1629 non-null   object
#  14  tagline           557 non-null    object
#  15  actors            1624 non-null   object
#  16  wins_nominations  707 non-null    object
#  17  release_date      1522 non-null   object
# dtypes: float64(1), int64(3), object(14)
# memory usage: 229.2+ KB


# describe
print(movies.describe()) # yeh mathematical column ka summary nikal ke deta h
# None
#        is_adult  year_of_release  imdb_rating     imdb_votes
# count    1629.0      1629.000000  1629.000000    1629.000000
# mean        0.0      2010.263966     5.557459    5384.263352
# std         0.0         5.381542     1.567609   14552.103231
# min         0.0      2001.000000     0.000000       0.000000
# 25%         0.0      2005.000000     4.400000     233.000000
# 50%         0.0      2011.000000     5.600000    1000.000000
# 75%         0.0      2015.000000     6.800000    4287.000000
# max         0.0      2019.000000     9.400000  310481.000000


# isnull -> imp ....pure column me check hota kaha kaha missing values h in bool
print(movies.isnull())

#       title_x  imdb_id  poster_path  wiki_link  ...  tagline  actors  wins_nominations  release_date
# 0       False    False        False      False  ...     True   False             False         False
# 1       False    False         True      False  ...     True   False              True         False
# 2       False    False        False      False  ...     True   False              True         False
# 3       False    False        False      False  ...     True   False              True         False
# 4       False    False         True      False  ...     True   False             False         False
# ...       ...      ...          ...        ...  ...      ...     ...               ... ...
# 1624    False    False        False      False  ...     True   False              True         False
# 1625    False    False        False      False  ...     True   False              True         False
# 1626    False    False         True      False  ...     True   False              TrueTrue
# 1627    False    False        False      False  ...     True   False              True         False
# 1628    False    False        False      False  ...     True   False              True         False

# [1629 rows x 18 columns]

# is gande data ko samjhne wale data matalab bas yeh pata krna h li is column me kitne missing value h uske liye sum use. krenge

print(movies.isnull().sum())
# title_x                0
# imdb_id                0
# poster_path          103
# wiki_link              0
# title_y                0
# original_title         0
# is_adult               0
# year_of_release        0
# runtime                0
# genres                 0
# imdb_rating            0
# imdb_votes             0
# story                 20
# summary                0
# tagline             1072
# actors                 5
# wins_nominations     922
# release_date         107
# dtype: int64

# duplicated
print(movies.duplicated())
# 0       False
# 1       False
# 2       False
# 3       False
# 4       False
#         ...
# 1624    False
# 1625    False
# 1626    False
# 1627    False
# 1628    False
# Length: 1629, dtype: bool
movies.duplicated().sum() # kitne duplicate rows h
# 0

print(students)

#           iq  marks  package
# name
# nitish   100     80       10
# ankit     90     70        7
# rupesh   120    100       14
# rishabh   80     50        2
# amit       0      0        0
# ankita     0      0        0
# None

# mujhe iske column me marks ko rename krke percent and package ko lpa so

print(students.rename(columns = {'marks':'percent','package':'lpa'},inplace = True)) # once again yeh bhi value return krta h original me changes nhi krta h ... agar original me change krne h to inplace = true use krna ho

print(students)
#           iq  percent  lpa
# name
# nitish   100       80   10
# ankit     90       70    7
# rupesh   120      100   14
# rishabh   80       50    2
# amit       0        0    0
# ankita     0        0    0

# MATH METHODS

# SUM -> saare col ke values agar int me h sum ho jayega and string then concatanate ho jayega

print(students.sum())
# iq         390
# percent    300
# lpa         33
# dtype: int64
print(students.sum(axis = 1)) # row wise sum hoga
# name
# nitish     190
# ankit      167
# rupesh     234
# rishabh    132
# amit         0
# ankita       0
# dtype: int64

# aese hi yeh h
students.mean()
students.var()
# ispe bhi axis wise kam kr sakte h default column wise hi krte h

# SELECTING COLS FROM A DATAFRAME

# single cols -> single col fetching
print(movies['title_x']) # ek single column fetch ho gya and yeh series hi hota h and iska type bhi series hoga
# 0                   Uri: The Surgical Strike
# 1                              Battalion 609
# 2       The Accidental Prime Minister (film)
# 3                            Why Cheat India
# 4                            Evening Shadows
#                         ...
# 1624                   Tera Mera Saath Rahen
# 1625                    Yeh Zindagi Ka Safar
# 1626                         Sabse Bada Sukh
# 1627                                   Daaka
# 1628                                Humsafar
# Name: title_x, Length: 1629, dtype: str

# multiple cols fetching
movies[['title_x','year_of_release','actors']] # multipkes col fetch krne ke liye and iska type hoga dataframe coz multiple series taken out
# and order hamare hisab  se hi fetch hoga


# SELECTING ROWS FROM A DATAFRAME



student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

students = pd.DataFrame(student_dict)
students.set_index('name',inplace=True) # set index se name column as a index banega na ki 0 1 2
print(students) # bhale hi humne students ka index name de diya but wo fetch apne default index se bhi ho jayega

#           iq  marks  package
# name
# nitish   100     80       10
# ankit     90     70        7
# rupesh   120    100       14
# rishabh   80     50        2
# amit       0      0        0
# ankita     0      0        0

# iloc - searches using index positions
# loc - searches using index labels

# single row -> dataframe me se ek single row ya single column nikalo wo ek series hi hoga

print(students.iloc[0])
# so isse nitish index ke saare information aa jayegi and it will be series

# iq         100
# marks       80
# package     10
# Name: nitish, dtype: int64

# multiple rows fetch krne ke lite
print(students.iloc[0:3]) # YAHA SLICING POSSSIBLE
# isse 3 row fetch ho jayegi

#          iq  marks  package
# name
# nitish  100     80       10
# ankit    90     70        7
# rupesh  120    100       14


# FANCY INDEXING
movies.iloc[[0,4,5]]


# AB INDEX WISE FETCHING HO GYI WITH ILOC

# NOW FETCH WITH THE USE OF INDEX LABEL

students.loc['nitish']

# now multiple items want

students.loc['nitish':'rishabh':2] # 2 2 jump krega
# so iska matlab h nitish se rishabh tak ke sab item fetch INCLUDING RISHABH

# iloc and loc me difference yahi h ki iloc me last element excluded and loc me included

# SELECTING BOTH ROWS AND COLUMNS
# rows and column dono saath me fetch

# suppose fetch 3 movies and pahle 2 columns ka data chaiye bas
# using iloc
print(movies.iloc[0:3,0:2])
#                                 title_x    imdb_id
# 0              Uri: The Surgical Strike  tt8291224
# 1                         Battalion 609  tt9472208
# 2  The Accidental Prime Minister (film)  tt6986710

# using loc
print(movies.loc[0:3,'title_x':'imdb_id']) # isse bhi wahi aayega and label kaa naam hi 0 1 2 h

# jab bhi tum dataframe banaoge uska index kuch bhi ho but internally uska indexing ho jata 0 1 2 jo iloc ke through access kr pate h


# FILTERING A DATAFRAME -> VERY VERY IMPORTANT

# 1.) FIND ALL THE FINAL WINNERS #  IPL ke  har saal ke winner dena h
masks = ipl['MatchNumber'] == 'Final'
new_df = ipl[masks]
print(new_df[['Season','WinningTeam']])

# method -2
ipl[ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']] # ek line me puracode

# 2.) how many super over finishes have occured
ipl[ipl['SuperOver'] == 'Y'].shape[0] # coz shape column and rows dono bata rha

# 3.) how many matches has csk won in kolkata
# ipl[ipl['WinningTeam','City'] == ['CSK','kolkata']].shape[0] # wrong coz do column ko ek saaath compare nhi kr sakte

print(ipl[(ipl['WinningTeam'] == 'Chennai Super Kings') & (ipl['City']=='Kolkata')
].shape[0])
# 5

# 4.) toss winner is match winner in percentage

print((ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100) # 51

# 5.) # movies with rating higher than 8 and votes>10000
movies[(movies['imdb_rating'] > 8.5) & (movies['imdb_votes'] > 10000)].shape[0]

# 6.) # Action movies with rating higher than 7.5
# yeh tricky h coz ek movie ke genre 3 bhi h jaise Action/Drama/Musical
# so hume split krna padega  string me split
masks1 = movies['genres'].str.split('|').apply(lambda x : 'Action' in x) # apply condition check ke liye hota h and return true or false krta h
masks2 = movies['imdb_rating'] > 7.5
print(movies[masks1 & masks2])

1:42:35
