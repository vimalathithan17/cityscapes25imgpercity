import shutil
import os

def copy_files(src,dest):
    for f in os.listdir(src):
        shutil.copy(os.path.join(src,f),dest) 

def copy_files_rec(src,dest):
    for d in os.listdir(src):
        copy_files(os.path.join(src,d),dest)


copy_files('coco/panoptic_train2017','cityscapes_coco_panoptic_merged/panoptic_train')
copy_files('coco/panoptic_val2017','cityscapes_coco_panoptic_merged/panoptic_val')
copy_files('coco/train2017','cityscapes_coco_panoptic_merged/train')
copy_files('coco/val2017','cityscapes_coco_panoptic_merged/val')

copy_files('CityscapesWithCocoPanopticLabels/panoptic_train','cityscapes_coco_panoptic_merged/panoptic_train')
copy_files('CityscapesWithCocoPanopticLabels/panoptic_val','cityscapes_coco_panoptic_merged/panoptic_val')
copy_files('CityscapesWithCocoPanopticLabels/train','cityscapes_coco_panoptic_merged/train')
copy_files('CityscapesWithCocoPanopticLabels/val','cityscapes_coco_panoptic_merged/val')