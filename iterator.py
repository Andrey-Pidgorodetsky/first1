def my_for_loop(iterable):
    iterator=iter(iterable)

    while True:
        try:
            print(iterator.__next__())
        except StopIteration:
            print('Iteration finished')
            break

my_for_loop("Hello world")