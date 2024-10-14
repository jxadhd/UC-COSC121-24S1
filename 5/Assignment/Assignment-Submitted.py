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


def read_list(prompt):
    """Prompts the user for a list of comma-separated values and returns a list of these values.
    Each string in the returned list has leading and trailing white-space removed."""
    user_input = input(prompt)
    values = [item.strip() for item in user_input.split(',')]
    return values

class Timer:
    """A simple timer application that allows users to manage timers with various commands."""

    def __init__(self):
        """Initialize the Timer class with an empty active timer and a list of completed timers."""
        self.active_timer = None
        self.timers = []

    def start_task(self):
        """Start a new active timer.
        The user is prompted for task IDs (comma-separated)."""
        if self.active_timer:
            print("Can't start a timer, one is already running.")
            return
        task_ids = input("Enter task IDs (comma-separated): ").split(",")
        self.active_timer = {"task_ids": task_ids, "start_time": None}

    def end_active_task(self):
        """Stop the last active timer.
        If there is no active task, display an appropriate message."""
        if not self.active_timer:
            print("No timer is currently running.")
            return
        end_time = input("Please enter a time (hh:mm:ss): ")
        self.active_timer["end_time"] = end_time
        self.timers.append(self.active_timer)
        self.active_timer = None

    def delete_task(self):
        """Remove the last task entry.
        If there are no timers, display an appropriate message."""
        if not self.timers:
            print("Can't remove task when none exist.")
            return
        self.timers.pop()

    def report_timers(self):
        """List all current timers."""
        print("Report:")
        for timer in self.timers:
            task_ids = ",".join(timer["task_ids"])
            print(f"    ({task_ids}) {timer['start_time']}:{timer['end_time']}")

    def read_list(self, filename):
        """Read data from a file and return it as a list."""
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                print(f"Reading data from file: {filename}")
                return lines
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return []

    def run(self):
        """Main loop."""
        while True:
            command = input("Select command (s/e/d/r/q): ").lower()
            if command == "s":
                self.start_task()
            elif command == "e":
                self.end_active_task()
            elif command == "d":
                self.delete_task()
            elif command == "r":
                self.report_timers()
            elif command == "q":
                break
            else:
                print("Command is not valid. Please try again.")

def main():
    """Entry point for the timer application."""
    timer_app = Timer()
    timer_app.run()

if __name__ == "__main__":
    main()
