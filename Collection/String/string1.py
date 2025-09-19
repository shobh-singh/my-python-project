text = "  Hello Python World  "

# Length
print(len(text))              # 21

# Lower & Upper
print(text.lower())           # "  hello python world  "
print(text.upper())           # "  HELLO PYTHON WORLD  "

# Strip (remove extra spaces)
print(text.strip())           # "Hello Python World"

# Split (convert into list)
words = text.strip().split()
print(words)                  # ['Hello', 'Python', 'World']

# Join (list to string)
print("-".join(words))        # "Hello-Python-World"

# Replace
print(text.replace("Python", "Java"))  # "  Hello Java World  "

# Find substring
print(text.find("Python"))    # 8 (index)

# String slicing
print(text[2:7])              # "Hello"



for ch in "Hello":
    print(ch)

