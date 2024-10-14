"""DS here"""

def common(course1, course2, course3):
    """Returns IDs of students in all courses"""
    return set(course1) & set(course2) & set(course3)