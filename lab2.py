#---------------------------------------------------------------------
#                                                          Python Sets
#---------------------------------------------------------------------
# Python Sets

# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# *Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.

# Example
# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)




# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can add new items.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# Example
# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)




# Get the Length of a Set
# To determine how many items a set has, use the len() function.
# Example
# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))




# Set Items - Data Types
# Set items can be of any data type.
# Example
# String, int, and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}




# A set can contain different data types.
# Example
# A set with strings, integers, and boolean values:
set4 = {"abc", 34, True, 40, "male"}




# type()
# From Python's perspective, sets are defined as objects with the data type 'set'.
# Example
# What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))




# The set() Constructor
# It is also possible to use the set() constructor to make a set.
# Example
# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)




# Access Set Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

# Example 1: Loop through the set items
thisset = {"apple", "banana", "cherry"}
for item in thisset:
    print(item)

# Example 2: Check if an item exists in the set
thisset = {"apple", "banana", "cherry"}
if "banana" in thisset:
    print("Yes, 'banana' is in the fruits set")

# Example 3: Using `in` with a condition to print a message
thisset = {"apple", "banana", "cherry"}
if "grapes" not in thisset:
    print("No, 'banana' is not in the fruits set")
    
    
    

# Add Set Items
# To add one item to a set, use the `add()` method.
# To add multiple items to a set, use the `update()` method.

# Example 1: Add a single item to a set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

# Example 2: Add multiple items to a set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# Example 3: Add items from a list to a set
thisset = {"apple", "banana", "cherry"}
fruits = ["orange", "mango", "grapes"]
thisset.update(fruits)
print(thisset)




# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# ExampleGet your own Python Server
# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)




# Note: If the item to remove does not exist, remove() will raise an error.
# Example
# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)




# Note: If the item to remove does not exist, discard() will NOT raise an error.
# You can also use the pop() method to remove an item, but this method will remove a random item, 
# so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
# Example
# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)




# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
# Example
# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)



# Example
# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)




# Loop Items
# You can loop through the set items by using a for loop:
# ExampleGet your own Python Server
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)




# Join Sets
# There are several ways to join two or more sets in Python.

# The union() and update() methods joins all items from both sets.

# The intersection() method keeps ONLY the duplicates.

# The difference() method keeps the items from the first set that are not in the other set(s).

# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# Union
# The union() method returns a new set with all items from both sets.

# ExampleGet your own Python Server
# Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)




# You can use the | operator instead of the union() method, and you will get the same result.
# Example
# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)




# Join Multiple Sets
# All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas:
# Example
# Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)





# When using the | operator, separate the sets with more | operators:
# Example
# Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)




# Join a Set and a Tuple
# The union() method allows you to join a set with other data types, like lists or tuples.
# The result will be a set.
# Example
# Join a set with a tuple:
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)




# Note: The  | operator only allows you to join sets with sets, 
# and not with other data types like you can with the  union() method.
# Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
# Example
# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)




# Note: Both union() and update() will exclude any duplicate items.
# Intersection
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.
# Example
# Join set1 and set2, but keep only the duplicates:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)




# You can use the & operator instead of the intersection() method, and you will get the same result.
# Example
# Use & to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)




# Note: The & operator only allows you to join sets with sets, 
# and not with other data types like you can with the intersection() method.
# The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.
# Example
# Keep the items that exist in both set1, and set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)




# The values True and 1 are considered the same value. The same goes for False and 0.
# Example
# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)




# Difference
# The difference() method will return a new set that will contain only the items 
# from the first set that are not present in the other set.
# Example
# Keep all items from set1 that are not in set2:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)




# You can use the - operator instead of the difference() method, and you will get the same result.
# Example
# Use - to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)




# Note: The - operator only allows you to join sets with sets, 
# and not with other data types like you can with the difference() method.
# The difference_update() method will also keep the items from the first set that are not in the other set, 
# but it will change the original set instead of returning a new set.
# Example
# Use the difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)




# Symmetric Differences
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# Example
# Keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)




# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
# Example
# Use ^ to join two sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)




# Note: The ^ operator only allows you to join sets with sets, 
# and not with other data types like you can with the symmetric_difference() method.
# The symmetric_difference_update() method will also keep all but the duplicates, 
# but it will change the original set instead of returning a new set.
# Example
# Use the symmetric_difference_update() method to keep the items that are not present in both sets:
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)