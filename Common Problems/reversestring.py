def reverse_string(word):
	if type(word) is not str:
		raise Exception("Please enter a string")
	new_str = ""
	for letter in word:
		new_str = letter + new_str
	return new_str

def reverse_string_recursion(word):
	if word == "":
		return word
	else:
		return reverse_string_recursion(word[1:]) + word[0] 
