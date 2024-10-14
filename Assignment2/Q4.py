"""Q4"""

from datetime import datetime, timedelta

def task_frequencies(task_hours):
    """Takes a dictionary with task ids as keys and lists of timedelta objects as values.
    Returns a dictionary mapping each task id to the number of timers it had."""
    frequencies = {}
    for task_id, timers in task_hours.items():
        frequencies[task_id] = len(timers)
    return frequencies

# Example usage:
task_hours = {
    "COSC121": [timedelta(hours=1), timedelta(hours=2)],
    "STAT201": [timedelta(hours=3)]
}

print(task_frequencies(task_hours))