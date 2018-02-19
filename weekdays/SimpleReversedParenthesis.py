# Given a string, return the minimal number of parenthesis reversals needed to make balanced parenthesis.
#
# For example:
#
# solve(")(") = 2 Because we need to reverse ")" to "(" and "(" to ")". These are 2 reversals.
# solve("(((())") = 1 We need to reverse just one "(" parenthesis to make it balanced.
# solve("(((") = -1 Not possible to form balanced parenthesis. Return -1.
# Parenthesis will be either "(" or ")".

import numpy as np

def solve(s):
	change_count = 0
	test_list = list(s)

	if len(test_list)%2 != 0:
		return -1

	while len(test_list) > 1:
		for i in range(len(test_list)):
			if test_list[0] == ")":
				change_count += 1
				test_list[0] = "("
				break
			elif test_list[i] == "(" and ")" in test_list:
				del test_list[i]
				del test_list[test_list.index(")")]
				break
			elif test_list[i] == "(" and "(" in test_list:
				del test_list[i]
				del test_list[test_list.index("(")]
				change_count += 1
				break

	return change_count


change_count = solve("())(((")
print(change_count)

# Other answers:
#
# def solve(s):
#     t = None
#     while t != s:
#         t, s = s, s.replace('()', '')
#     return -1 if len(s) % 2 else sum(1 + (a == tuple(')(')) for a in zip(*[iter(s)] * 2))
#
#
# def solve(s):
#     if len(s) % 2: return -1
#     #imagine a simple symmetric random walk; '(' is a step up and ')' is a step down. We must stay above the original position
#     height = 0; counter = 0
#     for x in s:
#         if x == '(':
#             height += 1
#         else:
#             height -= 1
#         if height < 0:
#             counter += 1
#             height += 2
#     #counter is the number of flips from ')' to '(', height//2 number of opposite flips
#     return counter + height // 2
#
# def solve(s):
#     while "()" in s:
#         s = s.replace("()","")
#     count = 0
#     while len(s)>1:
#         count+=s.count("((")
#         s = s.replace("((","")
#         count+=s.count("))")
#         s = s.replace("))","")
#         count+=(s.count(")(")*2)
#         s = s.replace(")(","")
#     return count if len(s)==0 else -1
#
#
# def solve(s):
#     if len(s) % 2 != 0:
#         return -1
#     res, k = 0, 0
#     for c in s:
#         k += 1 if c == '(' else -1
#         if k < 0:
#             k += 2
#             res += 1
#     return res + k // 2