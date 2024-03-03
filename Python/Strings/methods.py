txt = "hello world"

res = txt.upper()
print(res)  # Output: HELLO WORLD

res = txt.lower()
print(res)  # Output: hello world

res = txt.capitalize()
print(res)  # Output: Hello world

res = txt.title()
print(res)  # Output: Hello World

txt = "Hello World"
res = txt.swapcase()
print(res)  # Output: HELLO WORLD

txt = "   hello world "
res = txt.strip()
print(res)  # Output: hello world

txt = "hello world"
res = txt.replace("hello", "hi")
print(res)  # Output: hi world

res = txt.startswith("hello")
print(res)  # Output: True

res = txt.endswith("world")
print(res)  # Output: True

# true - all characters in the string are alphabet
txt = "hello"
res = txt.isalpha()
print(res)  # Output: True

# true - string is alphanumeric
txt = "year2024"
res = txt.isalnum()
print(res)  # Output: True

# true - all characters in the string are digits
txt = "123"
res = txt.isdigit()
print(res)  # Output: True

txt = "hello world"
res = txt.islower()
print(res)  # Output: True

res = txt.isupper()
print(res)  # Output: False

txt="The most important thing is to enjoy your life at the fullest"
res=txt.find("life")
print(res)
print(type(res))
res=txt.find("big")
print(res)

txt = "apple,orange,guava"
res = txt.split(",")
print(res)
print(type(res))  # list
