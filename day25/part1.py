foo = open('example').read().split('\n\n')
for bar in enumerate(foo):
    print(bar)

print("---")

items = [{i for i, c in enumerate(item) if c == '#'}
    for item in open('example').read().split('\n\n')]

# 3. Calculating the Number of Non-Overlapping Pairs:

#     sum(not k&l for k in items for l in items)//2:
#         for k in items for l in items: This nested loop iterates through all possible pairs of sets within the items list.
#         k&l: This calculates the intersection of sets k and l.
#         not k&l: This checks if the intersection of sets k and l is empty (i.e., no common elements). If the intersection is empty, not k&l evaluates to True, otherwise False.
#         sum(...): Sums up the number of True values (i.e., the number of pairs of sets with no common elements).
#         //2: Divides the sum by 2 to account for the fact that each pair of sets is counted twice (e.g., the pair {set1, set2} is the same as the pair {set2, set1}).

# print(sum(not k&l for k in items for l in items)//2)

# Initialize a counter to 0
count = 0

# Iterate through each item in the 'items' list
for k in items:
    # Iterate through each item in the 'items' list again
    for l in items:
        print(k,l)
        # Check if the bitwise AND of k and l is zero
        # (meaning they have no common set bits)
        if not (k & l):
            # If no common set bits, increment the counter
            count += 1

# Divide the count by 2 to get the actual number of unique pairs
count //= 2

# Print the result
print(count)
