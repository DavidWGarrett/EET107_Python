# David Garrett
# EET-107-100 Chapter 12 Lab 2
# 4-28-2021

# Find a minimum value in a tuple using recursive loops

def main():

    # Three random tuples with a minimum value
    random_tuple_number1 = (66, 53, 77, 55, 4, 1, 7, 5, 45, 2)
    random_tuple_number2 = (3, 5, 7, 8, 2, 1)
    random_tupleaaa = (1, 2, 3, 5, 7, 8, 2)

    # Three print statements that calls the sum_rr function inside of it that prints the lowest value of tuple

    print('The minimum value in the tuple ' + str(random_tuple_number1) + ' is '
          + str(sum_rr(random_tuple_number1, random_tuple_number1[0])))

    print('The minimum value in the tuple ' + str(random_tuple_number2) + ' is '
          + str(sum_rr(random_tuple_number2, random_tuple_number2[0])))

    print('The minimum value in the tuple ' + str(random_tupleaaa) + ' is '
          + str(sum_rr(random_tupleaaa, random_tupleaaa[0])))


def sum_rr(nums, min_value):  # Tuple and first index of tuple gets passed to function
    if len(nums) == 1:  # if statement doesn't trigger till the tuple length is down to 1 after recursion
        return min_value  # returns minimum value of tuple

    else:
        if min_value > nums[1]:
            # if minimum value is bigger than second index value, new value gets initialized and passed
            min_value = nums[1]
        return sum_rr(nums[1:], min_value)  # functions calls itself, passes tuple without the first index value


main()