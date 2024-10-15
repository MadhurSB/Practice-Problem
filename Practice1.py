My code:

student_marks = [input().split()]
student_name = [input()]
def student():
    student_report = {}
    for _ in student_name:
        student_mark = int(student_marks[0] + student_marks[1] + student_marks[2])/3
        student_report = {student_name: student_marks}
    while student_report[student_name] = True:
        print(student_name[student_mark])        
student()

Wrong things in my code:

Key Issues in Your Approach:
Input Collection:

You used input().split() but only stored the result of one input line in student_marks. You should have processed multiple input lines for multiple students.
student_marks should be a dictionary, not a list, because you need to map each student's name to their respective marks. In your approach, student_marks is a list containing just one element, which is not appropriate for multiple students' data.
Variable Assignment:

student_name = [input()] is incorrect for querying a specific student. You don't need to put the input in a list. It should be a single string representing the student’s name to query later.
Logic for Storing Data:

In your student() function, you attempted to calculate the average using student_marks[0] + student_marks[1] + student_marks[2], which assumes all student marks are already separated into individual variables. This would cause an indexing error because your data wasn't structured properly for multiple students.
Incorrect Average Calculation:

You tried to add marks directly with int(student_marks[0] + student_marks[1] + student_marks[2])/3, which concatenates strings instead of performing addition. Even if the data were correctly structured, you would need to convert marks into floats and then sum them.
Dictionary Misuse:

student_report = {student_name: student_marks} creates a dictionary with the whole list of student names as the key, which is not what you want. Each student's name should map to their respective marks, and it should be done inside a loop that processes each student's data.
Incorrect Condition in the Loop:

The while student_report[student_name] = True: line is incorrect syntax for checking the existence of a student. Additionally, using a while loop here is inappropriate. You should use direct dictionary access instead to retrieve the student's marks.
Printing Logic:

print(student_name[student_mark]) doesn't make sense because student_mark is supposed to be the calculated average, not an index for accessing student_name. You should print the result directly, not try to index into student_name.
Correct Approach Breakdown:
Data Storage: Use a dictionary to store students' names as keys and their marks as values in a list.

Querying: You need to handle the query by fetching the marks for the queried student from the dictionary.

Average Calculation: Use sum() to calculate the average of marks and print it with two decimal precision.

if __name__ == '__main__':
    n = int(input())  # Number of students
    student_marks = {}

    # Reading input and storing in dictionary
    for _ in range(n):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))  # Convert the marks to a list of floats
        student_marks[name] = marks

    query_name = input()  # The name of the student to query

    # Calculate the average of the marks for the queried student
    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])

    # Print the result rounded to 2 decimal places
    print(f"{average_marks:.2f}")
