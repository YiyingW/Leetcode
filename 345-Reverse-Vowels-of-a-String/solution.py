class Solution(object):
	def reverseVowels(self, s):
		string = [l for l in s]
		i = 0
		j = len(string) - 1
		vowels = ['a','e','i','o','u','A','E','I','O','U']
		while (i < j):
			if string[i] in vowels and string[j] in vowels:
				string[i], string[j] = string[j], string[i]
				i += 1
				j -= 1
			elif string[i] in vowels and string[j] not in vowels:
				j -= 1
			elif string[i] not in vowels and string[j] in vowels:
				i += 1
			else:
				i += 1
				j -= 1




		return "".join(string)