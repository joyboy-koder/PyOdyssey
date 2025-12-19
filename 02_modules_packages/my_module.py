print("Importing my modules...")

test = 'Test String'

def find_index(toSearch, target):
    for i, value in enumerate(toSearch):
        if value == target:
            return i
    return -1