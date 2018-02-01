
# Easiest solution
def check_array(var1, var2):
	if sorted(var1) == sorted(var2):
		return "True"
	else:
		return "False"

## Sorted uses Timsort - O(n(log(n)) time, O(n) space complexity
## so overall, 2O(nlog(n) time, 2O(n) space)


# A better solution wrt O
def check_array_dict(var1, var2):
	if len(var1) != len(var2):
		return "False"

	words_in_array = {}

	for word in var1 + var2:
		if word in words_in_array.keys():
			words_in_array[word] += 1
		else:
			words_in_array[word] = 1

	for value in words_in_array.values():
		if value != 2:
			return("False")
		else:
			return("True")


## this one is 2O(N) (2 for loops) + 3O(N) (3 if statements)
## So, 5O(N), a little better than the 2nlog(n) but not that much better.
