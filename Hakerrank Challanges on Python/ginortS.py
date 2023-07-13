# Read the input string
st = input()

# Initialize empty lists for each category of characters
lowercase = []
uppercase = []
odd_digits = []
even_digits = []

# Iterate over each character in the input string and categorize it
for c in st:
    if c.islower():
        lowercase.append(c)
    elif c.isupper():
        uppercase.append(c)
    elif c.isdigit():
        if int(c) % 2 == 0:
            even_digits.append(c)
        else:
            odd_digits.append(c)

# Sort each list in ascending order
lowercase.sort()
uppercase.sort()
odd_digits.sort()
even_digits.sort()

# Print the concatenated strings for each category
print("".join(lowercase), end="")
print("".join(uppercase), end="")
print("".join(odd_digits), end="")
print("".join(even_digits), end="")
