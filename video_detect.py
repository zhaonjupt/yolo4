#-------------------------------------#
#       调用摄像头检测 capture(0)
#-------------------------------------#
from yolo import YOLO
from PIL import Image
import numpy as np
import cv2
import time
import os
import tensorflow as tf

physical_devices = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)
save_video = True

yolo = YOLO()
# 调用摄像头
video_path = input('Please input the video path:')

if video_path.endswith('.mp4'):
    filename = os.path.split(video_path)[-1]
    video = cv2.VideoCapture(video_path)




    video_frame_cnt = int(video.get(7))
    video_width = int(video.get(3))
    video_height = int(video.get(4))
    video_size = (video_width, video_height)
    video_fps = int(video.get(5))
    # fourcc = video.get(6)
    # print(fourcc)
    # cv2.VideoCaputre(0)获取摄像头视频输入，文件路径则读取已存在的视频文件
    # video.get()
    # 0:当前视频位置，毫秒为单位
    # 3: 视频帧宽度
    # 4: 视频帧高度
    # 5：帧速率
    # 6: fourcc编码码四字字符串
    # 7：视频文件中的帧数
    #fps = 0.0

    if save_video:
         fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
         save_path = './res' + '/' + filename
         print('save_path is: {}'.format(save_path))
         videoWriter = cv2.VideoWriter(save_path, fourcc, video_fps, video_size)
         #videoWriter = cv2.VideoWriter(save_path, fourcc, video_fps, (video_width, video_height))




    for i in range(video_frame_cnt):
        start_time = time.time()
        # 读取某一帧
        ref, frame=video.read()
        # 格式转变，BGRtoRGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 转变成Image
        frame = Image.fromarray(np.uint8(frame))

        # 进行检测
        frame = np.array(yolo.detect_image(frame))

        # RGBtoBGR满足opencv显示格式
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        fps = 1. / (time.time() - start_time)
        #fps  = ( fps + (1./(time.time()-t1)) ) / 2
        print("fps= %.2f"%(fps))
        frame = cv2.putText(frame, "fps= %.2f"%(fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if save_video:
            videoWriter.write(frame)

        cv2.imshow("video",frame)
        c= cv2.waitKey(1) & 0xff
        if c==27:
            video.release()
            break
    videoWriter.release()


else:
    pass
