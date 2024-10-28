def find_max(numbers):
	if not numbers:
		raise ValueError("Matrix should not be empty")
	return max(numbers)

numbers_list = [10, 3, 7, 1, 2, 0, 7, 19]
print(find_max(numbers_list))