#A company decided to give bonus of 1000Rs to #employee if his/her service is more than 5 years
#Ask user their salary and year of service and print the net bonus amount

salary = int(input('Enter your salary'))
year = int(input('Enter your years of service'))
if year > 5:
    bonus = salary + 1000
    print(bonus)
else:
    print(salary)

