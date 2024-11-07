FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Reads a text file and returns the list of
    to-do items.
    :param filepath: text file
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do items to the text file.
    :param todos_arg: to-do items
    :param filepath: text file
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
