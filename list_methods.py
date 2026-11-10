# ===============================
#   LIST METHODS
# ===============================

# Common list methods in Python include: 

# 1. append(): Adds an element to the end of the list.
# 2. extend(): It is used to add multiple elements at the end of list.
# 3. insert(): It is used to add an element at specified index.
# 4. remove(): Removes a specific element from a list.
# 5. pop(): By default it removes the last index element.
# 6. clear(): Removes all elements from the list.           
# 7. index(): it returns the first occurrence of any element.
# 8. count(): The count( ) method count how many times an element appears in a list.
# 9. sort(): by default it arranges elements in ascending order. 
# sort(reverse = True) => it arranges elements in descending order.
# 10. reverse(): Reverse the order of element in a list.
# 11. copy(): The copy( ) method create a copy of a list

# ==========================================
# 1. APPEND() METHOD
# It adds a single element at the end of a list.
# ==========================================

# # Example 1
# my_list = [11, 22, 33]
# print("Example 1 Before:", my_list)
# my_list.append(44)
# print("Example 1 After:", my_list)  # [11, 22, 33, 44]

# # Example 2
# my_list = [10, 20, 30]
# print("Example 2 Before:", my_list)
# my_list.append(40)
# print("Example 2 After:", my_list)  # [10, 20, 30, 40]

# # Example 3
# my_list = ["Apple", "Banana"]
# print("Example 3 Before:", my_list)
# my_list.append("Mango")
# print("Example 3 After:", my_list)  # ['Apple', 'Banana', 'Mango']

# # Example 4
# my_list = [1, 2, 3]
# print("Example 4 Before:", my_list)
# my_list.append(100)
# print("Example 4 After:", my_list)  # [1, 2, 3, 100]

# # Example 5
# my_list = [5, 10, 15]
# print("Example 5 Before:", my_list)
# my_list.append(20)
# print("Example 5 After:", my_list)  # [5, 10, 15, 20]

# # Example 6
# my_list = ["Python", "Java"]
# print("Example 6 Before:", my_list)
# my_list.append("C++")
# print("Example 6 After:", my_list)  # ['Python', 'Java', 'C++']

# # Example 7
# my_list = [2, 4, 6]
# print("Example 7 Before:", my_list)
# my_list.append(8)
# print("Example 7 After:", my_list)  # [2, 4, 6, 8]

# # Example 8
# my_list = [100, 200]
# print("Example 8 Before:", my_list)
# my_list.append(300)
# print("Example 8 After:", my_list)  # [100, 200, 300]

# # Example 9
# my_list = ["Red", "Blue"]
# print("Example 9 Before:", my_list)
# my_list.append("Green")
# print("Example 9 After:", my_list)  # ['Red', 'Blue', 'Green']

# # Example 10
# my_list = [50, 60, 70]
# print("Example 10 Before:", my_list)
# my_list.append(80)
# print("Example 10 After:", my_list)  # [50, 60, 70, 80]
# _________________________________________________________________________________________________
# 
# ==========================================
# 2. EXTEND() METHOD
# It adds multiple elements at the end of a list.
# ==========================================

# # Example 1
# my_list = [11, 22]
# print("Example 1 Before:", my_list)
# my_list.extend([33, 44])
# print("Example 1 After:", my_list)  # [11, 22, 33, 44]

# # Example 2
# my_list = [1, 2, 3]
# print("Example 2 Before:", my_list)
# my_list.extend([4, 5, 6])
# print("Example 2 After:", my_list)  # [1, 2, 3, 4, 5, 6]

# # Example 3
# my_list = ["Apple"]
# print("Example 3 Before:", my_list)
# my_list.extend(["Mango", "Banana"])
# print("Example 3 After:", my_list)

# # Example 4
# my_list = [10, 20]
# print("Example 4 Before:", my_list)
# my_list.extend([30, 40, 50])
# print("Example 4 After:", my_list)

# # Example 5
# my_list = ["Python", "Java"]
# print("Example 5 Before:", my_list)
# my_list.extend(["C", "C++"])
# print("Example 5 After:", my_list)

# # Example 6
# my_list = [100]
# print("Example 6 Before:", my_list)
# my_list.extend([200, 300])
# print("Example 6 After:", my_list)

# # Example 7
# my_list = [2, 4]
# print("Example 7 Before:", my_list)
# my_list.extend([6, 8, 10])
# print("Example 7 After:", my_list)

# # Example 8
# my_list = ["Red", "Blue"]
# print("Example 8 Before:", my_list)
# my_list.extend(["Green", "Yellow"])
# print("Example 8 After:", my_list)

# # Example 9
# my_list = [5, 15, 25]
# print("Example 9 Before:", my_list)
# my_list.extend([35, 45])
# print("Example 9 After:", my_list)

# # Example 10
# my_list = ["Monday"]
# print("Example 10 Before:", my_list)
# my_list.extend(["Tuesday", "Wednesday"])
# print("Example 10 After:", my_list)
# __________________________________________________________________________________________________
#
# ==========================================
# 3. INSERT() METHOD
# It adds an element at a specified index.
# ==========================================

# # Example 1
# my_list = [11, 22, 33, 44]
# print("Example 1 Before:", my_list)
# my_list.insert(2, 99)
# print("Example 1 After:", my_list)  # [11, 22, 99, 33, 44]

# # Example 2
# my_list = [10, 20, 30]
# print("Example 2 Before:", my_list)
# my_list.insert(0, 5)
# print("Example 2 After:", my_list)

# # Example 3
# my_list = ["Apple", "Mango"]
# print("Example 3 Before:", my_list)
# my_list.insert(1, "Banana")
# print("Example 3 After:", my_list)

# # Example 4
# my_list = [1, 2, 4, 5]
# print("Example 4 Before:", my_list)
# my_list.insert(2, 3)
# print("Example 4 After:", my_list)

# # Example 5
# my_list = [100, 200, 400]
# print("Example 5 Before:", my_list)
# my_list.insert(2, 300)
# print("Example 5 After:", my_list)

# # Example 6
# my_list = ["Python", "C++"]
# print("Example 6 Before:", my_list)
# my_list.insert(1, "Java")
# print("Example 6 After:", my_list)

# # Example 7
# my_list = [2, 4, 8]
# print("Example 7 Before:", my_list)
# my_list.insert(2, 6)
# print("Example 7 After:", my_list)

# # Example 8
# my_list = ["Red", "Green"]
# print("Example 8 Before:", my_list)
# my_list.insert(1, "Blue")
# print("Example 8 After:", my_list)

# # Example 9
# my_list = [50, 60, 80]
# print("Example 9 Before:", my_list)
# my_list.insert(2, 70)
# print("Example 9 After:", my_list)

# # Example 10
# my_list = ["Monday", "Wednesday"]
# print("Example 10 Before:", my_list)
# my_list.insert(1, "Tuesday")
# print("Example 10 After:", my_list)
# __________________________________________________________________________________________________
#
# ==========================================
# 4. REMOVE() METHOD
# It removes the first occurrence of a value.
# ==========================================

# # Example 1
# my_list = [11, 22, 33, 44]
# print("Example 1 Before:", my_list)
# my_list.remove(33)
# print("Example 1 After:", my_list)

# # Example 2
# my_list = [10, 20, 30, 40]
# print("Example 2 Before:", my_list)
# my_list.remove(10)
# print("Example 2 After:", my_list)

# # Example 3
# my_list = ["Apple", "Mango", "Banana"]
# print("Example 3 Before:", my_list)
# my_list.remove("Mango")
# print("Example 3 After:", my_list)

# # Example 4
# my_list = [1, 2, 3, 4, 5]
# print("Example 4 Before:", my_list)
# my_list.remove(5)
# print("Example 4 After:", my_list)

# # Example 5
# my_list = [100, 200, 300]
# print("Example 5 Before:", my_list)
# my_list.remove(200)
# print("Example 5 After:", my_list)

# # Example 6
# my_list = ["Python", "Java", "C++"]
# print("Example 6 Before:", my_list)
# my_list.remove("Java")
# print("Example 6 After:", my_list)

# # Example 7
# my_list = [2, 4, 6, 8]
# print("Example 7 Before:", my_list)
# my_list.remove(6)
# print("Example 7 After:", my_list)

# # Example 8
# my_list = ["Red", "Blue", "Green"]
# print("Example 8 Before:", my_list)
# my_list.remove("Blue")
# print("Example 8 After:", my_list)

# # Example 9
# my_list = [50, 60, 70, 80]
# print("Example 9 Before:", my_list)
# my_list.remove(70)
# print("Example 9 After:", my_list)

# # Example 10
# my_list = [10, 20, 10, 30]
# print("Example 10 Before:", my_list)
# my_list.remove(10)
# print("Example 10 After:", my_list)  # Removes first 10 only
# __________________________________________________________________________________________________
#
# ==========================================
# 5. POP() METHOD
# It removes and returns an element by index.
# Default: removes the last element.
# ==========================================

# # Example 1
# my_list = [11, 22, 33, 44]
# print("Example 1 Before:", my_list)
# my_list.pop()
# print("Example 1 After:", my_list)

# # Example 2
# my_list = [10, 20, 30, 40]
# print("Example 2 Before:", my_list)
# my_list.pop(0)
# print("Example 2 After:", my_list)

# # Example 3
# my_list = [1, 2, 3, 4, 5]
# print("Example 3 Before:", my_list)
# my_list.pop(2)
# print("Example 3 After:", my_list)

# # Example 4
# my_list = ["Apple", "Mango", "Banana"]
# print("Example 4 Before:", my_list)
# my_list.pop()
# print("Example 4 After:", my_list)

# # Example 5
# my_list = [100, 200, 300, 400]
# print("Example 5 Before:", my_list)
# my_list.pop(1)
# print("Example 5 After:", my_list)

# # Example 6
# my_list = ["Python", "Java", "C++"]
# print("Example 6 Before:", my_list)
# my_list.pop(0)
# print("Example 6 After:", my_list)

# # Example 7
# my_list = [2, 4, 6, 8]
# print("Example 7 Before:", my_list)
# my_list.pop(2)
# print("Example 7 After:", my_list)

# # Example 8
# my_list = ["Red", "Blue", "Green"]
# print("Example 8 Before:", my_list)
# my_list.pop(1)
# print("Example 8 After:", my_list)

# # Example 9
# my_list = [50, 60, 70, 80]
# print("Example 9 Before:", my_list)
# my_list.pop()
# print("Example 9 After:", my_list)

# # Example 10
# my_list = [10, 20, 30, 40, 50]
# print("Example 10 Before:", my_list)
# my_list.pop(3)
# print("Example 10 After:", my_list)
#__________________________________________________________________________________________________
#
# ==========================================
# 6. REVERSE() METHOD
# It reverses the order of elements.
# ==========================================

# # Example 1
# my_list = [11, 22, 33, 44]
# print("Example 1 Before:", my_list)
# my_list.reverse()
# print("Example 1 After:", my_list)

# # Example 2
# my_list = [1, 2, 3, 4, 5]
# print("Example 2 Before:", my_list)
# my_list.reverse()
# print("Example 2 After:", my_list)

# # Example 3
# my_list = ["Apple", "Mango", "Banana"]
# print("Example 3 Before:", my_list)
# my_list.reverse()
# print("Example 3 After:", my_list)

# # Example 4
# my_list = [10, 20, 30]
# print("Example 4 Before:", my_list)
# my_list.reverse()
# print("Example 4 After:", my_list)

# # Example 5
# my_list = [100, 200, 300, 400]
# print("Example 5 Before:", my_list)
# my_list.reverse()
# print("Example 5 After:", my_list)

# # Example 6
# my_list = ["Python", "Java", "C++"]
# print("Example 6 Before:", my_list)
# my_list.reverse()
# print("Example 6 After:", my_list)

# # Example 7
# my_list = [2, 4, 6, 8, 10]
# print("Example 7 Before:", my_list)
# my_list.reverse()
# print("Example 7 After:", my_list)

# # Example 8
# my_list = ["Red", "Blue", "Green"]
# print("Example 8 Before:", my_list)
# my_list.reverse()
# print("Example 8 After:", my_list)

# # Example 9
# my_list = [50, 60, 70]
# print("Example 9 Before:", my_list)
# my_list.reverse()
# print("Example 9 After:", my_list)

# # Example 10
# my_list = [5, 15, 25, 35]
# print("Example 10 Before:", my_list)
# my_list.reverse()
# print("Example 10 After:", my_list)
#___________________________________________________________________________________________________
#
# ==========================================
# 7. CLEAR() METHOD
# It removes all elements from a list.
# ==========================================

# # Example 1
# my_list = [11, 22, 33]
# print("Example 1 Before:", my_list)
# my_list.clear()
# print("Example 1 After:", my_list)

# # Example 2
# my_list = [1, 2, 3, 4]
# print("Example 2 Before:", my_list)
# my_list.clear()
# print("Example 2 After:", my_list)

# # Example 3
# my_list = ["Apple", "Mango"]
# print("Example 3 Before:", my_list)
# my_list.clear()
# print("Example 3 After:", my_list)

# # Example 4
# my_list = [10, 20, 30]
# print("Example 4 Before:", my_list)
# my_list.clear()
# print("Example 4 After:", my_list)

# # Example 5
# my_list = [100, 200, 300]
# print("Example 5 Before:", my_list)
# my_list.clear()
# print("Example 5 After:", my_list)

# # Example 6
# my_list = ["Python", "Java"]
# print("Example 6 Before:", my_list)
# my_list.clear()
# print("Example 6 After:", my_list)

# # Example 7
# my_list = [2, 4, 6, 8]
# print("Example 7 Before:", my_list)
# my_list.clear()
# print("Example 7 After:", my_list)

# # Example 8
# my_list = ["Red", "Blue"]
# print("Example 8 Before:", my_list)
# my_list.clear()
# print("Example 8 After:", my_list)

# # Example 9
# my_list = [50, 60, 70]
# print("Example 9 Before:", my_list)
# my_list.clear()
# print("Example 9 After:", my_list)

# # Example 10
# my_list = [5, 10, 15, 20]
# print("Example 10 Before:", my_list)
# my_list.clear()
# print("Example 10 After:", my_list)
#___________________________________________________________________________________________________
#
# ==========================================
# 8. SORT() METHOD
# Default: Ascending order.
# reverse=True: Descending order.
# ==========================================

# # Example 1 - Ascending
# my_list = [55, 44, 33, 22, 11]
# print("Example 1 Before:", my_list)
# my_list.sort()
# print("Example 1 After:", my_list)

# # Example 2 - Descending
# my_list = [10, 50, 20, 40, 30]
# print("Example 2 Before:", my_list)
# my_list.sort(reverse=True)
# print("Example 2 After:", my_list)

# # Example 3
# my_list = [9, 3, 7, 1, 5]
# print("Example 3 Before:", my_list)
# my_list.sort()
# print("Example 3 After:", my_list)

# # Example 4
# my_list = [12, 45, 23, 67, 10]
# print("Example 4 Before:", my_list)
# my_list.sort(reverse=True)
# print("Example 4 After:", my_list)

# # Example 5
# my_list = ["Orange", "Apple", "Mango"]
# print("Example 5 Before:", my_list)
# my_list.sort()
# print("Example 5 After:", my_list)

# # Example 6
# my_list = [80, 20, 60, 40]
# print("Example 6 Before:", my_list)
# my_list.sort()
# print("Example 6 After:", my_list)

# # Example 7
# my_list = [15, 5, 25, 10]
# print("Example 7 Before:", my_list)
# my_list.sort(reverse=True)
# print("Example 7 After:", my_list)

# # Example 8
# my_list = ["Zebra", "Apple", "Mango"]
# print("Example 8 Before:", my_list)
# my_list.sort()
# print("Example 8 After:", my_list)

# # Example 9
# my_list = [100, 10, 50, 20]
# print("Example 9 Before:", my_list)
# my_list.sort()
# print("Example 9 After:", my_list)

# # Example 10
# my_list = [90, 30, 70, 10, 50]
# print("Example 10 Before:", my_list)
# my_list.sort(reverse=True)
# print("Example 10 After:", my_list)
#___________________________________________________________________________________________________
#
# ==========================================
# 9. INDEX() METHOD
# It returns the index of the first occurrence.
# ==========================================

# # Example 1
# my_list = [11, 22, 33, 44]
# print("Example 1:", my_list.index(33))  # 2

# # Example 2
# my_list = [10, 20, 30, 40]
# print("Example 2:", my_list.index(10))  # 0

# # Example 3
# my_list = ["Apple", "Mango", "Banana"]
# print("Example 3:", my_list.index("Mango"))  # 1

# # Example 4
# my_list = [1, 2, 3, 4, 5]
# print("Example 4:", my_list.index(5))  # 4

# # Example 5
# my_list = [100, 200, 300]
# print("Example 5:", my_list.index(200))  # 1

# # Example 6
# my_list = ["Python", "Java", "C++"]
# print("Example 6:", my_list.index("C++"))  # 2

# # Example 7
# my_list = [2, 4, 6, 8]
# print("Example 7:", my_list.index(6))  # 2

# # Example 8
# my_list = ["Red", "Blue", "Green"]
# print("Example 8:", my_list.index("Green"))  # 2

# # Example 9
# my_list = [50, 60, 70, 80]
# print("Example 9:", my_list.index(60))  # 1

# # Example 10
# my_list = [10, 20, 10, 30]
# print("Example 10:", my_list.index(10))  # 0
#____________________________________________________________________________________________________
#
# ==========================================
# 10. COUNT() METHOD
# It counts how many times an element appears.
# ==========================================

# # Example 1
# my_list = [11, 22, 33, 22, 44]
# print("Example 1:", my_list.count(22))  # 2

# # Example 2
# my_list = [10, 10, 20, 30]
# print("Example 2:", my_list.count(10))  # 2

# # Example 3
# my_list = ["Apple", "Mango", "Apple"]
# print("Example 3:", my_list.count("Apple"))  # 2

# # Example 4
# my_list = [1, 2, 3, 2, 2, 4]
# print("Example 4:", my_list.count(2))  # 3

# # Example 5
# my_list = [100, 200, 100, 300]
# print("Example 5:", my_list.count(100))  # 2

# # Example 6
# my_list = ["Python", "Java", "Python"]
# print("Example 6:", my_list.count("Python"))  # 2

# # Example 7
# my_list = [5, 5, 5, 10, 15]
# print("Example 7:", my_list.count(5))  # 3

# # Example 8
# my_list = ["Red", "Blue", "Red", "Green"]
# print("Example 8:", my_list.count("Red"))  # 2

# # Example 9
# my_list = [50, 60, 70, 60, 80]
# print("Example 9:", my_list.count(60))  # 2

# # Example 10
# my_list = [1, 1, 2, 3, 1, 4]
# print("Example 10:", my_list.count(1))  # 3
#_____________________________________________________________________________________________________
#
# ==========================================
# 11. COPY() METHOD
# It creates a shallow copy of a list.
# ==========================================

# # Example 1
# my_list = [11, 22, 33]
# print("Example 1 Before:", my_list)
# new_list = my_list.copy()
# print("Example 1 After:", new_list)

# # Example 2
# my_list = [10, 20, 30]
# new_list = my_list.copy()
# print("Example 2:", new_list)

# # Example 3
# my_list = ["Apple", "Mango"]
# new_list = my_list.copy()
# print("Example 3:", new_list)

# # Example 4
# my_list = [1, 2, 3, 4]
# new_list = my_list.copy()
# print("Example 4:", new_list)

# # Example 5
# my_list = [100, 200, 300]
# new_list = my_list.copy()
# print("Example 5:", new_list)

# # Example 6
# my_list = ["Python", "Java"]
# new_list = my_list.copy()
# print("Example 6:", new_list)

# # Example 7
# my_list = [2, 4, 6, 8]
# new_list = my_list.copy()
# print("Example 7:", new_list)

# # Example 8
# my_list = ["Red", "Blue", "Green"]
# new_list = my_list.copy()
# print("Example 8:", new_list)

# # Example 9
# my_list = [50, 60, 70]
# new_list = my_list.copy()
# print("Example 9:", new_list)

# # Example 10
# my_list = [5, 10, 15, 20]
# new_list = my_list.copy()
# print("Example 10:", new_list)
#______________________________________________________________________________________________________
