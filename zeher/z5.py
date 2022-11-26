#tuples store multipleitems in a single variable
#ordered,unchangeable,  
my_tuple=("orange")
print(my_tuple)
my_tuple1=("orange",)
print(my_tuple1)
my_tuple2=("orange","apple","pineapple","grapes")
print(my_tuple2)
print(my_tuple2[1])
print(my_tuple2[-1])
print(my_tuple2[0:])
l=list(my_tuple2)
print(l)
l.append("BANANA")
t=tuple(l)
print(t)
tuple1=(1,2,3)
tuple2=(4,5,6)
tuple1+=tuple2
print(tuple1)

#Reverse the above tuple
print(tuple1[::-1])

name=("Aryan",)
print(name)
