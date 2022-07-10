help = """
help - display a list of available commands and ther function
add - add a task to the list
show -  display all tasks
exit - stop the program"""

todolist = {
  "today": [],
  "tomorrow": [],
  "other": {}
}

while True:
  command = input("Write a command: ")
  if command == "help":
    print(help)
  elif command == "show":
    print(todolist)
  elif command == "add":
    date = input("Wrate the date: ")
    task = input("Write a task: ")
    if date == 'today':
      todolist['today'].append(task)
    elif date == 'tomorrow':
      todolist['tomorrow'].append(task)
    else:
      todolist['other'] = dict(date=task)
      # have some trouble
  elif command == "exit":
    break
  else:
    print("there is no such command, but we are working on it")
  