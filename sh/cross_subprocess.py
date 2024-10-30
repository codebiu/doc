# ANSI 转义序列F
class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'    
class console:
    '''带颜色输出'''
    # 静态方法
    @staticmethod
    def error(message,*other):
        print(Color.RED + message + Color.RESET,*other) 
    @staticmethod
    def exception(message,*other):
        print(Color.RED + message + Color.RESET,*other)
    @staticmethod
    def log(message,*other):
        print(Color.GREEN + message + Color.RESET,*other)

# 语言编码
import locale
default_locale = locale.getdefaultlocale()
is_chinese_user = default_locale[0] == 'zh' or 'zh_CN'
def select(zh,en):
    return zh if is_chinese_user else en
console.log(select('默认语言编码设置:','default_locale' ),default_locale)

#  Linux命令与Windows命令
import os
import subprocess
# 定义Linux命令与Windows命令的对应表
command_mapping = {
    'ls': 'dir',
    'pwd': 'cd',
    'cat': 'type',
    'cp': 'copy',
    'mv': 'move',
    'rm': 'del',
    'mkdir': 'mkdir',
    'rmdir': 'rmdir',
    'touch': 'type nul >',  # 这个命令需要单独处理
}

def translate_command(linux_command):
    """将Linux命令转换为Windows命令"""
    commands = linux_command.split()
    windows_command = []

    for cmd in commands:
        if cmd in command_mapping:
            windows_command.append(command_mapping[cmd])
        else:
            windows_command.append(cmd)

    return ' '.join(windows_command)

def run_command(linux_command):
    """根据操作系统执行对应的命令"""
    # # Unix-like (Linux, macOS)
    command = linux_command
    
    # Windows
    if os.name == 'nt':  
        command = translate_command(linux_command)
        console.log(select('系统:','sys:'),'windows')
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        console.log(select('控制输出:','Command Output:'))
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        console.error(f"Command '{e.cmd}' failed with error code {e.returncode}")
        console.error("Error Output:")
        console.error(e.stderr)

if __name__ == "__main__":
    # 示例：执行Linux命令
    # linux_command = input("Enter a Linux command: ")
    # run_command(linux_command)
    run_command('ls')
