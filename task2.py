# Task 2: You will be given two versions of a source code file.
# You have to identify the number of changes
# (addition, deletion, total changes) between these two files.

# This script compares test.rs and test2.rs and outputs the added, deleted
# and total number of changes from first file to the second file. Here the 
# first file is treated as the previous version and the second file is treated
# as the newer version. The 3 values are printed on the terminal and the details
# written on in the differences.diff file.

#Nazmus Sakib Ahmed
#BSSE1108 

import re

import difflib

def compare_rust_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1:
        file1_lines = file1.readlines()

    with open(file2_path, 'r') as file2:
        file2_lines = file2.readlines()

    d = difflib.Differ()
    # diff = (d.compare(file1_lines, file2_lines))
    diff = difflib.unified_diff(file1_lines, file2_lines, fromfile=file1_path, tofile=file2_path)
    retArr=[]
    # return '\n'.join(diff)
    for x in diff:
        retArr.append(x)
        
    return retArr


def read_rust_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def generateInsights(differences):
    
    additions=[x for x in differences if x[0]=='+']
    # print(additions)
    #removing 1 because the file itself is counted.
    addStr="Additions: "+ str(len(additions)-1);
    print(addStr)
    
    deletions=[x for x in differences if x[0]=='-']
    # print(deletions)
    deleteStr="Deletions: "+(str(len(deletions)-1))
    print(deleteStr)

    totalChanges=len(additions)+len(deletions)-2;
    totChangeStr="Total Changes: " +str((totalChanges));
    print(totChangeStr)
    return addStr,deleteStr,totChangeStr
def driver(path1,path2):
    # path1="test.rs";
    # path2="test2.rs";
    # srcCode1=read_rust_file(path);
    # srcCode2=read_rust_file(path);
    prev=path1;
    new=path2;
    differences=compare_rust_files(prev,new)
    from pprint import pprint
    added,deleted,changed=generateInsights(differences)
    
    #Details are written in differences.diff file in this folder
    with open ('differences.diff', 'w') as file:  
        file.writelines(added+"; "+ deleted + "; " + changed +"\n")  
        file.writelines("".join(differences))    

import argparse
parser = argparse.ArgumentParser(description='Count SLOC')
parser.add_argument('-f','--file',nargs='*')

args = parser.parse_args()
# print(args.file)
path1='test.rs'
path2='test2.rs'
if args.file:
    if len(args.file)==2:
        path1=args.file[0]
        path2=args.file[1]

driver(path1,path2);