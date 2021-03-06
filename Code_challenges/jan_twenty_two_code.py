# You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.
#
# Find max(abs(length(x) − length(y)))
#
# If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).
#
# #Example:
#
# s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# mxdiflg(s1, s2) --> 13

#My submitted code:

def mxdiflg(a1, a2):
	if len(a1) == 0 or len(a2) == 0:
		return -1
	else:
		a1_lengths = [len(a) for a in a1]
		a2_lengths = [len(a) for a in a2]

		if abs(max(a1_lengths) - min(a2_lengths)) > abs(max(a2_lengths) - min(a1_lengths)):
			return abs(max(a1_lengths) - min(a2_lengths))
		else:
			return abs(max(a2_lengths) - min(a1_lengths))


#Better code:

# def mxdiflg(a1, a2):
#     if a1 and a2:
#         return max(
#             len(max(a1, key=len)) - len(min(a2, key=len)),
#             len(max(a2, key=len)) - len(min(a1, key=len)))
#     return -1

#
# def mxdiflg(a1, a2):
#     if a1 and a2:
#         return max(abs(len(x) - len(y)) for x in a1 for y in a2)
#     return -1