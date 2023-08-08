# Task 3: You will be given two versions of source code repository
# (two folders which contain source code at two different versions). 
# You have to identify which files have been 
# changed and calculate the number of changes 
# (addition, deletion, total changes).

# This script walks through the files in the repo and the prevCommit folders
# and finds .rs files with the same name and folder path. Then it compares them to 
# find the additions, deletions and total changes. These values and the details 
# are stored in the diffFolder<timestamp> folder with the same name as the files
# that were compared

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
    
    print(retArr)
    # from pprint import pprint
    # pprint("".join(diff))
    return retArr


def generateInsights(differences):
    
    additions=[x for x in differences if x[0]=='+']
    # print(additions)
    #removing 1 because the file itself is counted.
    addStr="Additions: "+ str(len(additions)-1);
    countAdd=len(additions)-1
    
    deletions=[x for x in differences if x[0]=='-']
    # print(deletions)
    deleteStr="Deletions: "+(str(len(deletions)-1))
    countDel=len(deleteStr)-1
   

    totalChanges=len(additions)+len(deletions)-2;
    totChangeStr="Total Changes: " +str((totalChanges));
    countTot=totalChanges
  
    return addStr,countAdd,deleteStr,countDel,totChangeStr,countTot

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


def find_nth_backslash(input_string, n):
    start_index = 0
    count = 0

    while count < n:
        occurrence_index = input_string.find("\\", start_index)
        if occurrence_index == -1:
            break
        count += 1
        if count == n:
            return occurrence_index
        start_index = occurrence_index + 1

    return -1

def compareAndWrite(prev,new,name,dest):

    differences=compare_rust_files(prev,new)
    added,addedCount,deleted,deletedCount,totChanges,totCount=generateInsights(differences)
    # print(totChanges)
    # idx1=find_nth_backslash(prev,2)
    # idx2=find_nth_backslash(prev,3)

    # name=prev[idx1+1:idx2]
    # print(name)
    last_idx= name.rfind("\\")
  

   
    path1=name[last_idx+1:-3]+'.diff'
    path1=dest+"\\"+path1
    
    
    if totCount>0:
        with open( path1, 'w') as file:  
            file.writelines(added+"; "+ deleted + "; " + totChanges +"\n")  
            file.writelines("".join(differences))     
    
        

def pathList():
    folderPath1="repo\\"
    folderPath2="prevCommit\\"
    rs_filesNew = find_rs_files(folderPath1)
    rs_filesPrev = find_rs_files(folderPath2)
    rs_filesNew= [x[5:] for x in rs_filesNew ]
    rs_filesPrev=[x[11:] for x in rs_filesPrev]
    return rs_filesNew, rs_filesPrev

def create_file_path_dictionary(file_paths):
    import os
    file_path_dict = {
        
    }
   
    for file_path in file_paths:
        # file_name = os.path.basename(file_path)
        idx1=find_nth_backslash(file_path,3)+1
        print(str(file_path))
        if str(file_path) in file_path_dict:
            file_path_dict[str(file_path)] = 2
        else:
            file_path_dict[str(file_path)] = 1
    
    return file_path_dict



def driver3():
    new,old=pathList();
    total=new.copy()
    total.extend(old)
    print(new)
    dc=create_file_path_dictionary(total)
    print(dc)
    # print(new)
    # print(old)
    import datetime
    current_timestamp = int(datetime.datetime.now().timestamp())
    destPath="diffFolder"+str(current_timestamp)
    os.mkdir(destPath)
    for key in dc:
        if dc[key]>1:
            print(key)
            compareAndWrite(os.path.join("repo",key),os.path.join("prevCommit",key),key,destPath);

        
        
driver3()