import csv
import xml.etree.ElementTree as ET
from datetime import datetime


def csv2gpx(csv_file, gpx_file):
    # 创建GPX根元素
    gpx = ET.Element('gpx', version="1.1", creator="csv-to-gpx-converter")

    # 创建一个<trk>元素
    trk = ET.SubElement(gpx, 'trk')

    # 创建一个<name>元素
    name = ET.SubElement(trk, 'name')
    name.text = "CSV to GPX Conversion"

    # 创建一个<trkseg>元素
    trkseg = ET.SubElement(trk, 'trkseg')

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            trkpt = ET.SubElement(trkseg, 'trkpt', lat=row['latitude'], lon=row['longitude'])
            ele = ET.SubElement(trkpt, 'ele')
            ele.text = row['altitude']
            time = ET.SubElement(trkpt, 'time')
            # 将时间戳转换为ISO 8601格式
            time.text = datetime.utcfromtimestamp(int(row['dataTime'])).strftime('%Y-%m-%dT%H:%M:%SZ')
            # 可选：添加速度、准确度等其他信息
            speed = ET.SubElement(trkpt, 'speed')
            speed.text = row['speed']
            accuracy = ET.SubElement(trkpt, 'accuracy')
            accuracy.text = row['accuracy']

    # 创建一个ElementTree对象，并写入GPX文件
    tree = ET.ElementTree(gpx)
    tree.write(gpx_file, encoding='utf-8', xml_declaration=True)
