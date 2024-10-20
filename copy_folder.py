import shutil
import os

def copy_files(src,dest):
    for f in os.listdir(src):
        shutil.copy(os.path.join(src,f),dest) 

def copy_files_rec(src,dest):
    for d in os.listdir(src):
        copy_files(os.path.join(src,d),dest)

# copy_files('cityscapes/gtFine/cityscapes_panoptic_train','CityscapesWithCocoPanopticLabels/panoptic_train')
# copy_files('cityscapes/gtFine/cityscapes_panoptic_val','CityscapesWithCocoPanopticLabels/panoptic_val')
# copy_files_rec('cityscapes/leftImg8bit/train','CityscapesWithCocoPanopticLabels/train')
# copy_files_rec('cityscapes/leftImg8bit/val','CityscapesWithCocoPanopticLabels/val')