# Create an empty list called my_list
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)

# Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove the last element from the list
my_list.pop()

# Sort the list in an ascending order
my_list.sort()

# Find the index of 30 in the list
index_of_30 = my_list.index(30)

# Print the index of 30
print("Index of 30 in my_list is " + str(index_of_30))
