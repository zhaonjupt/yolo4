import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

#classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
classes = ["warning", "safe"]

def convert_annotation(year, image_id, list_file):
    in_file = open('./VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id), 'rb')
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls == "person":
            cls = "warning"
        elif cls == "hat":
            cls = "safe"
        #if cls not in classes or int(difficult)==1:
        if cls not in classes:
            continue
        cls_id = classes.index(cls)   #标签列表的索引值
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))



if __name__ == '__main__':
    wd = getcwd()  # 返回当前工作目录
    for year, image_set in sets:
        image_ids = open('./VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
        list_file = open('%s_%s.txt'%(year, image_set), 'w')
        for image_id in image_ids:
            #list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg'%(wd, year, image_id))
            list_file.write('./VOCdevkit/VOC%s/JPEGImages/%s.jpg' % (year, image_id))
            convert_annotation(year, image_id, list_file)
            list_file.write('\n')
        list_file.close()