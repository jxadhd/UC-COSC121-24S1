"""This module NOT to be submitted - for testing and
   research only"""
""" COSC121 Assignment 2, Question 11
    This version replaces the cmd-printed graphs from Q10
    with a gui-graph printed by matplotlib.
    Author: J Cross (UCID 26210771)
    23/05/2024
    """
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np


MENU = """Options:
    [s] start timer
    [e] end timer
    [d] delete
    [r] report
    [a] analytics
    [q] quit"""
VALID_INSTRUCTIONS = {'s', 'e', 'd', 'r', 'a', 'q'}
NO_DATETIME = ''


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


def read_list(prompt):
    """Prompt user for input (comma separated values).
    Returns a list of the comma separated values, whitespace stripped.
    """
    strings = input(prompt).split(',')
    return [string.strip() for string in strings]


def read_valid_input(valids, transformer=None):
    """Read and return an input from stdin.
    Only accept inputs in valids, repeatedly prompt until one is given.
    Apply the transformer function to the user's inputs, if provided.
    """
    instruction = input('Select option: ')
    if transformer:
        instruction = transformer(instruction)
    while instruction not in valids:
        print('Please select a valid option')
        instruction = input('Select option: ')
        if transformer:
            instruction = transformer(instruction)
    return instruction


def read_instruction():
    """Read and return a valid instruction from stdin."""
    instruction = read_valid_input(VALID_INSTRUCTIONS, str.lower)
    return instruction


def select_timer_index(tasks):
    """Takes a list of Task objects, then prompts the
    user to select one. Returns the user selected Task object.
    """
    print("Select task:")
    for i, task in enumerate(tasks):
        print(f"      [{i}] {str(task)}")
    valid_task_nums = range(len(tasks))
    task_index = read_valid_input(valid_task_nums, int)
    return task_index


def add_task(tasks, task_id=None, start=None, end=None):
    """Add a new task to tasks.
    When task_id isn't provided prompt the user for it.
    """
    if task_id is None:
        task_id = input("Enter project name: ")
    timer = Task(task_id, start, end)
    tasks.append(timer)



def end_task(tasks):
    """Prompt the user to select a running task (from tasks).
    End the selected task.
    """
    running_tasks = [task for task in tasks if task.is_running()]
    if len(running_tasks) > 0:
        task_index = select_timer_index(running_tasks)
        task = tasks[task_index]
        task.end_timer()
    else:
        print("Can't end task: no timers are running.")


def delete_task(tasks):
    """Prompt the user to select a task (from tasks).
    Remove the selected task from tasks.
    """
    if len(tasks) > 0:
        task_index = select_timer_index(tasks)
        tasks.pop(task_index)
    else:
        print("Can't delete task: no timers exist.")


def print_report(tasks):
    """Print a basic report of times in tasks."""
    print("Report:")
    for task in tasks:
        print(f"    {task}")


def timedelta_duration_string(delta):
    """Returns string representation of  a datetime.timedelta as:
    hours:minutes:seconds.
    This function will be useful when answering question 8.
    """
    seconds_in_minute = 60
    seconds_in_hour = seconds_in_minute * 60

    seconds = delta.total_seconds()
    hours, seconds = divmod(seconds, seconds_in_hour)
    minutes, seconds = divmod(seconds, seconds_in_minute)
    return f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

def datetime_from_iso(string):
    """Return a datetime from an ISO format string.
    When no datetime, return None.
    """
    if string == NO_DATETIME:
        return None
    return datetime.fromisoformat(string)


def read_task_file(filename):
    """Opens a task file, with file name filename and reads it. 
    Returns a task list containing the tasks in that file.
    """
    infile = open(filename, 'r')
    lines = infile.read().splitlines()
    infile.close()

    tasks = []
    for line in lines:
        name, start, end = line.split(',')
        start = datetime_from_iso(start)
        end = datetime_from_iso(end)
        add_task(tasks, name, start, end)
    return tasks

def write_task_file(filename, tasks):
    """Write tasks to data file"""
    with open(filename, "w") as outfile:
        for task in tasks:
            end = task.end.isoformat() if task.end else ''
            line = f"{task.id},{task.start.isoformat()},{end}\n"
            outfile.write(line)

def print_analytics(tasks):
    """Returns all stored task IDs, no. of instances and total time"""
    task_dict = {}
    for task in tasks:
        if task.end:
            if task.id not in task_dict:
                task_dict[task.id] = {'count': 1, 'time': task.duration()}
            else:
                task_dict[task.id]['count'] += 1
                task_dict[task.id]['time'] += task.duration()

    sorted_tasks = sorted(task_dict.items())
    print("Task Analytics:")
    print("    Task ID    Freq Time")

    total_time = timedelta(0)
    total_count = 0
    for task_id, task_info in sorted_tasks:
        print(f"    {task_id:10}{task_info['count']:5}", end =' ')
        print(f"{timedelta_duration_string(task_info['time'])}")
        total_time += task_info["time"]
        total_count += task_info["count"]

    print(f"You spent {timedelta_duration_string(total_time)} on {total_count} task(s).")
    total_seconds = total_time.total_seconds()
    print("\nTotal Time (%)")
    analytics_bargraph(total_seconds, sorted_tasks)

def analytics_bargraph(total_seconds, sorted_tasks):
    """This function prints a bar graph showing the percentage of total time spent on each task."""
    # Extract task IDs and calculate percentages
    task_ids = [task_id for task_id, task_info in sorted_tasks]
    percentages = [round((task_info['time'].total_seconds() / total_seconds) * 100) for task_id, task_info in sorted_tasks]

    # Create the bar graph
    plt.bar(task_ids, percentages)
    
    # Format the x-axis
    plt.xticks(np.arange(len(task_ids)), [f'{task_id[:9]:^9}' for task_id in task_ids])
    plt.xlabel('     Tasks')
    
    # Format the y-axis
    max_percentage = max(percentages)
    y_max = min(max_percentage + 5 - (max_percentage % 5), 100)
    plt.yticks(np.arange(0, y_max + 1, 5), [f'{i:>3}' for i in range(0, y_max + 1, 5)])
   
    
    # Set the title
    plt.title('Total Time(%)', loc='center')
    
    # Show the plot
   
    plt.show()


def main():
    """Ask for an input filename, if one is provided read the tasks from that file. 
    Show the menu once and accept commands until the quit command is given.
    When quitting, ask for a filename and save the tasks to that file.
    """
    tasks = []
    filename = input("Enter filename to open (or enter to skip): ")
    if filename:
        tasks = read_task_file(filename)

    instruction = ''
    print(MENU)
    while instruction != 'q':
        instruction = read_instruction()
        if instruction == 's':
            add_task(tasks)
        elif instruction == 'e':
            end_task(tasks)
        elif instruction == 'd':
            delete_task(tasks)
        elif instruction == 'r':
            print_report(tasks)
        elif instruction == 'a':
            print_analytics(tasks)
        elif instruction == 'q':
            filename = input("Save tasks as (enter filename): ")
            if filename:
                write_task_file(filename, tasks)
            break

main()
