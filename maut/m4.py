dict1 = {"one":1, "two":2, "three":3}
dict2 = {"four":4, "five":5, "six":6}

#Merge two dictionaries in one

dict3 = {**dict1, **dict2}
print(dict3)
print(dict1|dict2)