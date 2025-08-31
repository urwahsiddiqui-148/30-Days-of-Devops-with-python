# bollean data type 
a = True
b = False
print(type(a))
print(type(b))


#list data type 
list1 = [1, 2, 3, 4,55,5]
list2 = ["apple", "banana", "coconet"]
print (list1, list2)
print (type(list1))
print (type(list2))
print (list1[0])
print (list2[1:3])
list1.append(6)
print (list1)

# dictionary data type
dict1 = {'name' : 'urwah shafiq', 'age': 23, 'living city': 'Multan', 'family sure name': 'Siddiqui'}
print (dict1['name'])
print (type(dict1))
print (dict1.keys())
print (dict1.values())
dict1 ['age'] = 25
print (dict1)

# dictionary is mutable guys 

# now set data type 
set =  {1,1,1,12,3,4,55,4,3,3,3,45,56,5,43,2,45,5,4,3,3,45}
print (set) 
print (type(set))
set.add(100)
print (set)
set.remove(3)
# set remves the duplicate item 
