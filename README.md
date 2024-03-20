# AdvYOLO: Advanced YOLOv8 Application for Bone Pathology Localization and Classification in Wrist X-ray Images

## Abstract

In the field of pediatric orthopedics, accurate and timely identification of wrist fractures is vital for effective treatment and recovery. Fractures significantly affect daily activities and can lead to long-term health issues. Especially in areas with limited medical resources, or for doctors with less experience, interpreting X-ray images accurately is challenging. This paper introduces the AdvYOLO algorithm, an enhanced version of YOLOv8, trained on the GRAZPEDWRI-DX dataset to diagnose wrist bone pathologies. The integration of the Dilation-wise Residual (DWR) and Large Separable Kernel Attention (LSKA) modules is critical for improving feature extraction and classification, as they allow more effective processing of complex patterns in X-ray images, leading to more accurate diagnostics. The mAP 50 value of AdvYOLO improved from 63.8\% to 68.7\%, achieving state-of-the-art performance in wrist detection. Additionally, the paper presents BoneVisionAI, a tool to assist doctors, particularly those with less experience, in accurately interpreting children's wrist X-rays, aiming to reduce diagnostic errors in the healthcare sector.

## YOLOv8 architecture

![advyolo](https://xiaoxiangge.oss-cn-shanghai.aliyuncs.com/advyolo.jpg)

## Requirements

- Linux (Ubuntu)
- Python = 3.9
- PyTorch 1.8.2

## Environment

```bash
  pip install -r requirements.txt
```

## Dataset

### Dataset Split

- GRAZPEDWRI-DX Dataset [(Download Link)](https://figshare.com/articles/dataset/GRAZPEDWRI-DX/14825193)
- Download dataset and put images and annotatation into `./GRAZPEDWRI-DX_dataset/data/images`, `./GRAZPEDWRI-DX_dataset/data/labels`.

```bash
python ./Fracture_Detection/split.py
```

- The dataset is divided into training, validation, and testing set (70-20-10 %) according to the key `patient_id` stored in `dataset.csv`.

### Data Augmentation

- Data augmentation of the training set using the addWeighted function doubles the size of the training set.

```bash
 python ./Fracture_Detection/imgaug.py
```

The file content is modified to the desired output file path.

### Pre -training model

You can download it through this link [ultralytics/ultralytics: NEW - YOLOv8 🚀 in PyTorch > ONNX > OpenVINO > CoreML > TFLite (github.com)](https://github.com/ultralytics/ultralytics)

### Trained Model

Use gdown to download the trained model from our GitHub:

```bash
gdown https://github.com/Happy-Xiang/AdvYOLO/blob/master/weights/best.pt
```

### Validate 

```bash
python val.py
```

## Experimental Results

| **Algorithms** | **DWR** | **LSKA** | **Optimizer** | **Precision** | **Recall** | **F1** | **map50** | **Params/M** | **GFLOPs** |
| -------------- | ------- | -------- | ------------- | ------------- | ---------- | ------ | --------- | ------------ | ---------- |
| YOLOv8s        | No      | No       | SGD           | 0.768         | 0.579      | 0.660  | 0.608     | 11.1         | 28.7       |
| YOLOv8s        | No      | No       | Adam          | 0.678         | 0.392      | 0.497  | 0.431     | 11.1         | 28.7       |
| YOLOv8s-D      | Yes     | No       | SGD           | 0.84          | 0.539      | 0.657  | 0.642     | 10.8         | 28.3       |
| YOLOv8s-D      | Yes     | No       | Adam          | 0.651         | 0.527      | 0.582  | 0.528     | 10.8         | 28.3       |
| YOLOv8s-L      | No      | Yes      | SGD           | 0.775         | 0.578      | 0.662  | 0.598     | 12.2         | 29.5       |
| YOLOv8s-L      | No      | Yes      | Adam          | 0.694         | 0.491      | 0.575  | 0.524     | 12.2         | 29.5       |
| AdvYOLO        | Yes     | Yes      | SGD           | 0.795         | 0.584      | 0.673  | **0.687** | 11.9         | 29.1       |
| AdvYOLO        | Yes     | Yes      | Adam          | 0.775         | 0.475      | 0.589  | 0.492     | 11.9         | 29.1       |

![image-20240320172738731](https://xiaoxiangge.oss-cn-shanghai.aliyuncs.com/image-20240320172738731.png)

Examples of pediatric wrist fracture detection on X-ray images. (a) manually labeled images, (b) predicted images.

## Application

You can download the corresponding visualization program in this link:

[Happy-Xiang/YOLOv8-PySide6-GUI-camera (github.com)](https://github.com/Happy-Xiang/YOLOv8-PySide6-GUI-camera)

![BoneVisionAl](https://xiaoxiangge.oss-cn-shanghai.aliyuncs.com/BoneVisionAl.jpg)
