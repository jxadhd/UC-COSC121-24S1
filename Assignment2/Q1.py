from datetime import datetime, timedelta

def days_till_exam():
    """Returns the number of days until the COSC121-2024S1 exam (at 20/06/2024 14:30:00)."""
    exam_date = datetime(2024, 6, 20, 14, 30)
    difference = exam_date - datetime.now()
    return difference.days
print(days_till_exam())