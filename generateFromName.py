import os, shutil
import re
from PIL import Image


def gen(src, dsc):
    with open(dsc, 'w') as writer:
        filelist = os.listdir(src)
        for i, file in enumerate(filelist):
            filename = file.split('.')[0]
            # newName = str(i).zfill()
            #文件名小于一定长度即为np子目录， 即图中不存在车牌信息
            if len(filename) < 5:
                newName = 'np_' + str(i+1).zfill(8)+'.jpg'
                os.rename(src + '/' + file, src + '/' + newName)
                writer.write(src + '/' + newName + ' \n')
            else:
                newName = "plate_" + str(i+1).zfill(8)+'.jpg'
                string = filename.split('-')[2]
                print(string)
                os.rename(src+'/'+file, src+'/'+newName)
                xmin, ymin, xmax, ymax = re.findall("\d+", string)
                writer.write(src +'/'+ newName + ' ')
                writer.write(xmin+','+ymin+','+xmax+','+ymax+',')
                writer.write('6'+'\n')


def read(src):
    with open(src,'r') as file:
        lines = file.readlines()
        for _, line in enumerate(lines):
            path = line.split(' ')[0]
            img = Image.open(path)
            img.show()

if __name__ == '__main__':
    src = './VOCdevkit/VOC2007/JPEGImages'
    dsc = './train.txt'
    gen(src, dsc)
    #read(dsc)