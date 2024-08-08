import tkinter as tk
from tkinter import filedialog
import csv2gpx


def select_file():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename(title="选择CSV文件", filetypes=[("CSV files", "*.csv")])
    return file_path


def save_file():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    file_path = filedialog.asksaveasfilename(title="保存GPX文件", defaultextension=".gpx",
                                             filetypes=[("GPX files", "*.gpx")])
    return file_path


def main():
    input_file = select_file()
    if not input_file:
        print("未选择输入文件")
        return

    output_file = save_file()
    if not output_file:
        print("未选择输出文件")
        return

    csv2gpx.csv2gpx(input_file, output_file)
    print(f"转换完成：{output_file}")


if __name__ == "__main__":
    main()
