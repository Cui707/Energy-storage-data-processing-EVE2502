import os
import shutil

def copy_files_to_subdirectories(directory):
    """将文件名包含CyxCsvData、ESDC、ESDP的文件复制到每个末级子目录"""
    target_files = ['CyxCsvData', 'ESDC', 'ESDP']
    
    # 获取当前目录中的所有文件
    files_to_copy = [file for file in os.listdir(directory) if any(target in file for target in target_files)]
    
    # 获取脚本所在目录的末级子目录
    for root, dirs, _ in os.walk(directory):
        if not dirs:  # 只处理末级子目录
            for file in files_to_copy:
                file_path = os.path.join(directory, file)
                shutil.copy(file_path, root)  # 复制文件到末级子目录
                print(f"复制文件: {file} 到 {root}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在目录
    
    # 步骤1: 将文件名包括CyxCsvData、ESDC、ESDP的文件复制到每个末级子目录
    copy_files_to_subdirectories(script_dir)

if __name__ == "__main__":
    main()
