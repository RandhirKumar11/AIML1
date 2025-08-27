nums={5,2,8,9,1,7}
print("Set: ",nums)

#adding elements in set
nums.add(10)
print("After add:",nums)

#updating with multiple elements
nums.update([20,30,40])
print("After updating:",nums)

#Removing elements
nums.remove(20)
nums.discard(100)
print("After remove and discard:",nums)

# pop()
popped=nums.pop()
print("Popped element:", popped)
print("After Popped:",nums)

#popped=nums.pop()
#print("Popped element:", popped)
#print("After Popped:",nums)

# clear the set
temp={1,2,3}
temp.clear()
print("After clear:",temp)

# set operation
a={1,2,3,4,5,6,7,9,10,11}
b={9,10,11,12,13,1,2,3,4,14,15}

# union
print("Union:",a.union(b))
print("Union:",b.union(a))

# intersection
print("Intersection:",a.intersection(b))

# difference
print("Difference (a-b):",a.difference(b))
print("Difference (b-a):", b.difference(a))

# symmetric difference (Elements not common in both)
print("Symmetric difference:",a.symmetric_difference(b))

# Relationship relation
x={1,2}
y={1,2,3,4}

# subset
print("X is subset of Y:", x.issubset(y))
print("Y is subset of X:", y.issubset(x))
print("X is subset of X:", x.issubset(x))

# disjoint set
z={10,20}
print("Y and Z are  disjoint:", y.isdisjoint(z))
print("Y and X are  disjoint:", y.isdisjoint(x))

# super set
print("Y is the superset of X:",y.issuperset(x))

# sorting of a set
nums={9,3,6,1,7}

# convert to list and sort in ascending order
sorted_nums=sorted(nums)
print("Ascending sort:",sorted_nums)

#sorted_nums_desc=sorted_nums,reverse=True
print("Descending sort:", sorted(nums,reverse=True))