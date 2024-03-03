a = "Hello"
print(a)
a = 'Hello'
print(a)

# Multiline String
a = """Hello,
How are you?
I'm fine"""
print(a)

# Python does not have a character data type, a single character is simply a string with a length of 1.
a = "Hello"
print(a[0])

# Looping Through a String
for x in "banana":
    print(x)

# String Length
print(len(a))

txt = "Life is a beautiful journey"
print("journey" in txt)

if "Life" in txt:
    print("Yes")
else:
    print("No")
