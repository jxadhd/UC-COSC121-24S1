SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60

# Function to convert time string to seconds
def to_seconds(time_string):
    """Split the time_string into hours, minutes, and seconds"""
    hours, minutes, seconds = time_string.split(':')
    
    # Convert strings to integers
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)
    
    # Calculate total seconds
    total_seconds = (hours * SECONDS_PER_HOUR) + (minutes * SECONDS_PER_MINUTE)\
        + seconds
    
    return total_seconds


def new_task(task_id, start_string):
    """Function to create a new task"""
    return (task_id, [to_seconds(start_string)])


def start_task(tasks, task_id):
    """Check if the last task is still running"""
    if tasks and len(tasks[-1][1]) == 1:
        print("Can't start a timer, one is already running")
    else:
        # Prompt the user for the start time
        start_time = input("Please enter a time (hh:mm:ss): ")
        # Call the new_task function to create a new task tuple
        new_task_tuple = new_task(task_id, start_time)
        # Append the new task tuple to the tasks list
        tasks.append(new_task_tuple)


def end_active_task(tasks):
    """Check if there is an active task"""
    if not tasks or len(tasks[-1][1]) != 1:
        print("No timer is currently running")
    else:
        # Prompt the user for the end time
        end_time = input("Please enter a time (hh:mm:ss): ")
        # Append the end time to the timer list of the active task
        tasks[-1][1].append(to_seconds(end_time))



my_tasks = [
    (['COSC121', 'Assignment 1', 'Question 1'], [57600])
]
end_active_task(my_tasks)
print(my_tasks)

def read_list(prompt):
    """
    Prompts the user for a list of comma-separated values and returns a list of these values.
    Each string in the returned list has leading and trailing white-space removed.

    Args:
        prompt (str): The prompt to display to the user.

    Returns:
        list: A list of cleaned comma-separated values entered by the user.
    """
    user_input = input(prompt)
    values = [item.strip() for item in user_input.split(',')]
    return values

