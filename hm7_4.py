def common_elements():
    my_list_3 = []
    my_list_5 = []
    for number in range(100):
        if number % 3 == 0:
            my_list_3.append(number)
        if number % 5 == 0:
            my_list_5.append(number)
    set_list_3 = set(my_list_3)
    set_list_5 = set(my_list_5)
    common_set = set_list_3.intersection(set_list_5)
    return common_set


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}, "Test failed"
print("OK")
