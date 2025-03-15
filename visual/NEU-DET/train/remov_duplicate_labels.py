#重复标签删除

import os

labels_path = " " #labels路径

for txt_file in os.listdir(labels_path):
    if txt_file.endswith(".txt"):
        file_path = os.path.join(labels_path, txt_file)

        with open(file_path, "r") as f:
            lines = f.readlines()

        # 去重并按行排序（可选）
        unique_lines = sorted(set(lines))

        # 重新写入文件
        with open(file_path, "w") as f:
            f.writelines(unique_lines)

print("处理完成，所有 `.txt` 文件中的重复标签已删除！")
