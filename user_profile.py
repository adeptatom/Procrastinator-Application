# Imports
import csv_data
import time
import app

# Global Variables
user = None

# Class that holds all the attributes of the user.
class User:
    """Class that initializes all the User attributes.
    """

    # Initialize the User profile with basic attributes.
    def __init__(self, name, time, music="basic", project="", task_list=None):
        """Initializes the user profile.

        Args:
            name (str): Name of the user.
            time (int): Number of seconds the user has been in work and break mode..
            music (list, optional): Type of music the user listens to. Defaults to "basic".
            task_list (list, optional): List of tasks the user has created. Defaults to [].
        """
        if task_list is None:
            task_list = []
        self.name = name
        self.time_completed = time
        self.music = music
        self.project_name = project
        self.task_list = task_list

    # Define a function to add tasks to the list.
    def add_task(self, task):
        """Add a task to the list of tasks the user owns. Cannot have an underscore in its description.

        Args:
            task (str): Task the user has created.

        Returns:
            str: Error message stating that the task is invalid.
        """

        # Check that there are no invalid characters.
        if "_" in task:
            # TODO GUI: Add popup that tells user that the task is invalid because of `_`.
            print("TASK IS INVALID")
            return "ERROR 001: INVALID TASK"

        # If valid, create the task.
        else:
            # Format: "Number: Task Name, Completion Status, Tags"
            self.task_list.append([task, "incomplete", "none"])

    # Define a function to remove tasks.
    def delete_task(self, task_num):
        """Delete a task the user has created.

        Args:
            task_num (str, int): Number of the task the user wishes to delete.
            
        Returns:
            str: Message stating whether the task was found or not.
        """

       # Delete the task, if it exists.
        try:
            del self.task_list[task_num - 1]

        # Report an error if the task was not found.
        except IndexError:
            print('ERROR: Task could not be found')
            # TODO GUI: Add a popup when error is formed.
            return 'ERROR 002: TASK NOT FOUND'
        
    # Define a function to add tasks to the list.
    def insert_task(self, task_num, place):
        """Insert a task in list of tasks the user owns to another position.

        Args:
            task_num (num): Number of the task to be moved.
            
            place (num): New position of the task.

        Returns:
            str: Error message stating that the task was not found.
        """

        # Check that there is such a task.
        if (len(self.task_list) < task_num) or (task_num <= 0):
            # TODO GUI: Add popup that tells user that the task is invalid because of `_`.
            print("TASK NOT FOUND")
            print(task_num, len(self.task_list))
            return "ERROR 009: TASK NOT FOUND"

        # If valid, insert the task.
        else:
            # Format: "Number: Task Name, Completion Status, Tags"
            
            # Get the task information.
            task = self.task_list[task_num-1][0]
            status = self.task_list[task_num-1][1]
            tags = self.task_list[task_num-1][2]
            
            # Insert the task.
            if place - 1 > -1:
                self.delete_task(task_num)
                self.task_list.insert(place - 1, [task, status, tags])

    # Create a list of tasks based off the values in `task_list.csv`.
    def create_tasks_list(self):
        """Creates the list of tasks from the previous session.
        """

        # Define the new list from previously stored data.
        try:
            tasks_list = csv_data.pull_csv_data("task_list.csv", 0, "tasks", 1)

        # If the list is empty, create a blank list.
        except IndexError:
            tasks_list = []

        # Ensure that tasks_list is not empty.
        if tasks_list == ' ':
            tasks_list = []

        # FORMAT: [ ["task_number", "task_name", "task_status", "tags"], [repeat for new task] ]

        # Check if tasks_list is empty.
        if len(tasks_list) == 0:
            pass

        # Continue if tasks_list is not empty.
        else:
            # Split task_list into separate components.
            tasks_list = tasks_list.split("_")  # type: ignore

            # Delete empty tasks.
            for task in tasks_list:
                if task == '':
                    tasks_list.remove(task)

            # Divide the tasks into groups of three.
            grouped_tasks = [tasks_list[i:i + 3] for i in range(0, len(tasks_list), 3)]

            # Add the grouped tasks to the User's task list.
            self.task_list = grouped_tasks

    # Define a function to return the type of music the user enjoys.
    def music_type(self):
        """Return the type of music the user enjoys listening to.

        Returns:
            str: Type of music the user listens to.
        """
        return self.music


# Define a function to initiate a new user to the application.
def initiate_user():
    """Initiates the user with their name, music preference, and base stats from previous sessions.
    """

    # Use the attributes to create a global User class.
    global user
    
    name = csv_data.pull_csv_data('user_data.csv', 0, "name", 1)
    time_complete = int(csv_data.pull_csv_data('user_data.csv', 0, "totalTime", 1))
    music = csv_data.pull_csv_data('user_data.csv', 0, "music", 1)
    project_name = csv_data.pull_csv_data('user_data.csv', 0, "project", 1)

    # Create the user class with base stats.
    user = User(name, time_complete, music, project_name, [])
    user.create_tasks_list()

    csv_data.rewrite_csv_data("user_data.csv", [f"name,{name}", f"totalTime,{time_complete}", f"music,{music}", f"project,{project_name}"], '\n')


# Define a function to store the user data when closing the app.
def store_data(user_class):

    # Find the user values for `vals.csv`.
    name = user_class.name
    time_complete = user_class.time_completed
    music = user_class.music
    project_name = user_class.project_name

    # Write the user values to `vals.csv`.
    csv_data.rewrite_csv_data('user_data.csv', [f"name,{name}", f"totalTime,{time_complete}", f"music,{music}", f"project,{project_name}"], '\n')

    # Prepare the tasks to be added to `task_list.csv`.
    all_tasks = ['tasks,']
    for task in user_class.task_list:
        #print(task)
        for section in task:
            #print(section)
            all_tasks.append(f"{section}")

    # Write all tasks down in `task_list.csv`.
    csv_data.rewrite_csv_data("task_list.csv", all_tasks, "_")
