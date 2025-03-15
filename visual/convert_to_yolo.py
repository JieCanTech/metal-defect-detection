#将数据集转换为 YOLO 格式

import os
import xml.etree.ElementTree as ET

# 定义类别名称
class_names = [" ", " ", " "]
class_to_id = {name: i for i, name in enumerate(class_names)}

# 设置数据集路径
dataset_path = r" "
images_path = os.path.join(dataset_path, "images")
annotations_path = os.path.join(dataset_path, "annotations")
output_labels_path = os.path.join(dataset_path, "labels")

# 确保 labels 目录存在
os.makedirs(output_labels_path, exist_ok=True)

# 遍历 XML 文件
for xml_file in os.listdir(annotations_path):
    if not xml_file.endswith(".xml"):
        continue

    # 解析 XML
    tree = ET.parse(os.path.join(annotations_path, xml_file))
    root = tree.getroot()

    # 获取图像信息
    filename = root.find("filename").text
    img_width = int(root.find("size/width").text)
    img_height = int(root.find("size/height").text)

    # YOLO 标注数据
    yolo_labels = []

    for obj in root.findall("object"):
        class_name = obj.find("name").text
        if class_name not in class_to_id:
            continue  # 跳过未定义类别

        class_id = class_to_id[class_name]
        bbox = obj.find("bndbox")

        # 提取边界框坐标
        xmin = int(bbox.find("xmin").text)
        ymin = int(bbox.find("ymin").text)
        xmax = int(bbox.find("xmax").text)
        ymax = int(bbox.find("ymax").text)

        # 转换为 YOLO 格式  归一化到 [0,1]
        x_center = (xmin + xmax) / (2.0 * img_width)
        y_center = (ymin + ymax) / (2.0 * img_height)
        width = (xmax - xmin) / img_width
        height = (ymax - ymin) / img_height

        # 生成 YOLO 格式标注
        yolo_labels.append(f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    # 保存 YOLO 格式的 .txt 文件
    yolo_label_file = os.path.join(output_labels_path, xml_file.replace(".xml", ".txt"))
    with open(yolo_label_file, "w") as f:
        f.write("\n".join(yolo_labels))

print(" NEU-DET 标注已转换为 YOLO 格式 ")
