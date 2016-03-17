def is_permutation(string_1, string_2):
    longest_string = max([string_1, string_2], key=len)
    for current_char in longest_string:
        count_1 = string_1.count(current_char)
        count_2 = string_2.count(current_char)
        if count_1 != count_2:
            return False
    return True


if __name__ == '__main__':
    first_string = 'i am lord voldemort'
    second_string = 'tom marvolo riddle '
    if is_permutation(first_string, second_string):
        print("{} is a permutation of {}".format(
            first_string, second_string))
    else:
        print("{} is not a permutation of {}".format(
            first_string, second_string))
