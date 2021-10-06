# def my_function(x):
#     return x
# print(my_function(4))


# def couner_up_to(x):
#     count=1
#     while count <=x:
#         yield count
#         count+=1
# for i in couner_up_to(10):
#     print(i)

# def crate_patterns():
#     max_patterns_number=100
#     patterns=('First pattern', 'Second pattern', 'Third pattern', 'Forth pattern')
#     i=0
#     result_list=[]
#     while len(result_list)<max_patterns_number:
#         if i>= len(patterns):
#             i=0
#         result_list.append(patterns[i])
#         i+=1
#     return result_list
#
# print(crate_patterns())
def get_current_pattern():
    patterns=('First pattern', 'Second pattern', 'Third pattern', 'Forth pattern')
    i=0
    while True:
        if i>=len(patterns):
            break
        yield patterns[i]
        i+=1

current_pattern=get_current_pattern()

for i in current_pattern:
    print(i)