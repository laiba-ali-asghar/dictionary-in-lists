# Dictionary with lists
students_marks = {
    "Ali": [85, 90, 88],
    "Laiba": [92, 95, 89],
    "Sara": [78, 80, 74]
}

# Accessing a list inside dictionary
print("Laiba's marks:", students_marks["Laiba"])

# Adding a new mark to a student's list
students_marks["Ali"].append(91)
print("Ali's updated marks:", students_marks["Ali"])

# Using built-in functions
print("\n--- Built-in Functions on Lists ---")

marks = students_marks["Laiba"]

print("Total marks:", sum(marks))            # sum of list
print("Maximum mark:", max(marks))           # highest value
print("Minimum mark:", min(marks))           # lowest value
print("Number of subjects:", len(marks))     # length of list
print("Sorted marks:", sorted(marks))        # ascending order

# Iterating through dictionary
print("\n--- All Students and Their Marks ---")
for name, mark_list in students_marks.items():
    print(name, "=>", mark_list)
