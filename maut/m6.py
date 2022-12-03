def div(a,b):

    def good_div(func):
        def inner_div(a,b):
            if a < b:
                a,b=b,a
            return func(a,b)

        return inner_div()
    div = good_div(div)
div(2,4)    

#OOPS is vvvIMP

from functools import reduce

list1 = [1,2,3,4,5,6]
sum = reduce(lambda i,j: i+j, list1)
print(sum)