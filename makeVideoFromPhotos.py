#WIP - this still doesn't work

import cv2
import numpy as np
import glob

frameSize = (480, 640)

out = cv2.VideoWriter('output_video.avi',cv2.VideoWriter_fourcc(*'MJPG'), 30, frameSize)

for filename in glob.glob('*.jpg'):
    for _ in range(30):
        print(filename)
        img = cv2.imread(filename)
        cv2.imshow("Output",img)
        cv2.waitKey(1)
        out.write(img)

out.release()