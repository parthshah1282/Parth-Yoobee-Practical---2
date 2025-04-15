# Import the numpy library and give it a short name 'np'
import numpy as np

# ---------------------------------------------
# Activity 1: Work with a 1D NumPy array
# ---------------------------------------------

# Create a NumPy array of the first 10 positive integers
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Print the array
print("Original array:", numbers)

# Print the shape of the array (how many elements and dimensions)
print("Shape of array:", numbers.shape)

# Print the data type of the array elements
print("Data type of array:", numbers.dtype)

# Multiply each element by 2 and print the result
doubled = numbers * 2
print("Array elements multiplied by 2:", doubled)

# ---------------------------------------------
# Activity 2: Work with a 2D NumPy array (like a table)
# ---------------------------------------------

# Scores of 5 students across 3 subjects
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])

# Calculate the average score for each student (across each row)
student_averages = np.mean(scores, axis=1)
print("Average score of each student:", student_averages)

# Calculate the average score for each subject (down each column)
subject_averages = np.mean(scores, axis=0)
print("Average score of each subject:", subject_averages)

# Find the student with the highest total score
# Sum each student's scores and get the index of the highest one
total_scores = np.sum(scores, axis=1)
top_student_index = np.argmax(total_scores)
print("Student with the highest total score (row index):", top_student_index)

# Add 5 bonus points to the third subject for all students
scores[:, 2] += 5
print("Updated scores after adding 5 bonus points to third subject:\n", scores)
