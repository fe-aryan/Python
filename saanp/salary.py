#Company will give bonus on following criteria

#Time spent in company      bonus
#More than 10 years          10%
#Between 6 and 10 years      8%
#Less than 5 years           5%

#Ask the salary and time spent from the user
#Print the net bonus amount accordingly

salary = int(input("Enter your current salary"))
year = int(input("Enter your year of service"))

if year > 10:
    print("Your net salary is -",salary+salary*1/10)
elif year >= 6 <= 10:
    print("Your net salary is -",salary+salary*8/100)
else:
    print("Your net salary is -",salary+salary*5/100)
