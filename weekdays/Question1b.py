# Given a string of arbitrary length, generate all permutations of the characters in the
# string.
# a. What is the worst-case O(n) of the solution?
# b. How would you handle Unicode character

#Assume input data is a string

def find_permutations(string1):
	letters = list(string1.replace(' ', ''))

	#Define recursive function, perm() to find permutations of the list

	def perm(letters):

		if len(letters) < 2:
			return letters

		else:
			permutations = []

			for i in range(len(letters)):

				new_permutations = perm((letters[:i]+letters[i+1:]))
				add_permutations = [letters[i] + word for word in new_permutations]
				permutations.extend(add_permutations)


			return permutations


	#Find all the permutations of the letters
	all_permutations = perm(letters)

	return all_permutations, len(all_permutations)  # list of all the permutations and the number of permutations


string1 = 'abcde'
new_list, length = find_permutations(string1)
print(new_list)
print(length, "permutations found")