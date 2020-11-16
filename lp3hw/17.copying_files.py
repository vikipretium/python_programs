# copying files
# exercise more files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

opened_file = open(from_file)
file_data = opened_file.read()

copy_file = open(to_file, 'w')
copy_file.write(file_data)

print("Copied")

copy_file.close()
opened_file.close()


