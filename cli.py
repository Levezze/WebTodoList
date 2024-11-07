# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(filepath='files/subfiles/todos.txt', todos_arg=todos)

    elif user_action.startswith('show'):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.capitalize()
            show_list = f"{index + 1}. {item}"
            print(show_list)

    elif user_action.startswith('edit'):
        try:
            edit_number = int(user_action[5:])
            edit_number = edit_number - 1

            todos = functions.get_todos()

            new_todo = input("Enter a new todo item: ")
            todos[edit_number] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            edit_number = int(user_action[9:])
            todos = functions.get_todos()
            index = edit_number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("This command is not valid.")

print("Bye!")
