import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('/root/AdvYOLO/Fracture_Detection/yolov8s-SPPF-LSKA-DWR.yaml')
    model.load('yolov8s.pt') # loading pretrain weights
    model.train(data='/root/AdvYOLO/Fracture_Detection/bone.yaml',
                cache=False,
                imgsz=1024,
                epochs=100,
                batch=16,
                close_mosaic=10,
                workers=8,
                device='0',
                optimizer='SGD', # using SGD
                # resume='', # last.pt path
                # amp=False # close amp
                # fraction=0.2,
                project='runs/train',
                name='exp',
                )
