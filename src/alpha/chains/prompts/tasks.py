system_template = """
Create a python list of task objects where task objects are python dictionaries

Consider the tasks by looking at the system inputs 

{system_inputs}

Make sure the output is stritly in Python list of JSON objects
"""

human_template = """
Create a list for of subtask objects to accomplish the instruction.
Don't create any redundant task, only create the needed the high level tasks.

Task objects are python dictionaries having "task_key", "input_key", 
"output_key", "description", "model_type" and "function_name".

"task_key" is the unique name for the task
"input_key" is the list of "task_key" of tasks that the task expects input from. If the input is directly coming from the user, "input_key" is "user"
"output_key" is the output of the model. If the output is given to user, make output_key as user
"description" is the detailed description of what the task does. It includes inputs and outputs of the task
"model_type" is either "ui" or "ai" depending on the functionality of the task
"function_name": is the function name which will be generated to accomplish that task

##########################
Instruction:{instruction}
##########################
List of Task objects:
"""