# Task 1: You are given a source code file of a specific programming language. 
# You have to calculate the SLOC (only source line of code without comment) 
# of that file.

#This script reads a .rs file and removes single line and multiline comments 
#and new lines. then counts the number of lines to calculate the SLOC
#The user can give any other files through the command line e.g. python task1.py -f <filename.rs>
#If no file name is specified then it runs on the default file test.rs

#Nazmus Sakib Ahmed
#BSSE1108 

import re

def remove_comments(input_text):
    # Regular expression to match single-line comments (lines starting with "//")
    single_line_pattern = r'(?m)^\s*//.*$'
    # Replace single-line comments with an empty string
    result = re.sub(single_line_pattern, '', input_text)

    # Regular expression to match block comments (multi-line comments)
    block_comment_pattern = r'/\*.*?\*/'
    # Replace block comments with an empty string
    result = re.sub(block_comment_pattern, '', result, flags=re.DOTALL)

    return result

def read_rust_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def driver(path):
    path=path;
    srcCode=read_rust_file(path);
    commentsRemoved=remove_comments(srcCode)
    splitLines= commentsRemoved.split('\n');
    cleanedLines=[x for x in splitLines if x!='']
    # print(cleanedLines)
    print(len(cleanedLines))


import argparse
parser = argparse.ArgumentParser(description='Count SLOC')
parser.add_argument('-f','--file')
args = parser.parse_args()
path='test.rs'
if args.file:
    path=args.file

driver(path);