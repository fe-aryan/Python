def isEven(i):
    return i%2==0

list1 = [3, 4, 10, 9, 18, 66, 13, 15]

evenNum = list(filter(isEven,list1))
print(evenNum)

EvenNum = list(filter(lambda i : i%2==0,list1))  #Above function in one line
print(EvenNum)

names = ["Nikhil", "Lucky", "Sourav", "Agastya", "Sunil"]
names.sort(key = lambda x:len(x))
print(names)

squareNum = list(map(lambda i : i ** 2,list1))
print(squareNum)

list5 = [10,20,30,40,50]
#Triple the values of this function
mulNum = list(map(lambda i : i*3,list5))
print(mulNum)