# Normal way
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)   # [1, 4, 9, 16, 25]

# Using List Comprehension
squares = [i * i for i in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

# With condition
even_squares = [i * i for i in range(1, 11) if i % 2 == 0]
print(even_squares)   # [4, 16, 36, 64, 100]
