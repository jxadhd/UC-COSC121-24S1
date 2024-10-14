"""Object orientation example: Student objects"""

class Student:
    """Defines a Student class, for use in a context similar to COSC121
    Data attributes: name: str of Student's full name
                     student_id: int of Student's ID
                     invigilated: float of Student's mark on test & exam
                     uninvigilated: float of Student's mark on LMs & assignments
    Methods: total_mark(), has_passed()
    """
    INVIGILATED_WEIGHT = 0.7
    UNINVIGILATED_WEIGHT = 0.3
    INVIGILATED_PASS_MARK = 0.45
    OVERALL_PASS_MARK = 0.5

    def __init__(self, name, student_id, invigilated, uninvigilated,):
        """Creates a new Student object with the specified name, id, 
           and marks
        """
        self.name = name
        self.student_id = student_id
        self.invigilated = invigilated
        self.uninvigilated = uninvigilated

    def total_mark(self):
        """Returns the weighted mark for the course"""
        invigilated_portion = self.invigilated * self.INVIGILATED_WEIGHT
        uninvigilated_portion = self.uninvigilated * self.UNINVIGILATED_WEIGHT
        return invigilated_portion + uninvigilated_portion

    def has_passed(self):
        """Returns True if the Student has passed the course
            and False otherwise, considering both the total mark
            and the invigilated pass requirement
            """
        has_overall_pass = self.total_mark() >= self.OVERALL_PASS_MARK
        has_invigilated_pass = self.invigilated >= self.INVIGILATED_PASS_MARK
        return has_overall_pass and has_invigilated_pass

    def grade(self):
        """Determines the student's letter grade (simplified)"""
        mark = self.total_mark()
        if not self.has_passed():
            return "D"
        elif self.has_passed():
            if mark < 0.65:
                return "C"
            elif mark < 0.8:
                return "B"
            elif mark >= 0.8:
                return "A"

    def __str__(self):
        """Returns a str of the Student object suitable for printing"""
        mark = self.total_mark() * 100
        grade = self.grade()
        return f"{self.name} ({self.student_id}). Grade: {grade} ({mark:.0f}%)."

    def __repr__(self):
        """Returns a str representation of the Student object"""
        return f"Student('{self.name}', {self.student_id}, {self.invigilated}, {self.uninvigilated})"

def read_students(csv_filename):
    """Creates Student object from CSV file"""
    studentlist = []
    with open(csv_filename, "r") as file:
        for line in file:
            row = line.strip().split(",")
            name, student_id, invigilated, uninvigilated = row
            newstudent = Student(name, int(student_id), float(invigilated), float(uninvigilated))
            studentlist.append(newstudent)
    return studentlist

def filter_students(students, letter_grade):
    """Returns just students who meet letter_grade"""
    gradefilter = []
    for each in students:
        if each.grade() == letter_grade:
            gradefilter.append(each)
    return gradefilter

def id_value(student):
    """Returns Student ID Val to use as sorting key"""
    return student.student_id

def mark_value(student):
    """Returns student mark value for use as sorting key"""
    return student.total_mark()
