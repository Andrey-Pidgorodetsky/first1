# def simple_function():
#     print('Simple function code')
#
# # simple_function()
def decorator_function(original_function):
    def wrap_function():
        print('Simple function code (old)')
        original_function()
        print('Oold code')
    return wrap_function
# decorated_function= decorator_function(simple_function)
# decorated_function()
@decorator_function
def simple_function():
    print('Simple function code')

simple_function()

