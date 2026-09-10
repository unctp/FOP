# this script organizes files in a given directory by their file extension or by the first letter of their name.

import os
import shutil
from datetime import datetime

def organize(directory, organize_by_extension, organize_by_date):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):

            if organize_by_date:
                file_date = get_file_date(filepath)

                date_folder = os.path.join(directory, file_date)

                if not os.path.exists(date_folder):
                    os.makedirs(date_folder)

                shutil.move(filepath, os.path.join(date_folder, filename))

            elif organize_by_extension:
                extension = os.path.splitext(filename)[1][1:]

                if extension:
                    extension_folder = os.path.join(directory, extension)

                    if not os.path.exists(extension_folder):
                        os.makedirs(extension_folder)

                    shutil.move(filepath, os.path.join(extension_folder, filename))

            else:
                first_letter = filename[0].upper()

                letter_folder = os.path.join(directory, first_letter)

                if not os.path.exists(letter_folder):
                    os.makedirs(letter_folder)

                shutil.move(filepath, os.path.join(letter_folder, filename))

def get_file_date(filepath):
    timestamp = os.path.getmtime(filepath)
    date = datetime.fromtimestamp(timestamp)
    return date.strftime("%-m-%-d-%y")

def input_directory():
    return input("enter the directory path to organize: ")

def input_organize_by_date():
    choice = input("Do you wany to organize by date? (y/n): ")
    return choice.lower() == 'y'

def input_organize_by_extension():
    choice = input("Do you want to organize by file extension? (y/n): ")
    return choice.lower() == 'y'

def main():
    directory = input_directory()
    organize_by_extension = input_organize_by_extension()
    organize_by_date = 'n'
    if organize_by_extension == 'y':

        if os.path.exists(directory) and os.path.isdir(directory):
            organize(directory, organize_by_extension, organize_by_date)
            print("files have been organized.")
        else:
            print("invalid directory path.")
    else:
        organize_by_date = input_organize_by_date()
        if os.path.exists(directory) and os.path.isdir(directory):
            organize(directory, organize_by_extension, organize_by_date)
            print("files have been organized.")
        else:
            print("invalid directory path.")

if __name__ == "__main__":
    main()
