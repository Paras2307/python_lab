# Input matrix
matrix = [
    [1, -2, 3],
    [-4, 5, 6],
    [7, 8, -9]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# 1. Remove negative numbers using filter()
filtered_matrix = list(map(
    lambda row: list(filter(lambda x: x >= 0, row)), matrix
))

print("\nMatrix after removing negative numbers:")
for row in filtered_matrix:
    print(row)

# 2. Square each element using map()
squared_matrix = list(map(
    lambda row: list(map(lambda x: x * x, row)), filtered_matrix
))

print("\nSquared Matrix:")
for row in squared_matrix:
    print(row)

# 3. Sort each row using sorted()
sorted_matrix = list(map(lambda row: sorted(row), filtered_matrix))

print("\nSorted Matrix:")
for row in sorted_matrix:
    print(row)

# 4. Convert matrix rows into tuples
tuple_matrix = tuple(map(tuple, sorted_matrix))

print("\nMatrix as Tuples:")
print(tuple_matrix)