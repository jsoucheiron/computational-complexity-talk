from itertools import permutations


def is_permutation(string_1, string_2):
    for permutation in permutations(string_1):
        permutation = ''.join(permutation)
        if permutation == string_2:
            return True
    return False


if __name__ == '__main__':
    first_string = 'i am lord voldemort'
    second_string = 'tom marvolo riddle '
    if is_permutation(first_string, second_string):
        print("{} is a permutation of {}".format(
            first_string, second_string))
    else:
        print("{} is not a permutation of {}".format(
            first_string, second_string))
