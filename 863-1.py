# create_folders_and_unzip.py
import os
import zipfile

def unzip_files_in_dir(directory):
    """解压所有压缩文件到相应的目录"""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.zip', '.tar', '.gz')):
                file_path = os.path.join(root, file)
                print(f"解压: {file_path}")
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(root)  # 解压到当前目录

def create_subfolders(directory):
    """在每个子目录中创建两个新文件夹（只创建一次）"""
    for root, dirs, _ in os.walk(directory):
        # 确保只处理顶级子目录，跳过更深的子目录
        if root == directory:  # 判断当前路径是否为脚本所在目录
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                folder_1 = os.path.join(dir_path, dir_name + "(1)")
                folder_2 = os.path.join(dir_path, dir_name + "(2)")

                # 只在顶级子目录中创建文件夹
                if not os.path.exists(folder_1):
                    os.makedirs(folder_1)
                    print(f"创建文件夹: {folder_1}")
                if not os.path.exists(folder_2):
                    os.makedirs(folder_2)
                    print(f"创建文件夹: {folder_2}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在目录
    
    # 步骤1: 解压文件
    unzip_files_in_dir(script_dir)
    
    # 步骤2: 在每个子目录中创建文件夹（只创建一次）
    create_subfolders(script_dir)

if __name__ == "__main__":
    main()
