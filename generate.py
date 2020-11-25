import os, shutil
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    txt = './train.txt'
    src = r'D:/桌面/VOC2007/Annotations'
    filelist = os.listdir(src)
    with open(txt, 'a+') as f:
        for _, file in enumerate(filelist):
            filename = file.split('.')[0]
            f.write('./VOCdevkit/VOC2007/JPEGImages/'+filename+'.jpg')
            tree = ET.parse(src+'/'+file)
            root = tree.getroot()

            for obj in root.iter('object'):
                name = obj.find('name').text

                if name == 'person':
                    str = '0'
                elif name == 'driver':
                    str = '1'
                elif name == 'car':
                    str = '2'
                elif name == 'bus':
                    str = '3'
                elif name == 'truck':
                    str = '4'
                elif name == 'van':
                    str = '4'
                elif name == 'face':
                    str = '5'
                elif name == 'plate':
                    str = '6'

                bbox = obj.find('bndbox')
                xmin = bbox.find('xmin').text
                ymin = bbox.find('ymin').text
                xmax = bbox.find('xmax').text
                ymax = bbox.find('ymax').text
                f.write(' ' + xmin + ',' + ymin + ',' + xmax + ',' + ymax + ',' + str)

            f.write('\n')