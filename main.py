import os


global current_path
current_path = ""
global filename
filename = ""
global original_path
original_path = ""


def delete_file():
    global current_path
    global filename
    global original_path

    out = os.system(f'del "{current_path + filename}"')
    print(f"{out} : {current_path + filename}")
    contents = os.listdir(current_path)

    dir_names = []
    for name in contents:
        if os.path.isdir(current_path + name):
            dir_names.append(name)

    for name in dir_names:
        current_path += name + "\\"
        delete_file()

    current_path = current_path.split("\\")
    del current_path[-1]
    del current_path[-1]
    current_path = "\\".join(current_path) + "\\"


current_path = input("Enter the root path > ")
filename = input("Enter the filename to delete > ")
original_path = current_path

delete_file()
