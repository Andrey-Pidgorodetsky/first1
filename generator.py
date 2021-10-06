# def my_function(x):
#     return x
# print(my_function(4))


def couner_up_to(x):
    count=1
    while count <=x:
        yield count
        count+=2




for i in couner_up_to(10):
    print(i)
