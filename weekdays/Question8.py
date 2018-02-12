# Search a word’s anagrams for a specific value
# a. True: ‘Foo’ in ‘Poof’
# b. False ‘Hah’ in ‘Poof’

def anagrams(string1, word):
	string1 = list(string1.lower())
	word = list(word.lower())

	for i in word:
		if i in string1:
			string1.remove(i)
		else:
			return "False"

	return "True"

check = anagrams('Poof','Foo')
print(check)