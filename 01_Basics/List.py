# List

#they are mutable
#they can hold duplicates

# declaring list
marks = [85, 90, 78, 92, 88]
print(marks)

# Accessing elements
print(marks[0])
print(marks[3])

# modifying
marks[2] = 80
print(marks)

# appending element (at the end)
marks.append(95)
print(marks)

# Insert at particular index 
marks.insert(1, 100)
print(marks)

# Removing element
marks.remove(80)
print(marks)

# Remove and return the last element
removed_mark = marks.pop()
print(removed_mark)
print(marks)

# length
print(len(marks))


# Print each mark one by one
for mark in marks:
    print(mark)

# whether element exists in the list
print(90 in marks)

# Sorting list
marks.sort()
print(marks)

# Reversing list
marks.reverse()
print(marks)

# Slicing

#accesing index
print(marks[1:5])
print(marks[:4])
print(marks[2:])

# Create a copy of the list
new_marks = marks[:]
print(new_marks)

# Select every second element
print(marks[::2])

# Select elements at odd indices
print(marks[1::2])

# Extract last three elements
print(marks[-3:])

# Reverse the list
print(marks[::-1])

# Extract from -5 to -2
print(marks[-5:-1])

# Replace elements from index 1 to 2
marks[1:3] = [100, 90]
print(marks)

# Print all marks in one line
for mark in marks:
    print(mark, end=" , ")

for mark in marks:
    if mark > 80:
        print(mark, "is greater than 80")

# Check if element is present
if 90 in marks:
    print("90 is present in the list")

#list comprehension
marks = [85, 90, 78, 92, 88]
new_marks = [mark for mark in marks]
print(new_marks)