
def highest_product(integer_array):

	sorted_array = sorted(integer_array)
	max_product = 1

	# Know that if there are no negative numbers, or if there is only one negative number, the max is just
	# the three max numbers multiplied together
	# Also know that if all numbers are negative, the max is the three smallest numbers multiplied together
	# Either way, it will be the last 3 numbers in the sorted list

	if sorted_array[0] >= 0 or sorted_array[-1] < 0:
		for num in sorted_array[-3:]:
			max_product *= num

	# If there is a mix of + and - numbers then its trickier. Two negative numbers must be used if they are to be used
	# at all, so you can get the 3 possibilities with negative numbers easily.
	# Pick the maximum of those and multiply it by the largest positive number and compare
	# that value with the largest three positive numbers multiplied together.
	# Whichever is largest is the max.

	else:
		new_array = []
		# Could probably use itertools here, but only 3 values
		new_array.append((sorted_array[0]*sorted_array[1]))
		new_array.append((sorted_array[1]*sorted_array[2]))
		new_array.append((sorted_array[0]*sorted_array[2]))

		max_neg = max(new_array)

		if max_neg * max(sorted_array) >= sorted_array[-3]*sorted_array[-2]*sorted_array[-1]:
			max_product =  max_neg * max(sorted_array)
		else:
			max_product = sorted_array[-3]*sorted_array[-2]*sorted_array[-1]

	print(max_product)
	return max_product   #integer



# highest_product([1,3,7,3,4,6,4,2,3])
# highest_product([0,0,0])
# highest_product([1,2,3])
highest_product([-2,3,-8,11,4,-5,10,-10])
# highest_product([-2,-3,-8,-10,-10])
