


def create_file():
    name=input("Enter the name of the file to create: ")
    with open(name, 'w') as file:
        pass

def add_entry():
    entry=input("Enter the name of the file to add content to: ")
    with open(entry, 'a') as file:
        file.write(entry + '\n')

def read_file():
    name=input("Enter the name of the file to read: ")
    with open(name, 'r') as file:
        print(file.read())

def append_to_file():
    name=input("Enter the name of the file to append content to: ")
    with open(name, 'a') as file:
        file.write(name + '\n')