# Instructions
# Please write a program that for a given folder i.e. (my_folder = r'c:\users') 
# counts all files in it and its subfolders (including their subfolders) and then also computes the total
# space occupied by all those files.
# Please do not flatten the tree structure of folders and files by using a function that walks through the file system,
# instead use i.e. recursion in your implementation to simplify the code.
# List all files in a directory using os.listdir
#####################################""
import os

 
Path = "C://Users//Dell//test"

def get_file_count(directory: str) -> int:
    l1=[0,0]
    for entry in os.scandir(directory):
        if entry.is_file():
            l1=[sum(x) for x in zip(l1, [1,int(os.stat(entry).st_size)])]
        elif entry.is_dir():
            l1=[sum(x) for x in zip(l1, get_file_count(os.path.join(directory, entry.name)))] 
    return l1

l=get_file_count(Path)
print(f'The Number of files in "{os.path.basename(Path)}" : {l[0]} --> {l[1]} bytes in total')