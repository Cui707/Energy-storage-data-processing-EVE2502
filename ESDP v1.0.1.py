import pandas as pd
import os

# 获取当前脚本所在的文件夹路径
folder_path = os.path.dirname(os.path.abspath(__file__))

# 显式设置当前工作目录为脚本所在的目录
os.chdir(folder_path)  # 确保当前工作目录设置为脚本所在的目录

# 创建一个空的 DataFrame 用于汇总所有数据
total_data = pd.DataFrame()

# 定义我们需要提取的列名关键字
keywords = [
    'occurTime', 'bms_maxU_', 'bms_minU_', 'bms_mdMaxT_','bms_maxT_',
    'bms_i_', 'bms_totalChargeKwh_', 'bms_totalDischargeKwh_',
    'bms_thisChargeKwh_','bms_thislChargeKwh_','bms_thisDischargeKwh_'
]

# 初始化一个字典用于存储不同列类型的数据
columns_by_type = {key: [] for key in keywords}

# 查找符合条件的文件（包含 'bms' 且以 .csv 结尾的文件）
bms_files = [file_name for file_name in os.listdir(folder_path) 
             if 'bms' in file_name and file_name.endswith('.csv')]

# 判断文件数量
num_files = len(bms_files)

if num_files == 0:
    print("没有找到符合条件的文件！")
else:
    print(f"找到 {num_files} 个符合条件的文件。")

    # 遍历所有符合条件的文件进行处理
    for idx, file_name in enumerate(sorted(bms_files), 1):  # 按顺序处理文件，确保文件顺序正确
        file_path = os.path.join(folder_path, file_name)
        
        if os.path.exists(file_path):  # 确保文件存在
            # 读取 CSV 文件
            df = pd.read_csv(file_path)

            # 提取每一类列，并按文件顺序命名
            for keyword in keywords:
                # 使用正则表达式匹配包含关键字的列
                matched_columns = df.filter(regex=keyword)

                # 为每个列添加精简后的列名（例如 bms1_maxU, bms2_occurTime 等）
                for col in matched_columns.columns:
                    # 使用文件的顺序来生成列名（bms1, bms2, ...）
                    new_col_name = f'bms{idx}_{col.split("_")[1]}' if len(col.split("_")) > 1 else f'bms{idx}_{col}'

                    matched_columns.rename(columns={col: new_col_name}, inplace=True)

                # 将当前文件的匹配列添加到对应列类型的列表中
                columns_by_type[keyword].append(matched_columns)

    # 合并每一类列，并在列之间插入空白列
    for key, columns_list in columns_by_type.items():
        # 将所有相同类型的列按列拼接在一起
        concatenated_columns = pd.concat(columns_list, axis=1)

        # 插入1列空白列
        empty_columns = pd.DataFrame(columns=[f'empty_{i}' for i in range(1, 2)], index=concatenated_columns.index)
        concatenated_columns = pd.concat([concatenated_columns, empty_columns], axis=1)

        # 将合并后的列添加到 total_data 中
        total_data = pd.concat([total_data, concatenated_columns], axis=1)

    # 自动命名生成的文件为 "SystemData.xlsx"
    output_file_name = "SystemData.xlsx"

    # 生成完整的文件路径
    total_file_path = os.path.join(folder_path, output_file_name)

    # 将汇总结果写入 Excel 文件
    total_data.to_excel(total_file_path, index=False)

    print(f'所有数据已成功汇总并写入 {total_file_path}')
