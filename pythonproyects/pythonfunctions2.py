# Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a, b, c):
    if (a > b and a > c):
        return a
    elif (b > c):
        return b
    else:
        return c


print(max_num(4, 6, 3))

# Write a Python function called mult_list() to multiply all the numbers in a list.


def mult_list(list):
    multiplier = 1
    for i in list:
        multiplier = multiplier * i

    return multiplier


list_of_numbers = {1, 2, 3, 4}
print(mult_list(list_of_numbers))


# Write a Python function called rev_string() to reverse a string.
def rev_string(normal_string):
    reversed_string = normal_string[::-1]
    print(reversed_string)


rev_string("hello")


# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range(inclusive) as arguments.
# Examples: num_within(3, 2, 4) returns True, num_within(3, 1, 3) returns True, num_within(10, 2, 5) returns False.
def num_within(x, y, number):
    if (x > y):
        if (x >= number and y <= number):
            print("Number is in range")
        else:
            print("Number is not in range")
    else:
        if (x <= number and y >= number):
            print("Number is in range")
        else:
            print("Number is not in range")


num_within(1, 4, 3)


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note: Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
# Each number is the two numbers above it added together.

def pascal(n):
    row1 = [1]
    for i in row1:
        if (i-1 == 0 or i+1 == 2):
            print(row1)
            row1.append(i+1)
            print(row1)


pascal(1)
