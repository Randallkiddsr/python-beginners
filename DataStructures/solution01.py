#!/usr/bin/env python3
def prompt_for_to_do():
    return input("Enter a task for your "
        + "to-do list. Press <enter> when done: ")

todos = []
todo = prompt_for_to_do()

while len(todo) > 0:
    todos.append(todo)
    todo = prompt_for_to_do()

print("\nYour To-Do List:")
print("----------------")
for todo in todos:
    print(todo)

print()



