tuple1 = (1,[6,7],2,3,4,5)
i = tuple1[1][0]
print(i)

# •	Sets is a non-homogenous but stores in single variable
# •	Representation= {}
# •	no Duplicate element 
# •	unchangeable
#   unordered
set={"cars","boat","bike"}
print(set)
#no Duplicate element 
set1={"cars","boat","bike","cars"}
print(set1)
print(len(set))
if "bike" in set:
    print("True")
else:
  print("False")