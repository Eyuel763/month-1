def sum_list(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    
    return sum

my_list = [1, 2, 3, 4, 5]
list_sum = sum_list(my_list)
print(f"Sum of the list: {list_sum}")