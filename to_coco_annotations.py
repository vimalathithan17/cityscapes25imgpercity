import json 
import os
#BASE='/workspace/cityscapes25imgpercity/'#base directory path
to_coco={
 7: {'color': (128, 64, 128), 'isthing': 0, 'id': 149, 'name': 'road'},
 11: {'color': (70, 70, 70), 'isthing': 0, 'id': 128, 'name': 'house'},
 12: {'color': (102, 102, 156),'isthing': 0,'id': 199,'name': 'wall-other-merged'},
 13: {'color': (190, 153, 153),'isthing': 0,'id': 185,'name': 'fence-merged'},
 19: {'color': (250, 170, 30),'isthing': 1,'id': 10,'name': 'traffic light'},
 20: {'color': (220, 220, 0), 'isthing': 1, 'id': 13, 'name': 'stop sign'},
 21: {'color': (107, 142, 35), 'isthing': 0, 'id': 184, 'name': 'tree-merged'},
 22: {'color': (152, 251, 152),'isthing': 0,'id': 193,'name': 'grass-merged'},
 23: {'color': (70, 130, 180),'isthing': 0,'id': 187,'name': 'sky-other-merged'},
 24: {'color': (220, 20, 60), 'isthing': 1, 'id': 1, 'name': 'person'},
 26: {'color': (0, 0, 142), 'isthing': 1, 'id': 3, 'name': 'car'},
 27: {'color': (0, 0, 70), 'isthing': 1, 'id': 8, 'name': 'truck'},
 28: {'color': (0, 60, 100), 'isthing': 1, 'id': 6, 'name': 'bus'},
 31: {'color': (0, 80, 100), 'isthing': 1, 'id': 7, 'name': 'train'},
 32: {'color': (0, 0, 230), 'isthing': 1, 'id': 4, 'name': 'motorcycle'},
 33: {'color': (119, 11, 32), 'isthing': 1, 'id': 2, 'name': 'bicycle'},
 25: {'color': (255, 0, 0),'isthing': 1,'id': 201,'name': 'rider'},
 17: {'color': (153, 153, 153),'isthing': 0,'id': 202,'name': 'pole'},
 8: {'color': (244, 35, 232),'isthing': 0,'id': 203,'name': 'sidewalk'}
 }

with open('cityscapes/gtFine/cityscapes_panoptic_train.json') as f:
    p=json.load(f)
for ann in p['annotations']:
    for seg in ann['segments_info']:
        seg['category_id']=to_coco[seg['category_id']]['id']
p.pop('categories')

with open('CityscapesWithCocoPanopticLabels/annotations/city_panoptic_train.json','w') as f:
    json.dump(p,f,indent=4)

with open('cityscapes/gtFine/cityscapes_panoptic_val.json') as f:
    p=json.load(f)
for ann in p['annotations']:
    for seg in ann['segments_info']:
        seg['category_id']=to_coco[seg['category_id']]['id']
p.pop('categories')

with open('CityscapesWithCocoPanopticLabels/annotations/city_panoptic_val.json','w') as f:
    json.dump(p,f,indent=4)