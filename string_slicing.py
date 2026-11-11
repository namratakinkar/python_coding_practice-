# =====================================
#  STRING SLICING
# =====================================

# there are two types of slicing.

# Two parameter slicing 
# Three parameter slicing

# ========================================
# Two Parameter Slicing
# ========================================

# Two Parameter Slicing Rule :- 

# - By default the starting point will always be 0.
# - By default the ending point will be always EXCLUDED.
# - By default the endung point will be last index.

# syntax :-

# String[Start : End]

# --------------------------------------------------------------------

# Examples :- 

# --------------------------------------------------------------------

# Example 1 :-

# 0   1   2    3    4    5    6     7    8     9     10  => indexing
# P   r   o    g    r    a    m     m    i     n     g

# my_string = "Programming"
# print(my_string)
# print(my_string[2:8])

# Explanation:- 
# Starting Point :- 2
# Ending Point :- 8(Excluded)
# Final Range :- 2 to 7
# Final Output :- ogramm
#_________________________________________________________________

# Example 2 :-

# 0   1   2    3    4    5    6     7    8     9     10  => indexing
# P   r   o    g    r    a    m     m    i     n     g

# my_string = "Programming"
# print(my_string[0:9])

# Explanation:-
# Starting Point :- 0
# Ending Point :- 9(Excluded)
# Final range :- 0 to 8
# Final Outout :- Programmi
#__________________________________________________________________

# Example 3 :-

# 0   1   2    3    4    5    6     7    8     9     10  => indexing
# P   r   o    g    r    a    m     m    i     n     g

# my_string = "Programming"
# print(my_string[4: 10])

# Explanation :-
# Starting Point :- 4
# Ending Point :- 10(Excluded)
# Final range :- 4 to 9
# Final Output :- rammin
#___________________________________________________________________

# Example 4 :-

# 0   1   2    3    4    5    6     7    8     9     10  => indexing
# P   r   o    g    r    a    m     m    i     n     g

# my_string = "Programming"
# print(my_string[ : 6])

# Explanation :-
# Starting Point :- Not Given ( By Default 0)
# Ending Point :- 6(Excluded)
# Final range :- 0 to 5
# Final Output :- progra
#____________________________________________________________________

# Example 5 :-

# 0   1   2    3    4    5    6     7    8     9     10  => indexing
# P   r   o    g    r    a    m     m    i     n     g

# my_string = "Programming"
# print(my_string[7 : ])

# Explanation :- 
# Starting Point :- 7
# Ending Point :- Not Given (By Default last index)
# Final Range :- 7 to last index
# Final Output :- ming
#_____________________________________________________________________

# Example 6 :-

# 0   1   2    3    4    5    6     7    8     9     10  => indexing
# P   r   o    g    r    a    m     m    i     n     g

# my_string = "Programming"
# print(my_string[3 : 9])

# Explanation :- 
# Starting Point :- 3
# Ending Point :- 9(Excluded)
# Final Range :- 3 to 8
# Final Output :- grammin
#_____________________________________________________________________

# Example 7 :-

# 0   1   2    3    4    5    6     7    8     9     10  => indexing
# P   r   o    g    r    a    m     m    i     n     g

# my_string = "Programming"
# print(my_string[6 : 10])

# Explanation :- 
# Starting Point :- 6
# Ending Point :- 10(Excluded)
# Final Range :- 6 to 9
# Final Output :- mmin
#_____________________________________________________________________

# Example 8 :-

# 0   1   2    3    4    5    6     7    8     9     10  => indexing
# P   r   o    g    r    a    m     m    i     n     g

# my_string = "Programming"
# print(my_string[ : ])

# Explanation :- 
# Starting Point :- Nat Given(By default 0)
# Ending Point :- Not Given (By Default last index)
# Final Range :- 0 to last index
# Final Output :- programming
#_____________________________________________________________________

# Example 9 :-

# 0   1    2    3   4    5 => indexing
# S   a    l    o   n    i

# my_string = "Saloni"
# print(my_string[ : ])

# Explanation :- 
# Starting Point :- Not Given (By default 0)
# Ending Point :- Not Given (By Default last index)
# Final Range :- 0 to last index
# Final Output :- saloni
#_____________________________________________________________________

# Example 10 :-

# 0   1    2    3   4    5 => indexing
# S   a    l    o   n    i

# my_string = "Saloni"
# print(my_string[3 : 5])

# Explanation :- 
# Starting Point :- 3
# Ending Point :- 5
# Final Range :- 3 ,4
# Final Output :- on
#_____________________________________________________________________

# Example 11 :-

# 0   1    2    3   4    5 => indexing
# S   a    l    o   n    i

# my_string = "Saloni"
# print(my_string[0 : ])

# Explanation :- 
# Starting Point :- 0
# Ending Point :- Not Given (By Default last index)
# Final Range :- 0 to last index
# Final Output :- saloni
#_____________________________________________________________________

# Example 12 :-

# 0   1    2     3     4     5
# p   y    t     h     o     n

# my_string = "python"
# print(my_string[0 : 5])

# Explanation :- 
# Starting Point :- 0
# Ending Point :- 5(Excluded)
# Final Range :- 0 to 4
# Final Output :- pytho
#_____________________________________________________________________

# Example 13 :-

# 0   1    2     3     4     5
# p   y    t     h     o     n

# my_string = "python"
# print(my_string[3 : ])

# Explanation :- 
# Starting Point :- 3
# Ending Point :- Not Given (By default last index)
# Final Range :- 3 to last index
# Final Output :- hon
#_____________________________________________________________________

# Example 14 :-

# 0   1    2     3     4     5
# p   y    t     h     o     n

# my_string = "python"
# print(my_string[ : 5])

# Explanation :- 
# Starting Point :- Not Given (By default 0)
# Ending Point :- 5(Excluded)
# Final Range :- 0 to 4
# Final Output :- pytho
#_____________________________________________________________________

# Example 15 :-

# 0   1    2     3     4     5
# p   y    t     h     o     n

# my_string = "python"
# print(my_string[ : ])

# Explanation :- 
# Starting Point :- Not Given (By default 0)
# Ending Point :- Not Given (By default last index)
# Final Range :- 0 to last index
# Final Output :- python
#_____________________________________________________________________

#===================================
# Negitive Indexing
#===================================

# Example 16 :-

#-8  -7   -6   -5   -4   -3    -2    -1
# n   o    t    e    b    o     o     k

# my_string = "NoteBook"
# print(my_string[ : ])

# Explanation :- 
# Starting Point :- Not Given (By default 0)
# Ending Point :- Not Given (By default last index)
# Final Range :-  0 to last index
# Final Output :- notebook
#_____________________________________________________________________

# Example 17 :-

#-8  -7   -6   -5   -4   -3    -2    -1
# n   o    t    e    b    o     o     k

# my_string = "NoteBook"
# print(my_string[-8 : -3])

# Explanation :- 
# Starting Point :- -8
# Ending Point :- -3(Excluded)
# Final Range :-  -8 to -4
# Final Output :- noteb
#_____________________________________________________________________

# Example 18 :-

#-8  -7   -6   -5   -4   -3    -2    -1
# n   o    t    e    b    o     o     k

# my_string = "NoteBook"
# print(my_string[-4 : ])

# Explanation :- 
# Starting Point :- -4
# Ending Point :- Not Given (By default last index)
# Final Range :-  -4 to last index
# Final Output :- book
#_____________________________________________________________________

# Example 19 :-

#-8  -7   -6   -5   -4   -3    -2    -1
# c   o    m    p    u    t     e     r

# my_string = "Computer"
# print(my_string[-8 : ])

# Explanation :- 
# Starting Point :- -8
# Ending Point :- Not Given (By default last index)
# Final Range :-  -8 to last index
# Final Output :- computre
#_____________________________________________________________________

# Example 20 :-

#-8  -7   -6   -5   -4   -3    -2    -1
# c   o    m    p    u    t     e     r

# my_string = "Computer"
# print(my_string[-7 : -1])

# Explanation :- 
# Starting Point :- -7
# Ending Point :- -1(Excluded)
# Final Range :-  -7 to -2
# Final Output :- ompute
#_____________________________________________________________________

# Example 21 :- 

#-10 -9   -8   -7   -6   -5    -4     -3    -2     -1
# t   e    c    h    n    o     l      o     g      y

# my_string = "Technology"
# print(my_string[-9 : -1])

# Explanation :- 
# Starting Point :- -9
# Ending Point :- -1(Excluded)
# Final Range :-  -9 to -2
# Final Output :- echnolog
#_____________________________________________________________________

# Example 22 :-

#-9  -8   -7   -6   -5   -4   -3   -2   -1
# d   e    v    e    l    o    p    e    r

# my_string = "Developer"
# print(my_string[-7 : -2])

# Explanation :- 
# Starting Point :- -7
# Ending Point :- -2(Excluded)
# Final Range :-  -7 to -3
# Final Output :- velop
#_____________________________________________________________________

# Example 23 :- 

#-8  -7  -6  -5  -4   -3   -2   -1
# k   e   y   b   o    a    r    d

# my_string = "keyboard"
# print(my_string[-5 : ])

# Explanation :- 
# Starting Point :- -5
# Ending Point :- Not Given (By default last index)
# Final Range :-  -5 to last index
# Final Output :- board
#_____________________________________________________________________

# Example 24 :-

#-8  -7  -6  -5  -4  -3  -2  -1
# l   a   n   g   u   a   g   e

# my_string = "Language"
# print(my_string[ : -2])

# Explanation :- 
# Starting Point :- Not Given (By default 0 [-8])
# Ending Point :- -2(Excluded)
# Final Range :-  -8 to -3
# Final Output :- langua
#_____________________________________________________________________

# Example :-

#-8  -7  -6   -5   -4   -3   -2   -1
# d   a   t    a    b    a    s    e

# my_string = "DataBase"
# print(my_string[-8 : -4])

# Explanation :- 
# Starting Point :- -8
# Ending Point :- -4(Excluded)
# Final Range :-  -8 to -5
# Final Output :- data
#_____________________________________________________________________

# ======================================
# Three Parameter Slicing
# ======================================

# Rule :-

# - By default the starting point will always be 0.
# - By default the ending point will be always EXCLUDED.  
# - By default the ending point will be last index.
# - By default the step value will be 1.

# syntax :-

# String[Start : End : Gap]

# start :- Starting point of the string.
# end :- Ending point of the string.    
# gap :- Step value of the string.
# gap = (N - 1) where N is the number of characters to be skipped.

# ------------------------------------------------------------------------

# Examples :-

# ------------------------------------------------------------------------

# Example 1 :-

# 0   1   2    3    4    5    6     7    8     9     10  => indexing
# p   r   o    g    r    a    m     m    i     n     g

# my_string = "Programming"
# print(my_string[0 : 10: 2])

# Explanation :-
# Starting Point :- 0
# Ending Point :- 10 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 0, 2, 4, 6, 8
# Final Output :- pormig
#_______________________________________________________________________

# Example 2 :-

# 0   1   2   3   4   5   6  => indexing
# P   y   t   h   o   n

# my_string = "Python"
# print(my_string[0 : 6: 2])

# Explanation :-
# Starting Point :- 0
# Ending Point :- 6 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 0, 2, 4
# Final Output :- Pto
#_______________________________________________________________________

# Example 3 :-

# 0   1   2   3   4   5   6   7   8   => indexing
# J   a   v   a   S   c   r   i   p   => Characters

# my_string = "JavaScript"
# print(my_string[0 : 9: 2])

# Explanation :-
# Starting Point :- 0
# Ending Point :- 9 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 0, 2, 4, 6, 8
# Final Output :- JvSrp
#_______________________________________________________________________

# Example 4 :-

# 0   1   2   3   4   5   6   7   => indexing
# C   o   m   p   u   t   e   r

# my_string = "Computer"
# print(my_string[1 : 7: 2])

# Explanation :-
# Starting Point :- 1
# Ending Point :- 7 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 1, 3, 5
# Final Output :- opt
#_______________________________________________________________________

# Example 5 :-

# 0   1   2   3   4   5   6   7  => indexing
# B   a   n   a   n   a

# my_string = "Banana"
# print(my_string[0 : 6: 2])

# Explanation :-
# Starting Point :- 0
# Ending Point :- 6 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 0, 2, 4
# Final Output :- Bnn
#_______________________________________________________________________

# Example 6 :-

# 0   1   2   3   4   5   6   7  => indexing
# D   e   v   e   l   o   p   e   r

# my_string = "Developer"
# print(my_string[0 : 9: 3])

# Explanation :-
# Starting Point :- 0
# Ending Point :- 9 (Excluded)
# Gap Value :- (3 - 1) = 2
# Final Range :- 0, 3, 6
# Final Output :- D e p
#_______________________________________________________________________

# Example 7 :-

# 0   1   2   3   4   5   6   7   8  => indexing
# H   a   r   d   w   a   r   e

# my_string = "Hardware"
# print(my_string[1 : 8: 2])

# Explanation :-
# Starting Point :- 1
# Ending Point :- 8 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 1, 3, 5, 7
# Final Output :- a d a e
#_______________________________________________________________________

# Example 8 :-

# 0   1   2   3   4   5   6   7  => indexing
# S   t   u   d   e   n   t

# my_string = "Student"
# print(my_string[0 : 7: 2])

# Explanation :-
# Starting Point :- 0
# Ending Point :- 7 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 0, 2, 4, 6
# Final Output :- S u e t
#_______________________________________________________________________

# Example 9 :-

# 0   1   2   3   4   5   6   7   8  => indexing
# I   n   t   e   r   n   e   t

# my_string = "Internet"
# print(my_string[0 : 8: 2])

# Explanation :-
# Starting Point :- 0
# Ending Point :- 8 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 0, 2, 4, 6
# Final Output :- I t r e
#_______________________________________________________________________

# Example 10 :-

# 0   1   2   3   4   5   6   7   8  => indexing
# W   e   b   s   i   t   e

# my_string = "Website"
# print(my_string[0 : 7: 2])

# Explanation :-
# Starting Point :- 0
# Ending Point :- 7 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 0, 2, 4, 6
# Final Output :- W b i e
#_______________________________________________________________________

# Example 11 :-

# 0   1   2   3   4   5   6   7  => indexing
# F   u   n   c   t   i   o   n

# my_string = "Function"
# print(my_string[1 : 8: 2])

# Explanation :-
# Starting Point :- 1
# Ending Point :- 8 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 1, 3, 5, 7
# Final Output :- u c i n
#_______________________________________________________________________

# Example 12 :-

# 0   1   2   3   4   5   6   7   8  => indexing
# D   a   t   a   b   a   s   e

# my_string = "Database"
# print(my_string[0 : 8: 3])

# Explanation :-
# Starting Point :- 0
# Ending Point :- 8 (Excluded)
# Gap Value :- (3 - 1) = 2
# Final Range :- 0, 3, 6
# Final Output :- D a s
#_______________________________________________________________________

# Example 13 :-

# 0   1   2   3   4   5   6   7  => indexing
# G   i   t   h   u   b

# my_string = "Github"
# print(my_string[0 : 6: 2])

# Explanation :-
# Starting Point :- 0
# Ending Point :- 6 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 0, 2, 4
# Final Output :- G t u
#_______________________________________________________________________

# Example 14 :-

# 0   1   2   3   4   5   6   7   8  => indexing
# S   c   h   o   o   l   i   n   g

# my_string = "Schooling"
# print(my_string[1 : 9: 3])

# Explanation :-
# Starting Point :- 1
# Ending Point :- 9 (Excluded)
# Gap Value :- (3 - 1) = 2
# Final Range :- 1, 4, 7
# Final Output :- c o n
#_______________________________________________________________________

# Example 15 :-

# 0   1   2   3   4   5   6   7   8  => indexing
# L   a   p   t   o   p

# my_string = "Laptop"
# print(my_string[1 : 6: 2])

# Explanation :-
# Starting Point :- 1
# Ending Point :- 6 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- 1, 3, 5
# Final Output :- a t p
#_______________________________________________________________________

# ===============================================
#  Negative Indexing with Three Parameter Slicing
# ===============================================

# Example 16 :-

#  -7  -6  -5  -4  -3  -2  -1 => negative indexing
#   W   e   b   s   i   t   e

# my_string = "Website"
# print(my_string[-7 : -1: 2])  

# Explanation :-
# Starting Point :- -7
# Ending Point :- -1 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- -7, -5, -3, -1
# Final Output :- W b i e
#_______________________________________________________________________

# Example 17 :-

#  -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 => negative indexing
#   P   r   o   g   r   a   m   m   i   n   g

# my_string = "Programming"
# print(my_string[-11 : -1: 2])

# Explanation :-
# Starting Point :- -11
# Ending Point :- -1 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- -11, -9, -7, -5, -3
# Final Output :- Pormg
#_______________________________________________________________________

# Example 18 :-

#  -6  -5  -4  -3  -2  -1 => negative indexing
#   P   y   t   h   o   n

# my_string = "Python"
# print(my_string[-6 : -1: 2])

# Explanation :-
# Starting Point :- -6
# Ending Point :- -1 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- -6, -4, -2
# Final Output :- Pto
#_______________________________________________________________________

# Example 19 :-

#  -10 -9  -8  -7  -6  -5  -4  -3  -2  -1 => negative indexing
#   J   a   v   a   S   c   r   i   p   t

# my_string = "JavaScript"
# print(my_string[-10 : -1: 2])

# Explanation :-
# Starting Point :- -10
# Ending Point :- -1 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- -10, -8, -6, -4, -2
# Final Output :- JvSrp
#_______________________________________________________________________

# Example 20 :-

#  -8  -7  -6  -5  -4  -3  -2  -1 => negative indexing
#   C   o   m   p   u   t   e   r

# my_string = "Computer"
# print(my_string[-7 : -1: 2])

# Explanation :-
# Starting Point :- -7
# Ending Point :- -1 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- -7, -5, -3
# Final Output :- o p t
#_______________________________________________________________________

# Example 21 :-

#  -6  -5  -4  -3  -2  -1 => negative indexing
#   B   a   n   a   n   a

# my_string = "Banana"
# print(my_string[-6 : -1: 2])

# Explanation :-
# Starting Point :- -6
# Ending Point :- -1 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- -6, -4, -2
# Final Output :- Bnn
#_______________________________________________________________________

# Example 22 :-

#  -9  -8  -7  -6  -5  -4  -3  -2  -1 => negative indexing
#   D   e   v   e   l   o   p   e   r

# my_string = "Developer"
# print(my_string[-9 : -1: 3])

# Explanation :-
# Starting Point :- -9
# Ending Point :- -1 (Excluded)
# Gap Value :- (3 - 1) = 2
# Final Range :- -9, -6, -3
# Final Output :- D e p
#_______________________________________________________________________

# Example 23 :-

#  -8  -7  -6  -5  -4  -3  -2  -1 => negative indexing
#   H   a   r   d   w   a   r   e

# my_string = "Hardware"
# print(my_string[-7 : -1: 2])

# Explanation :-
# Starting Point :- -7
# Ending Point :- -1 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- -7, -5, -3
# Final Output :- a d a
#_______________________________________________________________________

# Example 24 :-

#  -7  -6  -5  -4  -3  -2  -1 => negative indexing
#   S   t   u   d   e   n   t

# my_string = "Student"
# print(my_string[-7 : -1: 2])

# Explanation :-
# Starting Point :- -7
# Ending Point :- -1 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- -7, -5, -3
# Final Output :- S u e
#_______________________________________________________________________

# Example 25 :-

#  -8  -7  -6  -5  -4  -3  -2  -1 => negative indexing
#   I   n   t   e   r   n   e   t

# my_string = "Internet"
# print(my_string[-8 : -1: 2])

# Explanation :-
# Starting Point :- -8
# Ending Point :- -1 (Excluded)
# Gap Value :- (2 - 1) = 1
# Final Range :- -8, -6, -4, -2
# Final Output :- I t r e
#_______________________________________________________________________