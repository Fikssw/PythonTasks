def count_vowels():
	s = input("Enter sentence: ")
	vowels = "aeiouAEIOU"
	count = sum(1 for char in s if char in vowels)
	print(f"Sum of vowels: {count}")

count_vowels()