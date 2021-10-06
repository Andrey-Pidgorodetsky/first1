import time

list_start_time=time.time()
print(sum([number for number in range(10000000)]))
list_processing_time=time.time()-list_start_time

generator_start_time=time.time()
print(sum(number for number in range(10000000)))
generator_processing_time=time.time()-list_start_time

print(f'List processing {list_processing_time}')
print(f'Generator processing {generator_processing_time}')