[toc]

# Energy-storage-file-processing-EVE2502
    用于储能系统数据分析工作。将多个电池簇的原始数据文件中的关键信息提取出来，整合到一个新的表格文件。

## ESDP

### 脚本作用：

    将多个电池簇的原始数据文件中的关键信息提取出来，整合到一个新的表格文件。

### 使用方式：

    将BMS数据源文件修改文件名，格式为bms+数字（簇编号），如第一簇的数据就改成“bms1.csv”，可以有其他的字符，但是必须包含“bms”和数字，如“12345_bms1_abc.csv”也是可以的。

    将所有的数据原始文件与此脚本放到同一个文件夹下。
    
    执行脚本，即可在同一文件夹下生成整合后的表格文件“SystemData.xlsx”。

### 自定义：

    ①
    "keywords = ['xxx','xxx']"处，修改单引号内关键词可修改需要提取的列名关键字。

    ②
    # 查找符合条件的文件（包含 'bms' 且以 .csv 结尾的文件）
    bms_files = [file_name for file_name in os.listdir(folder_path) 
             if 'bms' in file_name and file_name.endswith('.csv')]
             
    此处修改中括号内bms和.csv，可以自定义符合条件的文件特征。
    
    ③
    output_file_name = "SystemData.xlsx"

    此处修改引号内的内容，自定义生成的新文件名称。

## ESDC

### 脚本作用：

        处理相同路径下的SystemData.xlsx文件，添加sysMaxU、sysMinU、MaxDiff、sysMaxT、DayTotalChargeKwh、DayTotalDischargeKwh列，并计算赋值。
    在当前目录生成新文件，文件名为当前文件夹名字.xlsx。

### 使用方法：

    同一目录下有SystemData.xlsx文件时，执行此脚本会对其部分内容做计算，文件内添加新的列展示计算结果并标红。修改后的文件在当前目录下另存为新文件，文件名为当前文件夹名字.xlsx。

## CyxCsvData

### 脚本作用：

    自动化按顺序执行ESDP和ESDC程序。

### 使用方法：

    将CyxCsvData和ESDP、ESDC程序放在同一目录下，执行CyxCsvData程序即可自动化按顺序执行ESDP和ESDC程序。

## 863系列脚本

### 脚本作用：

    普通处理文件只需使用ESDP和ESDC脚本，863系列脚本针对性用于处理863站系统为两分支设计，但合适场景下也可以提高处理其他系统数据的效率。

    863-1的作用为，解压子目录中的全部压缩包及创建两个分支文件夹。
    
    863-2的作用为将十个簇文件分类，并移动到对应的分支文件夹中。
    
    863-3的作用为将文件名包含CyxCsvData、ESDC、ESDP的文件复制到每个分支文件夹。 
    
### 使用方法：

    解压系统级压缩包，将863系列的3个脚本，以及'CyxCsvData', 'ESDC', 'ESDP'三个脚本，都放在解压出来的文件夹中。然后按顺序执行863的3个脚本，再到每一个分支文件夹中手动执行CyxCsvData程序。

