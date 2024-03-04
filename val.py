import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/train/exp/weights/best.pt')
    model.val(data='dataset/data.yaml',
              split='val',
              batch=16,
            #   save_json=True, # if you need to cal coco metrice
              project='runs/val',
              name='exp',
              )