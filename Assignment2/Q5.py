from datetime import datetime, timedelta


class Task:
    """Store a task timer.
    Note, the timer starts when the object is created.
    Attributes:
        - id: the task name
        - start: datetime representing start time
        - end: datetime representing end time. None when still running
    """

    def __init__(self, task_id, start=None, end=None):
        self.id = task_id
        self.start = start
        if self.start is None:
            self.start_timer()
        self.end = end

    def __repr__(self):
        """ Return a string like what you would use to create a Task.
        When printing a list of `Tasks` this method will be called to display 
        each task. Note, to call this method use the repr() function.
        """
        return f"Task('{self.id}', {repr(self.start)}, {repr(self.end)})"

    def __str__(self):
        """Return a nice human-readable string version of the Task.
        When insterting a task into an f-string this method is called.
        Note, to call this method use the str() function.
        """
        string = f"{self.id} {self.start.date()}: "
        if self.is_running():
            string += "<still running>"
        else:
            string += f"{self.duration()}"
        return string

    def is_running(self):
        """Returns True if task has no end time, False otherwise."""
        return self.end is None

    def start_timer(self):
        """Start the timer by setting start to current datetime"""
        self.start = datetime.now()  # Use the current datetime.

    def end_timer(self):
        """End the timer by setting end to current datetime.
        If the timer is not running do not end the timer."
        """
        if self.is_running():
            self.end = datetime.now()

    def duration(self):
        """Returns the duration of the timer as a timedelta.
        If the timer isn't stopped, return a timedelta(0).
        """
        if not self.is_running():
            return self.end - self.start
        return timedelta(0)

def task_times(tasks):
    """Takes a list of Task objects and returns a dictionary with
    task ids as keys and lists of durations as values."""
    times = {}
    for task in tasks:
        if task.id not in times:
            times[task.id] = []
        if task.end and task.start:  # Ensure there is a start and end time
            times[task.id].append(task.end - task.start)
    return times
