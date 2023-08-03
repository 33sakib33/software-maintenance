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

def driver():
    path="test.rs";
    srcCode=read_rust_file(path);
    commentsRemoved=remove_comments(srcCode)
    splitLines= commentsRemoved.split('\n');
    cleanedLines=[x for x in splitLines if x!='']
    print(cleanedLines)
    print(len(cleanedLines))

driver();