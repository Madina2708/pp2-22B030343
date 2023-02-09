nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("List of integers:")
print(nums)
print("\nEven numbers from the list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)

print("\nOdd numbers from the list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)