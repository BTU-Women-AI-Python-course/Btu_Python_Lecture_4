# append
list1 = [1,2,3,4,5,6,7,8,9]
list1.append(10)
print(list1)

# clear
list1 = [1,2,3,4,5,6,7,8,9]
list1.clear()
print(list1)

# copy
list1 = [1,2,3,4,5]

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, list1.copy()]
list2[-1].append(10)

print(list1)
print(list2)

# count
list1 = [1, 2, 3, 4, 5, 5]

print(list1.count(5))

# extend
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
list1.extend(list2)
print(list1)

# index
list1 = [2,1,2,3,4,5,6,7,8,9]
print(list1.index(2))

# insert
list1 = [2,1,2,3,4,5,6,7,8,9]
list1.insert(0,0)
print(list1)

# pop
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.pop(1)
print(list1)

# remove
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
list1.remove(1)
print(list1)

# reverse
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.reverse()
print(list1)

# sort
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.sort()
print(list1)
