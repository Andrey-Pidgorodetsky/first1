# assert  2+2=3, '2+2 is 4'
# assert  2+2=4
#
# def divide(a,b):
#     assert b!=0 , 'b must be not zero'
#     return a/b
# print(divide(2,2))


# def divide2(a,b):
#     assert a>0 and b>0 , 'Only +'
#     return a+b
# print(divide2(2,2))


def get_access (password):
    password_list=[0000, 1111, 2222, 3333]
    assert int(password) in password_list , 'Password is invalid'
    print("Access done")

get_access(1111)