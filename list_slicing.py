
# ==============================
#  Python List Slicing
# ==============================

# Definition:

# list slicing is used in python to extract some elements from a list, tuple, or string.

# Syntax:

# list_name[start : end]

# Rules:

# Starting Point = Included
# Ending Point = Excluded

# slicing are of two types.

# 1. Two parameter slicing - list name[start : end].
# 2. three parameter slicing - list name[start : end : gap].

# ======================================
# 1. Two parameter slicing
# ======================================

# ==================================================
# 1. POSITIVE INDEXING - LIST SLICING
# ==================================================

# Definition:
# Positive Indexing starts from 0 and moves from Left to Right.

# ---------------
#  Examples :-
# ---------------

# indexing:   0       1     2       3      4      5
# my_list = ["Amit", 25, "Python", True, 85.5, "Delhi"]

# Example 1:-
# print(my_list[0:3])

# Explanation:
# Starting Point = 0
# Ending Point = 3 (Excluded)
# So Final Range = 0 to 2
# Final Output = ["Amit", 25, "Python"]

# --------------------------------------------------

# Example 2:-
# print(my_list[1:4])

# Explanation:
# Starting Point = 1
# Ending Point = 4 (Excluded)
# So Final Range = 1 to 3
# Final Output = [25, "Python", True]

# --------------------------------------------------

# Example 3:-
# print(my_list[2:5])

# Explanation:
# Starting Point = 2
# Ending Point = 5 (Excluded)
# So Final Range = 2 to 4
# Final Output = ["Python", True, 85.5]

# --------------------------------------------------

# Example 4:-
# print(my_list[0:2])

# Explanation:
# Starting Point = 0
# Ending Point = 2 (Excluded)
# So Final Range = 0 to 1
# Final Output = ["Amit", 25]

# --------------------------------------------------

# Example 5:-
# print(my_list[3:6])

# Explanation:
# Starting Point = 3
# Ending Point = 6 (Excluded)
# So Final Range = 3 to 5
# Final Output = [True, 85.5, "Delhi"]

# --------------------------------------------------

# Example 6:-
# print(my_list[1:5])

# Explanation:
# Starting Point = 1
# Ending Point = 5 (Excluded)
# So Final Range = 1 to 4
# Final Output = [25, "Python", True, 85.5]

# --------------------------------------------------

# Example 7:-
# print(my_list[0:4])

# Explanation:
# Starting Point = 0
# Ending Point = 4 (Excluded)
# So Final Range = 0 to 3
# Final Output = ["Amit", 25, "Python", True]

# --------------------------------------------------

# Example 8:-
# print(my_list[2:4])

# Explanation:
# Starting Point = 2
# Ending Point = 4 (Excluded)
# So Final Range = 2 to 3
# Final Output = ["Python", True]

# --------------------------------------------------

# Example 9:-
#print(my_list[3:])

# Explanation:
# Starting Point = 3
# Ending Point = Not Given
# So Final Range = 3 to 5
# Final Output = [True, 85.5, "Delhi"]

# --------------------------------------------------

# Example 10:-
# print(my_list[:3])

# Explanation:
# Starting Point = Not Given (Default 0)
# Ending Point = 3 (Excluded)
# So Final Range = 0 to 2
# Final Output = ["Amit", 25, "Python"]


# ==================================================
# 2. NEGATIVE INDEXING - LIST SLICING
# ==================================================

# Definition:

# Negative Indexing starts from -1 and moves from Right to Left.

# indexing:   -6      -5     -4     -3   -2      -1
# my_list = ["Rahul", 30, "Java", False, 95.5, "Mumbai"]


# Example 1:-
# print(my_list[-6:-3])

# Explanation:
# Starting Point = -6
# Ending Point = -3 (Excluded)
# So Final Range = -6 to -4
# Final Output = ["Rahul", 30, "Java"]

# --------------------------------------------------

# Example 2:-
# print(my_list[-5:-2])

# Explanation:
# Starting Point = -5
# Ending Point = -2 (Excluded)
# So Final Range = -5 to -3
# Final Output = [30, "Java", False]

# --------------------------------------------------

# Example 3:-
# print(my_list[-4:-1])

# Explanation:
# Starting Point = -4
# Ending Point = -1 (Excluded)
# So Final Range = -4 to -2
# Final Output = ["Java", False, 95.5]

# --------------------------------------------------

# Example 4:-
# print(my_list[-6:-4])

# Explanation:
# Starting Point = -6
# Ending Point = -4 (Excluded)
# So Final Range = -6 to -5
# Final Output = ["Rahul", 30]

# --------------------------------------------------

# Example 5:-
# print(my_list[-3:])

# Explanation:
# Starting Point = -3
# Ending Point = Not Given
# So Final Range = -3 to -1
# Final Output = [False, 95.5, "Mumbai"]

# --------------------------------------------------

# Example 6:-
# print(my_list[-5:])

# Explanation:
# Starting Point = -5
# Ending Point = Not Given
# So Final Range = -5 to -1
# Final Output = [30, "Java", False, 95.5, "Mumbai"]

# --------------------------------------------------

# Example 7:-
# print(my_list[-6:-2])

# Explanation:
# Starting Point = -6
# Ending Point = -2 (Excluded)
# So Final Range = -6 to -3
# Final Output = ["Rahul", 30, "Java", False]

# --------------------------------------------------

# Example 8:-
# print(my_list[-4:-2])

# Explanation:
# Starting Point = -4
# Ending Point = -2 (Excluded)
# So Final Range = -4 to -3
# Final Output = ["Java", False]

# --------------------------------------------------

# Example 9:-
# print(my_list[-2:])

# Explanation:
# Starting Point = -2
# Ending Point = Not Given
# So Final Range = -2 to -1
# Final Output = [95.5, "Mumbai"]

# --------------------------------------------------

# Example 10:-
# print(my_list[:-3])

# Explanation:
# Starting Point = Not Given
# Ending Point = -3 (Excluded)
# So Final Range = -6 to -4
# Final Output = ["Rahul", 30, "Java"]

# ---------------------------------------------------

# =================================================
# 2. Three Parameter Slicing
# =================================================

# Definition : 

# By default the starting point will always be 0.
# By default the ending point will be always EXCLUDED.
# By default the gap will aiways be 1.

# syntax :-

# list name [start : end : gap]

# Parameters:

# Start = Starting Index (Included)
# End = Ending Index (Excluded)
# Gap = Number of steps to move forward or backward.
# Gap = (n - 1) where n = number of steps to move forward or backward.
# ==================================================
# 1. POSITIVE INDEXING - THREE PARAMETER SLICING
# ==================================================

# Definition:

# Positive Indexing starts from 0 and moves from Left to Right.

# indexing:    0     1      2     3     4      5        6      7
# my_list = ["Amit", 25, "Python", True, 85.5, "Delhi", "CSE", 100]

# Example 1:-
# print(my_list[0:8:2])

# Explanation:
# Starting Point = 0
# Ending Point = 8 (Excluded)
# Gap Size = (2 - 1) = 1
# So Final Range = 0, 2, 4, 6
# Final Output = ["Amit", "Python", 85.5, "CSE"]

# --------------------------------------------------

# Example 2:-
# print(my_list[1:8:2])

# Explanation:
# Starting Point = 1
# Ending Point = 8 (Excluded)
# Gap Size = (2 - 1) = 1
# So Final Range = 1, 3, 5, 7
# Final Output = [25, True, "Delhi", 100]

# --------------------------------------------------

# Example 3:-
# print(my_list[0:6:3])

# Explanation:
# Starting Point = 0
# Ending Point = 6 (Excluded)
# Gap Size = (3 - 1) = 2
# So Final Range = 0, 3
# Final Output = ["Amit", True]

# --------------------------------------------------

# Example 4:-
# print(my_list[1:7:3])

# Explanation:
# Starting Point = 1
# Ending Point = 7 (Excluded)
# Gap Size = (3 - 1) = 2
# So Final Range = 1, 4
# Final Output = [25, 85.5]

# --------------------------------------------------

# Example 5:-
# print(my_list[2:8:2])

# Explanation:
# Starting Point = 2
# Ending Point = 8 (Excluded)
# Gap Size = (2 - 1) = 1
# So Final Range = 2, 4, 6
# Final Output = ["Python", 85.5, "CSE"]

# --------------------------------------------------

# Example 6:-
# print(my_list[0:5:1])

# Explanation:
# Starting Point = 0
# Ending Point = 5 (Excluded)
# Gap Size = (1 - 1) = 0 
# So Final Range = 0, 1, 2, 3, 4
# Final Output = ["Amit", 25, "Python", True, 85.5]

# --------------------------------------------------

# Example 7:-
# print(my_list[2:7:2])

# Explanation:
# Starting Point = 2
# Ending Point = 7 (Excluded)
# Gap Size = (2 - 1) = 1
# So Final Range = 2, 4, 6
# Final Output = ["Python", 85.5, "CSE"]

# --------------------------------------------------

# Example 8:-
# print(my_list[3:8:2])

# Explanation:
# Starting Point = 3
# Ending Point = 8 (Excluded)
# Gap Size = (2 - 1) = 1
# So Final Range = 3, 5, 7
# Final Output = [True, "Delhi", 100]

# --------------------------------------------------

# Example 9:-
# print(my_list[::2])

# Explanation:
# Starting Point = Not Given (Default 0)
# Ending Point = Not Given (Default End)
# Gap Size = (2 - 1) = 1
# So Final Range = 0, 2, 4, 6
# Final Output = ["Amit", "Python", 85.5, "CSE"]

# --------------------------------------------------

# Example 10:-
# print(my_list[1::2])

# Explanation:
# Starting Point = 1
# Ending Point = Not Given (Default End)
# Gap Size = (2 - 1) = 1
# So Final Range = 1, 3, 5, 7
# Final Output = [25, True, "Delhi", 100]


# ==================================================
# 2. NEGATIVE INDEXING - THREE PARAMETER SLICING
# ==================================================

# Definition:
# Negative Indexing starts from -1 and moves from Right to Left.
# Negative gap Size (-1) moves the list in reverse direction.

# indexing:    -8     -7    -6      -5     -4     -3        -2      -1
# my_list = ["Rahul", 30, "Java", False, 95.5, "Mumbai", "Python", 200]


# Example 1:-
# print(my_list[-1:-9:1])

# Explanation:
# Starting Point = -1
# Ending Point = -9 (Excluded)
# Gap Size = (1 - 1) = 0
# So Final Range = -1, -2, -3, -4, -5, -6, -7, -8
# Final Output = [200, "Python", "Mumbai", 95.5, False, "Java", 30, "Rahul"]

# --------------------------------------------------

# Example 2:-
# print(my_list[-2:-9:2])

# Explanation:
# Starting Point = -2
# Ending Point = -9 (Excluded)
# Gap Size = (2 - 1) = 1
# So Final Range = -2, -4, -6, -8
# Final Output = ["Python", 95.5, "Java", "Rahul"]

# --------------------------------------------------

# Example 3:-
# print(my_list[-1:-9:2])

# Explanation:
# Starting Point = -1
# Ending Point = -9 (Excluded)
# Step Size = (2 - 1) = 1
# So Final Range = -1, -3, -5, -7
# Final Output = [200, "Mumbai", False, 30]

# --------------------------------------------------

# Example 4:-
# print(my_list[-3:-9:1])

# Explanation:
# Starting Point = -3
# Ending Point = -9(Excluded)
# Gap Size = (1 - 1) = 0
# So Final Range = -3, -4, -5, -6, -7, -8
# Final Output = ["Mumbai", 95.5, False, "Java", 30, "Rahul"]

# --------------------------------------------------

# Example 5:-
# print(my_list[-4:-9:2])

# Explanation:
# Starting Point = -4
# Ending Point = -9 (Excluded)
# Gap Size = (2 - 1) = 1
# So Final Range = -4, -6, -8
# Final Output = [95.5, "Java", "Rahul"]

# --------------------------------------------------

# Example 6:-
# print(my_list[-5:-9:1])

# Explanation:
# Starting Point = -5
# Ending Point = -9 (Excluded)
# Gap Size = (1 - 1) = 0
# So Final Range = -5, -6, -7, -8
# Final Output = [False, "Java", 30, "Rahul"]

# --------------------------------------------------

# Example 7:-
# print(my_list[-1:-5:1])

# Explanation:
# Starting Point = -1
# Ending Point = -5 (Excluded)
# Step Size = (1 - 1) = 0
# So Final Range = -1, -2, -3, -4
# Final Output = [200, "Python", "Mumbai", 95.5]

# --------------------------------------------------

# Example 8:-
# print(my_list[-2:-6:1])

# Explanation:
# Starting Point = -2
# Ending Point = -6 (Excluded)
# Gap Size = (1 - 1) = 0
# So Final Range = -2, -3, -4, -5
# Final Output = ["Python", "Mumbai", 95.5, False]

# --------------------------------------------------

# Example 9:-
# print(my_list[-3:-7:2])

# Explanation:
# Starting Point = -3
# Ending Point = -7 (Excluded)
# Gap Size = (2 - 1) = 1
# So Final Range = -3, -5
# Final Output = ["Mumbai", False]

# --------------------------------------------------

# Example 10:-
# print(my_list[::1])

# Explanation:
# Starting Point = Not Given (Default Last Index)
# Ending Point = Not Given (Default Before First Index)
# Gap Size = (1 - 1) = 0
# So Final Range = -1 to -8
# Final Output = [200, "Python", "Mumbai", 95.5, False, "Java", 30, "Rahul"]

# ---------------------------------------------------