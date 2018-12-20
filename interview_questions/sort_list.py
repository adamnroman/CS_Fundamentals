
def find_smallest(list_to_sort):
    min_value = float('inf')
    for num in list_to_sort:
        if num < min_value:
            min_value = num
    return min_value

def find_second_smallest(list_to_sort):
    min_value = float('inf')
    min2_value = float('inf')
    for num in list_to_sort:
        if num < min_value:
            min2_value = min_value
            min_value = num
        elif num < min2_value:
            min2_value = num
    return min2_value

def find_n_smallest(list_to_sort,n):
    indy = 0
    for x in range(len(list_to_sort)): 
        if list_to_sort[x] < list_to_sort[indy]:
            #swap the elements
            temp = list_to_sort[indy]
            list_to_sort[indy] = list_to_sort[x]
            list_to_sort[x] = temp


