#Take user input (string)
#if the len of string is greater than 3 add 'ing' as a suffix in the original string
#else print the same string given by the user

a=str(input("Enter: "))
if len(a)>3:
    print(a+"ing")
else:
    print(a)