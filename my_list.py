#QUESTIONS(week 2)
#Create an empty list called my_list.
#Append the following elements to my_list: 10, 20, 30, 40.
#Insert the value 15 at the second position in the list.
#Extend my_list with another list: [50, 60, 70].
#Remove the last element from my_list.
#Sort my_list in ascending order.
#Find and print the index of the value 30 in my_list

#SOLUTIONS
#Creating an empty list
my_list = [];

#Append the following elements to my_list: 10, 20, 30, 40.* using concatenation, 
#we can also use .extend, .append, +=
my_list  = my_list + [10, 20, 30, 40];
print(my_list);

#Insert the value 15 at the second position in the list.
#This can be done using slice method. It can also be done using .insert method
#e.g my_list.insert(1,15)
my_list = my_list[:1] + [15] + my_list[1:]
print(my_list);

#Extend my_list with another list: [50, 60, 70].This is done usinf .extend
my_list.extend([50, 60, 70])
print(my_list);

#Remove the last element from my_list.this is done using .pop
my_list.pop();
print(my_list);

#Sort my_list in ascending order.
my_list.sort()
print(my_list);

#Find and print the index of the value 30 in my_list
my_list.index(30)
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30);
