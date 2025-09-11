list = [5, 8, 2, 7, 1, 6, 3, 4]


def length(list):
    length = len(list)
    return length
print("The length of the list is: ", length(list))


def mean(list):
    mean = sum(list)/length(list)
    return mean
print("The mean of the list is: ", mean(list))


def range_of_list(list):
    range_of_list = max(list) - min(list)
    return range_of_list
print("The difference between the smallest and the largest value: ", range_of_list(list))



def add_values():