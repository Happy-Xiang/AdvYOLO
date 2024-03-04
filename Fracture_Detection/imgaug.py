# import os
# import cv2
# import numpy as np
#
# imgdir = "../data/images/"
# # labeldir = "../labels/"
#
# for root, dirs, files in os.walk(imgdir):
#     for name in files:
#         img_name = os.path.join(name)
#         print(img_name)
#         pic = cv2.imread(imgdir + img_name)
#         contrast = 1.2
#         brightness = 30
#         pic_turn = cv2.addWeighted(pic, contrast, pic, 0, brightness)
#         cv2.imwrite(imgdir + 'aug_' + img_name, pic_turn)
#         # cv2.imshow('original', pic)
#         # cv2.imshow('turn', pic_turn)
#         cv2.waitKey(0)

import os
import cv2
import numpy as np

imgdir = "/root/autodl-tmp/GRAZPEDWRI-DX_dataset/data/images/train_aug/"
labeldir = "/root/autodl-tmp/GRAZPEDWRI-DX_dataset/data/labels/train_aug/"  # Assuming labels are in a separate directory

for root, dirs, files in os.walk(imgdir):
    for name in files:
        img_name = os.path.join(name)
        label_name = os.path.splitext(name)[0] + ".txt"  # Assuming label files have same name with .txt extension

        # Image processing
        pic = cv2.imread(os.path.join(imgdir, img_name))
        contrast = 1.2
        brightness = 30
        pic_turn = cv2.addWeighted(pic, contrast, pic, 0, brightness)
        cv2.imwrite(os.path.join(imgdir, 'aug_' + img_name), pic_turn)

        # Label processing
        label_path = os.path.join(labeldir, label_name)
        with open(label_path, 'r') as label_file:
            label_data = label_file.read()

        # Modify label_data as needed based on image augmentation

        new_label_path = os.path.join(labeldir, 'aug_' + label_name)
        with open(new_label_path, 'w') as new_label_file:
            new_label_file.write(label_data)
