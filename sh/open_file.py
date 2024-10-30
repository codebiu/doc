import subprocess
import os

def open_files_in_vscode(*file_paths):
    try:
        # 构建命令
        command = ['code', '--reuse-window']
        
        # 检查文件是否存在并添加到命令
        for file_path in file_paths:
            if os.path.exists(file_path):
                command.append(file_path)
            else:
                print(f"File not found: {file_path}")

        # 调用VSCode命令行工具
        subprocess.run(command, check=True)
        print(f'Successfully opened {", ".join(file_paths)} in VSCode.')
    except subprocess.CalledProcessError as e:
        print(f'Failed to open files in VSCode. Error: {e}')
    except FileNotFoundError:
        print("VSCode command line tool 'code' not found. Make sure it's installed and in your PATH.")

# 示例：打开example.txt和test.py
open_files_in_vscode('test.text')
