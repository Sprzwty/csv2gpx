# CSV to GPX Converter

## 简介
这是一个Python程序，能够将CSV格式的轨迹数据转换为GPX格式。它使用了`tkinter`库来选择输入和输出文件，并将转换逻辑封装在一个单独的模块中。

## Introduction
This is a Python program that converts track data from CSV format to GPX format. It uses the `tkinter` library to select input and output files, and the conversion logic is encapsulated in a separate module.

## 功能 / Features
- 从CSV文件导入轨迹数据
- 将轨迹数据转换为GPX格式
- 选择输入和输出文件位置

- Import track data from CSV file
- Convert track data to GPX format
- Choose input and output file locations

## 安装 / Installation
1. 确保已安装Python环境。
2. 克隆或下载此仓库。
3. 使用以下命令安装必要的库：
   
   ```bash
   pip install tkinter
   ```

1. Ensure that Python is installed.
2. Clone or download this repository.
3. Install the required libraries using the following command:

   ```bash
   pip install tkinter
   ```

## 使用 / Usage

### CSV 文件格式 / CSV File Format
CSV文件应具有以下格式：

The CSV file should have the following format:

```csv
dataTime,locType,longitude,latitude,heading,accuracy,speed,distance,isBackForeground,stepType,altitude
1696956048,1,136.594342,36.443043,0.000000,83.470119,0.001424,311.631844,0,0,0.000000
1696925162,1,136.594405,36.443245,0.000000,35.000000,0.000000,0.000000,0,1,137.476021
...
```

### 转换程序 / Conversion Program

#### 步骤 / Steps
在PyCharm中运行`main.py`文件，选择输入和输出文件位置。

Run the `main.py` file in PyCharm and select the input and output file locations.

## 许可证 / License
该项目使用MIT许可证。详情请参见`LICENSE`文件。

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 贡献 / Contributing
欢迎任何形式的贡献。请先提交问题或拉取请求。

Contributions are welcome. Please open an issue or submit a pull request.
