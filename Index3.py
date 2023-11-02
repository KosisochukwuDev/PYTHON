mylist = [1,4,6,7,8,9,2,5,2,3]
mylist.append(5)
print(mylist)
mylist2 = [0,1,2]
mylist.append(mylist2)
print (mylist)
print(mylist + mylist2)

mylist_ = [1,4,6,7,8,9,2,5,2,3]
mylist_.clear()
print(mylist_)

#copy is used to copy the elements of a variable into another variable.
thislist = [1,3,5,7,9,2,4,6,9]
y=thislist.copy()
print(y)

#count is used to count the number of elements with that value.
list = [7,8,9,5,3,4,6,7,8]
print(list.count(8))

#extend is used to add lists to each other.
list2 = [2,3,4,5,6,7,8,9]
list22 = [2,3,5]
list2.extend(list22)
print('Extended List')# you can give a title so you'll know which line of code it is.
print(list2)

#index will give you the index value of that particular index.
thoselists = [4,5,6,7,8,9,2,3]
print(thoselists.index(5))
print(thoselists.index(9))

#for insert you put the index number and the number you want to replace that value with
reallists = [1,2,3,4,5,6,7,5]
reallists.insert(0,90)
print(reallists)

#pop is used to remove an element using the index number
list4 = [6,7,8,9,0,3,4,5,1,2]
list4.pop(0)
print (list4)
list4.pop(3)
print(list4)

#remove is used to remove a particular value.
list5 = [0,1,2,3,4,5,6,7,8]
list5.remove(8)
print(list5)

list6 = [2,4,6,8,0,1,3,5,7,9]
list6.reverse
print(list6)

#sort is used to arrange the values in order.
list7 = [4,5,6,7,8,9,10,2,3]
list7.sort()
print(list7)
