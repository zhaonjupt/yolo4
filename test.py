from PIL import Image
import os

with open('./train.txt') as f:
    lines = f.readlines()
    print(len(lines))