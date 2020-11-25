import os,shutil
import re
from PIL import  Image
import cv2

def gen(src, dsc):
    filelist = os.listdir(src)
    # a+追加写入   w覆盖写入
    with open(dsc, 'a+') as writer:
        for _, file in enumerate(filelist):
            filePath = src+'/'+file
            with open(filePath, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if(line.startswith("Image filename")):
                        #print(line.split(':')[-1])
                        str = line.split(':')[-1]
                        str = str[2:]
                        str = str[:-2]
                        str = str.split('/')[-1].split('.')[0] + '.jpg'
                        # print(str)
                        writer.write('./VOCdevkit/VOC2007/JPEGImages/' + str)
                    if(line.startswith('Bounding box')):
                        str = line.split(':')[-1]
                        xmin, ymin, xmax, ymax = re.findall("\d+", str)
                        # print(xmin, ymin, xmax, ymax)
                        writer.write(' '+xmin+','+ymin+','+xmax+','+ymax+',0')

            writer.write('\n')
            print("================================================")

def readTxt(src):
    with open(src, 'r') as f:
        lines = f.readlines()
        for line in lines:
            filename = line.split()[0]
            img = Image.open(filename)
            img.show()


if __name__ == '__main__':
    src = r'D:/桌面/walker/Annotations'
    dsc = './train.txt'
    #readTxt(dsc)
    gen(src, dsc)