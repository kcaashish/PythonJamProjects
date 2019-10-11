
def stringType(s):
	if s.isupper():
		return "Uppercase"
	elif s.islower():
		return "Lowercase"
	elif s.istitle() and " " in s:
		return "Titlecase"
	else:
		return "Capitalised"


print(stringType("HELLO"))
print(stringType("hello"))
print(stringType("Hello there"))
print(stringType("Hello There"))
