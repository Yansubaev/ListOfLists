from itertools import chain


def read_list():
    try:
        return list(map(int, input().split()))
    except ValueError:
        print("The line contains not numbers, stop reading input")


def append_to_list(where_to, what_to):
    if what_to is not None:
        where_to.append(what_to)
        return True


print("Enter list items in a line, separated by a space.\nTo enter the following list, press enter. "
      "\nTo stop recording, enter any character (not a number)")
general = []
a = read_list()
while append_to_list(general, a):
    a = read_list()
b = sorted(list(chain(*general)), reverse=True)
print(b)
