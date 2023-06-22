# listed all windows files
# be sure you downloading the file from :   https://github.com/anrsaad

import os

print("wait for writing files link into file_link.txt ... ")
def list_files(directory):
    with open('file_link.txt', 'w') as file:
        for root, dirs, files in os.walk(directory):
            for file_name in files:
               file_path = os.path.join(root, file_name)
               file_size = os.path.getsize(file_path)
               file.write(f"{file_path} - {file_size} bytes\n")

directory = 'C:\\'  # Replace path with directory you want to search files
list_files(directory)
