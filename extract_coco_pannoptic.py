import shutil
import os
import json
with open('kaggle/working/panoptic_train.json') as f:
    ptrain=json.load(f)
with open('kaggle/working/panoptic_val.json') as f:
    pval=json.load(f)

src_t='annotations/panoptic_train2017'
src_v='annotations/panoptic_val2017'
dest_t='coco/panoptic_train2017'
dest_v='coco/panoptic_val2017'

if dest_t  in os.listdir('coco'):
    shutil.rmtree(dest_t)
if dest_v in os.listdir('coco'):
    shutil.rmtree(dest_v)
os.mkdir(dest_t)
os.mkdir(dest_v)
train_imgs=set()
val_imgs=set()
for ann in ptrain['annotations']:
    train_imgs.add(ann['file_name'])
for ann in pval['annotations']:
    val_imgs.add(ann['file_name'])
for im in os.listdir(src_t):
    if im in train_imgs:
        print( dest_t+'/' + im)
        shutil.copy(f'{src_t}/{im}',dest_t)
for im in os.listdir(src_v):
    if im in val_imgs:
        print(dest_v+'/' + im)
        shutil.copy(f'{src_v}/{im}',dest_v)