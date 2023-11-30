import pandas as pd

# Reading the Excel file
df = pd.read_excel('My_Data.xlsx')

# Extract columns
quiz = df["QUIZZES "]
assignment = df["ASSIGNMENTS"]
mid = df["MID-TERM"]
final = df["FINAL"]

# Filling empty cells with the mean value
quiz.fillna(quiz.mean(axis=0), inplace=True)
assignment.fillna(assignment.mean(axis=0), inplace=True)
mid.fillna(mid.mean(axis=0), inplace=True)
final.fillna(final.mean(axis=0), inplace=True)

# Calculating the median of the filled "QUIZZES" column
median_quiz = quiz.median()

# Calculating the mode of the filled "ASSIGNMENTS" column
mode_assignment = assignment.mode().iloc[0]

# Calculating the mean of the filled "MID-TERM" column
mean_mid = mid.mean()

# Calculating the mean of the filled "final" column
mean_final = final.mean()

# Print the results
print("Median value of the Quiz Axis:", median_quiz)
print("Mode value of Assignment Axis:", mode_assignment)
print("Mean value of the Mid Term Axis:", mean_mid)
print("Mean value of the Final Axis:", mean_final)

print(df.describe)

# Determine the number of students who have taken the quiz
number_of_students = df.shape[0]

# Determine the number of students who have done the midterm
number_of_students_midterm = df.shape[0]

# Calculate the standard deviation of the midterm scores
std_dev_midterm = df['MID-TERM'].std()

# Print the results
print("Number of students who have taken the quiz:", number_of_students)
print("Number of students who have done the midterm:", number_of_students_midterm)
print("Standard deviation of the midterm scores:", std_dev_midterm)


# Assuming there is a "SEMESTER" column in your DataFrame
semester_group = df.groupby("Semester")

# Identify students with Mid Exam  and final exam scores above the mean
better_mid_students = df[df["MID-TERM"] > mean_mid]
better_final_studentss = df[df["FINAL"] > mean_final]


# Calculate the mean Mid Term score for each semester
mean_mid_by_semester = semester_group["MID-TERM"].mean()

# Find the semester with the highest mean Mid Term score
best_semester = mean_mid_by_semester.idxmax()
mean_value_for_comparison = mean_mid_by_semester.max()

# Print the result
print("Students who performed better in the Mid Exam:")
print(better_mid_students)
print("Students who performed better in the final Exam:")
print(better_final_studentss)
print("Used mean value for comparison:", mean_value_for_comparison)
print("Best-performing semester for Mid Exam:", best_semester)
print("Used mean value for comparison:", mean_value_for_comparison)

