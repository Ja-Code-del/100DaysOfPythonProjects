def get_the_max_of(my_list):
    max = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
    return max