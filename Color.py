
def get_color(color_number):
    number_color_list=[1,2,3,4,5,6]
    if type(color_number) is not int:
        raise TypeError('Wrong type, type must be integer')

    if color_number not in number_color_list:
        raise ValueError('Color number must be in range  from 1-7')


    if color_number == 1:
        return 'red'
    if color_number == 2:
        return 'orange'
    if color_number == 3:
        return 'yelow'
    if color_number == 4:
        return 'green'
    if color_number == 5:
        return 'blue'

    if color_number == 6:
        return 'indigo'
    if color_number == 7:
        return 'violet'

color=get_color(6)
print(color)
