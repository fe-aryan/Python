#Accept a number from the user
#Calculate and print the sum of all numbers
#From 1 to input number
#Using for loop

userInput = int(input("Enter a number "))
sum = 0
for i in range(1, userInput+1):
    sum = sum + 1
    print(i)

