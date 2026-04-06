import json
import sys
import os
from collections import defaultdict

def build_tree(paths):
    tree = defaultdict(list)
    for path in paths:
        parts = path.strip().split('/')[1:]
        current = tree
        for part in parts[:-1]:
            current = current.setdefault(part, {})
        current[parts[-1]] = None
    return tree

def print_tree(tree, prefix='', is_last=True):
    lines = []
    keys = sorted(tree.keys())
    for i, key in enumerate(keys):
        if i == len(keys) - 1:
            new_prefix = prefix + '    '
            lines.append(f"{prefix}└── {key}")
        else:
            new_prefix = prefix + '│   '
            lines.append(f"{prefix}├── {key}")
        
        if isinstance(tree[key], dict):
            lines.extend(print_tree(tree[key], new_prefix, i == len(keys) - 1))
    return lines

def process_file(input_file):
    with open(input_file) as f:
        paths = f.readlines()
    
    tree = build_tree(paths)
    tree_lines = print_tree(tree)
    
    with open(input_file, 'w') as f:
        f.write('\n'.join(tree_lines))

args = sys.argv
if (len(args) < 4):
    sys.exit(1)

path = args[3]
if(path[-1:] == "/"):
    path = path[:-1]
with open(args[1]) as file:
    content = file.read()
json_data = json.loads(content)
parameter_datas = json_data["parameter"]
target_parameter_root_key = args[2]
result_filedata_list = []
count = 0
for el in parameter_datas:
    v_type = el["type"]
    v_cmd = None
    v_chdir = None
    v_executable = None
    v_path = None
    
    if v_type == "command" or v_type == "shell":
        result_filedata_table = {}
        # Decectory exist check
        if el.get("cmd") != None:
           v_cmd = el.get("cmd")
        if el.get("chdir") != None:
           result_filedata_table["chdir"] = el.get("chdir")
        if el.get("executable") != None:
           result_filedata_table["executable"] = el.get("executable") 
        result_filedata_table["type"] = v_type
        result_filedata_table["cmd"] = v_cmd
        result_filedata_table["stdout"] = '/' +  str(count)+ '/customize/0/stdout.txt'
        result_filedata_table["stderr"] = '/' +  str(count)+ '/customize/0/stderr.txt'
        result_filedata_list.append(result_filedata_table)
        count +=1
                
    if v_type == "file" or v_type == "directory":
        result_filedata_table = {}
        result_filedata_table["type"] = v_type
        result_filedata_table["path"] = el["path"]
        if v_type == "file":
           result_filedata_table["file"] = '/' +  str(count)+ '/customize/0/' + el["path"].replace("\\", "/")
        if v_type == "directory":
           result_filedata_table["file"] = '/' +  str(count)+ '/customize/0/' + el["path"].replace("\\", "/").split('/')[-1] + '.zip'
           result_filedata_table["dircontent"] = '/' +  str(count)+ '/customize/0/dircontent.txt'
           process_file(path + '/' +  str(count)+ '/customize/0/dircontent.txt')
        result_filedata_list.append(result_filedata_table)
        count +=1
result = {}
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))
