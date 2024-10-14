"""Question 7 COSC121
    Author: Josh Cross
    Date: 06th May 2024
"""

def main():
    """Returns grade statistics"""
    filename = get_filename()
    data = read_data(filename)
    stats = statistics(data)
    print_results(stats)

def get_filename():
    """Return the name of the student data file to be processed.
       This is a so-called 'stub' implementation which always returns
       the same filename. A fuller implementation would prompt the user
       for the filename.
    """
    return "data.csv"

def read_data(filename):
    """Read and return the contents of the given file.
       The file is assumed to exist, or an exception will occur.
       It is also assumed that each line of the file consists of a
       student name, a comma, and a floating-point mark.
       Returns: a list of (name, mark) tuples, where name is a string
       and mark is a floating-point number.
    """
    data = []
    with open(filename, 'r') as grades:
        for line in grades:
            name, mark = line.strip().split(',')
            data.append((name, float(mark)))
    return data

def statistics(student_data):
    """Given a list of (name, mark) pairs, returns a tuple containing
       statistics extracted from the list. The components of the returned tuple 
       are minimum_mark, maximum_mark, average_mark and top_students. The
       first three are just floating point values. The last one is an
       alphabetically ordered list of the names of all students whose
       marks are equal to the maximum_mark.
    """
    marks = [mark for name, mark in student_data]
    names = [name for name, mark in student_data]
    min_mark = min(marks)
    max_mark = max(marks)
    avg_mark = sum(marks) / len(marks)
    top_students = sorted([name for name, mark in student_data if mark == max_mark])
    return min_mark, max_mark, avg_mark, top_students

def print_results(stats_tuple):
    """Print the statistics given. The parameters 'stats_tuple' is a
       tuple of the form returned by the 'statistics' function
       above.
    """
    (minimum, maximum, average, top_students) = stats_tuple
    print(f"Minimum mark: {minimum:.2f}")
    print(f"Maximum mark: {maximum:.2f}")
    print(f"Average mark: {average:.2f}")

    if len(top_students) == 1:
        print(f"Top student: {top_students[0]}")
    else:
        print(f"Top-equal students:\n  {', '.join(top_students)}")

main()
