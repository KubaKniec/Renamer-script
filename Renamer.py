import os


def remove_substring_from_file(file_path, substring):
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist!")
        return

    directory, filename = os.path.split(file_path)
    name, ext = os.path.splitext(filename)

    if substring in name:
        new_name = name.replace(substring, "")
        new_file_path = os.path.join(directory, new_name + ext)
        os.rename(file_path, new_file_path)
        print(f"The file {filename} has been renamed to {new_name + ext}")
    else:
        print(f"The file {filename} does not contain the substring '{substring}', skipping.")


def remove_substring_from_all_files_in_folder(directory, substring):
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist!")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            remove_substring_from_file(file_path, substring)


while True:
    mode = input("Do you want to change (1) a single file or (2) multiple files? (type 'e' to exit): ")

    if mode.lower() == 'e':
        print("Program terminated.")
        break

    if mode == '1':
        file_path = input("Enter the full path to the file: ")
        substring = input("Enter the substring you want to remove from the file name: ")
        remove_substring_from_file(file_path, substring)

    elif mode == '2':
        directory = input("Enter the folder path: ")
        substring = input("Enter the substring you want to remove from file names: ")
        remove_substring_from_all_files_in_folder(directory, substring)

    else:
        print("Invalid option. Please type '1', '2', or 'e'.")
