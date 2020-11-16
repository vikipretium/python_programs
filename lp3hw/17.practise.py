from sys import argv
from os.path import exists

prg_to_run, file1, file2 = argv

print(f"\nprocessing copy from {file1} to {file2}\n")

open_file = open(file1)
read_file = open_file.read()

copy_process = open(file2, 'w')
copy_process.write(read_file)

print("copy success!\n")
open_file.close()
copy_process.close()

print("........Content of the file copied.......\n")
opened = open(file2)
print(opened.read())


