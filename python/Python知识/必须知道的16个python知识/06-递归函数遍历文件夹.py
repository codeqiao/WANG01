# 目的： 使用递归函数遍历文件夹

from ipaddress import ip_address

import os
def list_file_or_folder(path_name):
    for path in os.listdir(path_name):
        print(f"{path_name}:{path}")
        temp_path_name = f"{path_name}/{path}"
        if os.path.isdir(temp_path_name):
            # os.path.isdir(参数) 这个参数必须是绝对路径
            list_file_or_folder(temp_path_name)

list_file_or_folder(".")