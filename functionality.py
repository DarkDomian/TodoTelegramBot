help = """
help - display a list of available commands and ther function
add - add a task to the list
show -  display all tasks
exit - stop the program"""

today = []
tomorrow = []
other = []

while True:
  command = input("Write a command: ")
  if command == "help":
    print(help)
  elif command == "show":
    print(today, tomorrow, other)
  elif command == "add":
    date = input("Wrate the date: ")
    task = input("Write a task: ")
    if date == 'today':
      today.append(task)
    elif date == 'tomorrow':
      tomorrow.append(task)
    else:
      other.append(task)
    print(f'Your task {task} has been added')
  elif command == "exit":
    break
  else:
    print("there is no such command, but we are working on it")

