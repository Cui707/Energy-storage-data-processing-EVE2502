import os
import subprocess
import time
import glob

# 定义文件名模式
esdp_pattern = '*ESDP*.py'
esdc_pattern = '*ESDC*.py'
system_data_file = 'SystemData.xlsx'

# 查找符合模式的文件
def find_program(pattern):
    matching_files = glob.glob(pattern)
    if not matching_files:
        raise FileNotFoundError(f"未找到匹配的文件: {pattern}")
    return matching_files[0]  # 返回第一个匹配的文件

# 执行程序
def run_program(program_name):
    print(f"正在执行程序: {program_name}...")
    subprocess.run(['python', program_name], check=True)

# 等待SystemData.xlsx文件生成
def wait_for_system_data():
    print("等待SystemData.xlsx文件生成...")
    while not os.path.exists(system_data_file):
        time.sleep(1)  # 每秒钟检查一次文件是否生成

# 主流程
def main():
    try:
        # 查找ESDP和ESDC程序
        esdp_program = find_program(esdp_pattern)
        esdc_program = find_program(esdc_pattern)

        # 执行ESDP程序
        run_program(esdp_program)

        # 等待SystemData.xlsx文件生成
        wait_for_system_data()

        # 执行ESDC程序
        run_program(esdc_program)

        print("流程执行完毕。")
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"程序执行出错: {e}")

if __name__ == "__main__":
    main()
