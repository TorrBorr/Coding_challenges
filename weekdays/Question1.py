#Given a string of arbitrary length, generate all permutations of the characters in the
#string.
#a. What is the worst-case O(n) of the solution?
#b. How would you handle Unicode character

#Assume my

def find_permutations(string1):
	print(string1)
	print(type(string1))
	letters = string1.replace(' ','')
	letters = list(letters)

	try:
		n
	except:
		n=0
	n=n+1
	print(n)

	try:
		permutations
	except NameError:
		permutations = [string1]


	for i in range(len(letters)):
		print("first i =", i)
		#print(letters[i])
		for j in range(i+1,len(letters)):
			print("first j =", j)
			#print(letters[j])
			new_permutation = list(letters)
			new_permutation[i] = letters[j]
			new_permutation[j] = letters[i]
			new_permutation = str(''.join(new_permutation))
			print(new_permutation)
			if new_permutation not in permutations:
				#next_permutation = str(''.join(new_permutation))
				permutations.append(new_permutation)
				print(permutations)
				print(new_permutation)
				print(type(new_permutation))


				letters = list(new_permutation)

				for i in range(len(letters) - 1):
					#print(i)
					print(letters[i])
					for j in range(i + 1, len(letters)):
						#print(j)
						print(letters[j])
						new_permutation = list(letters)
						new_permutation[i] = letters[j]
						new_permutation[j] = letters[i]
						new_permutation = str(''.join(new_permutation))
						print("new_permutation =", new_permutation)
						if new_permutation not in permutations:
							next_permutation = str(''.join(new_permutation))
							permutations.append(next_permutation)
							print(permutations)
							print(next_permutation)
							print(type(next_permutation))

				#find_permutations(new_permutation)




	return permutations     # list of all the permutations from the list

string1 = 'abc'
#string1 = 'i hate SQL'
#string2 = 'SQL is the worst'


new_list = find_permutations(string1)
print(new_list)