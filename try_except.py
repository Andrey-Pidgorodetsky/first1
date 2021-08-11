
#print(None)
#try:
#    print(len(22))
#    print("my_fun")
#except TypeError:
#    print("TypeError")


#number=input('Enter number  ')
#try:
#    print(int(number)/2)
#except:
#    print('You need ro enter a number')
#else:
#    print('Good')


def oshibki(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print('You cannot divide by zero')
    except TypeError:
        print('Its must be numbers')
    else:
        print('ok')
    finally:
        print('Finally block')

first=int(input("enter first number "))
last=int(input('enter last number'))
print(oshibki(first, last))

print (None)
try:
    print(len(22))
    print("my_fun")
except TypeError:
    print("TypeError")



