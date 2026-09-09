# this script organizes files in a given directory by their file extension or by the first letter of their name.

import os
import shutil

def organize(directory, organize_by_extension):
    # organize by either name or extension depending whether organize_by_extension is True or False
    if organize_by_extension:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                extension = os.path.splitext(filename)[1][1:]  # get the file extension without the dot
                if extension:  # check if the file has an extension
                    extension_folder = os.path.join(directory, extension)
                    if not os.path.exists(extension_folder):
                        os.makedirs(extension_folder)
                    shutil.move(os.path.join(directory, filename), os.path.join(extension_folder, filename))
    else:
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                first_letter = filename[0].upper()  # get the first letter of the filename and convert to uppercase
                letter_folder = os.path.join(directory, first_letter)
                if not os.path.exists(letter_folder):
                    os.makedirs(letter_folder)
                shutil.move(os.path.join(directory, filename), os.path.join(letter_folder, filename))

def input_directory():
    return input("enter the directory path to organize: ")

def input_organize_by_extension():
    choice = input("Do you want to organize by file extension? (y/n): ")
    return choice.lower() == 'y'

def main():
    directory = input_directory()
    organize_by_extension = input_organize_by_extension()
    if os.path.exists(directory) and os.path.isdir(directory):
        organize(directory, organize_by_extension)
        print("files have been organized.")
    else:
        print("invalid directory path.")

if __name__ == "__main__":
    main()