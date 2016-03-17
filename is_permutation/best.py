from collections import Counter


def is_permutation(string_1, string_2):
    if Counter(string_1) != Counter(string_2):
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
