#
# print(None)
# try:
#    print(len(22))
#    print("my_fun")
# except TypeError:
#    print("TypeError")
#
#
# number=input('Enter number  ')
# try:
#    print(int(number)/2)
# except:
#    print('You need ro enter a number')
# else:
#    print('Good')


# x=input('enter first number ')
# y=input('enter second number ')
# def oshibki(x, y):
#     try:
#         print(int(x)/int(y))
#     except ZeroDivisionError:
#         print('You cannot divide by zero')
#     except TypeError:
#         print('Its must be numbers')
#     except ValueError :
#         print('ValueError')
#     else:
#         print('ok')
#     finally:
#         print('Finally block')
# oshibki(x,y)

# print (None)
# try:
#     print(len(22))
#     print("my_fun")
# except TypeError:
#     print("TypeError")

while True:
        try:
            x = int(input('enter first number '))
            y = int(input('enter second number '))
            print(x/y)
        except ValueError as a:
            print("You must entering namers . ValueError")
            print(a)
        except ZeroDivisionError as a:
            print("ZeroDivisionError")
            print(a)
        else:
            print('fine')
            break
        finally:
            print('Its finally block')
print('code finished')

