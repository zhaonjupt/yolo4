from yolo import YOLO
from PIL import Image
import tensorflow as tf
import os

physical_devices = tf.config.experimental.list_physical_devices(device_type='GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

yolo = YOLO()

while True:
    img = input('Input image filename:')
    filename = os.path.split(img)[-1]
    save_path = './res' + '/' + filename
    try:
        image = Image.open(img)
        print("read successfully!!!")


    except:
        print('Open Error! Try again!')
        continue

    r_image = yolo.detect_image(image)
    r_image.show()
    try:
        r_image.save(save_path)
        print("The result has been saved in './res' folder!!!")
    except:
        print("The image has not been saved! Please check the path!!!")
    # else:
    #     r_image = yolo.detect_image(image)
    #     r_image.show()
