# def prodact(n, func):
#     result=1
#     for number in range(1,n):
#         result*=func(number)
#     return result
# def square(x):
#     return  x*x
#
# def cube(x):
#     return x*x*x
# def my_function(a,b,func):
#     result= func([a,b])
#     return result
#
# print(prodact(4,square))
# print(prodact(4,cube))
# print(my_function(5,2,sum))
from random import choice

def colorize(i):
    def get_color():
        colors=('red','green','blue')
        color=choice(colors)
        return color

    result =get_color()+ ' ' +i
    return result
print(colorize('apple'))