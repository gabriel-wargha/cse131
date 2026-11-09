from LAB09 import sort

def test_less_than_2_positions_sort_():
   assert(sort([1])) == [1]
   assert(sort([7])) == [7]

def test_boundary_conditions_sort():
   assert(sort([100000, 1, 50000])) == [1, 50000, 100000]
   assert(sort([1,5,5,2,3])) == [1, 2, 3, 5, 5]

def test_requirements_conditions_sort():
   assert(sort([1,4,9,11,13,8,3,2])) == [1,2,3,4,8,9,11,13]
   assert(sort([80,90,54,32,12,76])) == [12,32,54,76,80,90]
 
   
#Empty 
assert(sort([])) == []

# Just one sublist
assert(sort([7, 7])) == [7, 7]

# Small unsorted 
assert(sort([4, 2])) == [2, 4]

# Inverse Order 
assert(sort([9, 8, 7, 4])) == [4, 7, 8, 9]

#Duplicates 
assert(sort([3, 5, 3, 4, 5, 4])) == [3, 3, 4, 4, 5, 5]