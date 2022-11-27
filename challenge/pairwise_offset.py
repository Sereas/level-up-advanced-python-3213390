def pairwise_offset(sequence, fillvalue='*', offset=0):
    total_length = len(sequence) + offset
    return_list = []
    for elem in range(total_length):
        if elem > len(sequence)-1:
            first_value = fillvalue
        else:
            first_value = sequence[elem]

        if elem < offset:
            second_value = fillvalue
        else:
            second_value = sequence[elem-offset]

        new_tuple = (first_value, second_value)
        return_list.append(new_tuple)
    return return_list

