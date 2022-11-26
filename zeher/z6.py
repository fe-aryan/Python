#Write a program to unpack the following tuple into four variable and print each variable
#packing & unpacking
tup=("A","B","C")
(one,*two,three)=tup  #8 is taking all the parameter and leaving one for one parameter
print(one)
print(two)
print(three)