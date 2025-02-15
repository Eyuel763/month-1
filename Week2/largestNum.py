def largest_num(numbers):
    largest = numbers[0]
    for i in numbers:
        if largest < i:
            largest = i

    return largest

my_list = [10, 5, 20, 8, 15, 25]
largest_num = largest_num(my_list)
print(f"The largest number in the list is: {largest_num}")