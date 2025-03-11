# list_1 = [9,'$',4,3,'.',5]


def custom_sort(list1:list):
    # Step 1: Extract numbers and sort them
    numbers = sorted([item for item in list_1 if isinstance(item, int)])

    # Step 2: Reinsert special characters at their original positions
    result = []
    num_index = 0

    for item in list_1:
        if isinstance(item, int):
            result.append(numbers[num_index])
            num_index += 1
        else:
            result.append(item)
    return result
list_1 = [9,'$',4,3,'.',5]
print(custom_sort(list_1)) ## output= [3,'$',4, 5,'.',9]