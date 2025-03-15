# metal-defect-detection
金属表面缺陷检测项目，使用 YOLOv8 进行缺陷识别，适用于智能制造与质量检测。
开发环境：Python 3.12
尝试训练了50轮，每幅图尺寸统一在640*640，批量大小是16
使用的数据集是NEU-DET
只有crazing这个分类的漏检，都是240张，原因可能是特征比较模糊，难以提取。也有可能是crazing分类的与背景比较相近，导致边界比较模糊，比较难识别。
或许可以试试yolo更大的模型，也可以提高分辨率，我把分辨率设置比较低,mixup参数或许可以调高点，mixup适用于边界模糊的特征，mosaic也可以调整，适用于比较小的特征目标
yolo task=detect mode=train model=yolov8n.pt data=dataset.yaml epochs=50 imgsz=640 batch=16
以上是我用的yolo命令
task=detect:检测；model=train:进入训练模式；mdoel=yolov8n.pt这是使用yolo模型，可以换成yolo其他模型更精确。data=dataset.yaml：这是确定数据集的路径和验证数据的路径，dataset.yaml里面编写；epoch=50：训练次数；imgsz=640：图片大小；batch=16是单步训练量，这个根据个人电脑配置来
yolo task=detect mode=predict model=runs/detect/train/weights/best.pt source=
以上是我用来进行测试的yolo命令
model=predict：进行推理的命令；model=runs/detect/train/weights/best.pt：使用训练好的最佳模型；source=：用于检测验证的数据的路径
这一模型如果进行更多的数据集训练，使用更大的yolo版本，是适用于很多场景的不仅仅是工业上的表面检测，动物识别，农业上的检测，比如害虫，果实成熟度等，车辆识别和安全检测也可以，比如有人经过等



如果有合作或者问题咨询请联系：
13052271219@163.com
260119501@qq.com
15262999863
句容市杰璨技术信息咨询
