# SETS{}

# Sets are used to store multiple items in a single variable. It can have different data types


# Unordered
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Duplicates Not Allowed
# Sets cannot have two items with the same value.


#if object in set 

mySet = {"orange", "apple", "banana",4}
# mySet.add("mango")
# print(mySet)
# if "apple" in mySet:
#    print("True")
# else:
#  print("False")
# x=dict()
# for z in enumerate(range(2)):
#     x[z[0]]=z[1]
#     x[z[1]+8]=z[0]
# print(x)
# 
mySet1={1,2,3,4}
#addition of two sets
#mySet2=mySet.union(mySet1)

#finding the same element
#mySet2=mySet.intersection(mySet1)

#to remove the common element
mySet2=mySet.symmetric_difference(mySet1)
print (mySet2)