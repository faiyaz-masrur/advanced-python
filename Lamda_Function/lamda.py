from functools import reduce


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared = list(map(lambda x: x ** 2, numbers))
print("Squared:", squared)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

sorted_desc = sorted(numbers, key=lambda x: x ** 2, reverse=True)
print("Sorted by square (desc):", sorted_desc)

sum_of_squares = reduce(lambda acc, x: acc + x ** 2, numbers, 0)
print("Sum of squares:", sum_of_squares)
