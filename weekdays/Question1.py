#Given a string of arbitrary length, generate all permutations of the characters in the
#string.
#a. What is the worst-case O(n) of the solution?
#b. How would you handle Unicode character

# Assume input data is a string

def find_permutations(string1):
	letters = list(string1.replace(' ',''))

	try:
		permutations
	except NameError:
		permutations = [string1]

	for i in range(len(letters)):

		for j in range(i+1,len(letters)):

			new_permutation = list(letters)
			new_permutation[i] = letters[j]
			new_permutation[j] = letters[i]
			new_permutation = str(''.join(new_permutation))

			if new_permutation not in permutations:
				permutations.append(new_permutation)
				new_letters = list(new_permutation)

				for x in range(len(new_letters)):

					for y in range(x + 1, len(new_letters)):

						new_permutation = list(new_letters)
						new_permutation[x] = new_letters[y]
						new_permutation[y] = new_letters[x]
						new_permutation = str(''.join(new_permutation))

						if new_permutation not in permutations:
							next_permutation = str(''.join(new_permutation))
							permutations.append(next_permutation)

	return permutations,len(permutations)     # list of all the permutations and the number of permutations

string1 = 'abc'

new_list, length = find_permutations(string1)
print(length, "permutations found")
print(new_list)