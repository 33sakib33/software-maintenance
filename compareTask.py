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

    
    
    return '\n'.join(diff)



import os

def find_rs_files(folder_path):
    rs_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.rs'):
                rs_files.append(os.path.join(root, file))
    return rs_files




def read_rust_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return content

def driver():
    path1="test.rs";
    path2="test2.rs";
    # srcCode1=read_rust_file(path);
    # srcCode2=read_rust_file(path);
    prev=path1;
    new=path2;
    df=compare_rust_files(prev,new)
    from pprint import pprint
    pprint(df)
    folderPath1="repo\rust-practice"
    folderPath2="prevCommit\rust-practice"
    with open ('differences.diff', 'w') as file:  
        file.write(prev + "and" + new)
        file.writelines(df)    

driver();
def find_nth_character(input_string, character, n):
    found_indices = []
    start_index = 0

    for _ in range(n):
        next_occurrence_index = input_string.find(character, start_index)
        if next_occurrence_index != -1:
            found_indices.append(next_occurrence_index)
            start_index = next_occurrence_index + 1
        else:
            break

    return found_indices
def compareAndWrite(prev,new,num):
    df=compare_rust_files(prev,new)
    # idx1=find_nth_character(prev,'\\',2)
    # idx2=find_nth_character(prev,'\\',3)
    # last_backslash_index = prev.rfind("\\")
    # print(idx1[0])
    # print(idx2[0])
    # name=prev[idx1[0]:idx2[0]]
    # print(name)
    path1='changes'+str(num)+'.diff'
    path1="diffFolder"+"\\"+path1
    with open( path1, 'w') as file:  
        file.writelines(df)    

def pathList():
    folderPath1="repo\\rust-practice\\"
    folderPath2="prevCommit\\rust-practice\\"
    rs_filesNew = find_rs_files(folderPath1)
    rs_filesPrev = find_rs_files(folderPath1)
    return rs_filesNew, rs_filesPrev

def driver3():
    new,old=pathList();
    num=0;
    for fn,fo in zip(new,old):
        print(fn)
        print(fo)
        compareAndWrite(fo,fn,num);
        num+=1;
        


# driver3()