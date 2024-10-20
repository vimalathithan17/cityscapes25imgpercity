import requests
import os
import json
with open('kaggle/working/instances_train.json') as f:
    ptrain=json.load(f)
with open('kaggle/working/instances_val.json') as f:
    pval=json.load(f)

os.mkdir('coco/train2017')
os.mkdir('coco/val2017')

for im in ptrain['images']:
    img_data = requests.get(im['coco_url']).content
    print('train2017/' + im['file_name'])
    with open('coco/train2017/' + im['file_name'], 'wb') as handler:
        handler.write(img_data)
for im in pval['images']:
    img_data = requests.get(im['coco_url']).content
    print('val2017/' + im['file_name'])
    with open('coco/val2017/' + im['file_name'], 'wb') as handler:
        handler.write(img_data)