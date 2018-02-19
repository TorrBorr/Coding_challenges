# The goal of this exercise is to convert a string
# to a new string where each character in the new
# string is '(' if that character appears only once
# in the original string, or ')' if that character
# appears more than once in the original string.
# Ignore capitalization when determining if a
# character is a duplicate.
#
# Examples:
#
# "din" => "((("
#
# "recede" => "()()()"
#
# "Success" => ")())())"
#
# "(( @" => "))(("


def duplicate_encoder(word):
	word_dict = {}
	for i in word.lower():
		if i in word_dict:
			word_dict[i] += 1
		else:
			word_dict[i] = 1
	encoded = []
	for letter in word.lower():
		if word_dict[letter] > 1:
			encoded.append(")")
		else:
			encoded.append("(")

	return "".join(encoded)

word = 	"(( @"

encoded_word = duplicate_encoder(word)
print(encoded_word)