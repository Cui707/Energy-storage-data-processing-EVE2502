import os
import shutil

def classify_files(directory):
    """根据文件名中的数字将表格文件分类"""
    for root, _, files in os.walk(directory):
        for file in files:
            if 'bms' in file and file.endswith(('.xls', '.xlsx', '.csv')):  # 根据文件类型修改
                try:
                    # 提取数字并分类
                    number = int(''.join(filter(str.isdigit, file.split('bms')[1])))  # 提取数字
                    if number < 6:
                        target_folder = os.path.join(root, f"{os.path.basename(root)}(1)")
                    else:
                        target_folder = os.path.join(root, f"{os.path.basename(root)}(2)")

                    # 检查目标文件夹是否存在
                    if os.path.exists(target_folder):  # 如果文件夹存在，进行文件移动
                        shutil.move(os.path.join(root, file), os.path.join(target_folder, file))
                        print(f"已分类: {file} -> {target_folder}")
                    else:
                        print(f"目标文件夹 {target_folder} 不存在，跳过分类")
                except ValueError:
                    print(f"文件名中没有数字: {file}")

def copy_files_to_subdirectories(directory):
    """将文件复制到子目录"""
    for root, _, files in os.walk(directory):
        for file in files:
            if 'bms' in file and file.endswith(('.xls', '.xlsx', '.csv')):  # 根据文件类型修改
                try:
                    # 提取数字并分类
                    number = int(''.join(filter(str.isdigit, file.split('bms')[1])))  # 提取数字
                    if number < 6:
                        target_folder = os.path.join(root, f"{os.path.basename(root)}(1)")
                    else:
                        target_folder = os.path.join(root, f"{os.path.basename(root)}(2)")

                    # 检查目标文件夹是否存在
                    if os.path.exists(target_folder):  # 如果文件夹存在，进行文件复制
                        shutil.copy(os.path.join(root, file), os.path.join(target_folder, file))
                        print(f"已复制: {file} -> {target_folder}")
                    else:
                        print(f"目标文件夹 {target_folder} 不存在，跳过复制")
                except ValueError:
                    print(f"文件名中没有数字: {file}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # 获取脚本所在目录
    classify_files(script_dir)
    copy_files_to_subdirectories(script_dir)

if __name__ == "__main__":
    main()
