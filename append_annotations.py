import json

def append_annotations(file1,file2,dest):
    with open(file1) as f:
        p1=json.load(f)
    with open(file2) as f:
        p2=json.load(f)
    p1['annotations'].extend(p2['annotations'])
    p1['images'].extend(p2['images'])
    # p1['categories']=[
    # {
    #     "color": [
    #         128,
    #         64,
    #         128
    #     ],
    #     "isthing": 0,
    #     "id": 149,
    #     "name": "road"
    # },
    # {
    #     "color": [
    #         70,
    #         70,
    #         70
    #     ],
    #     "isthing": 0,
    #     "id": 128,
    #     "name": "house"
    # },
    # {
    #     "color": [
    #         102,
    #         102,
    #         156
    #     ],
    #     "isthing": 0,
    #     "id": 199,
    #     "name": "wall-other-merged"
    # },
    # {
    #     "color": [
    #         190,
    #         153,
    #         153
    #     ],
    #     "isthing": 0,
    #     "id": 185,
    #     "name": "fence-merged"
    # },
    # {
    #     "color": [
    #         250,
    #         170,
    #         30
    #     ],
    #     "isthing": 1,
    #     "id": 10,
    #     "name": "traffic light"
    # },
    # {
    #     "color": [
    #         220,
    #         220,
    #         0
    #     ],
    #     "isthing": 1,
    #     "id": 13,
    #     "name": "stop sign"
    # },
    # {
    #     "color": [
    #         107,
    #         142,
    #         35
    #     ],
    #     "isthing": 0,
    #     "id": 184,
    #     "name": "tree-merged"
    # },
    # {
    #     "color": [
    #         152,
    #         251,
    #         152
    #     ],
    #     "isthing": 0,
    #     "id": 193,
    #     "name": "grass-merged"
    # },
    # {
    #     "color": [
    #         70,
    #         130,
    #         180
    #     ],
    #     "isthing": 0,
    #     "id": 187,
    #     "name": "sky-other-merged"
    # },
    # {
    #     "color": [
    #         220,
    #         20,
    #         60
    #     ],
    #     "isthing": 1,
    #     "id": 1,
    #     "name": "person"
    # },
    # {
    #     "color": [
    #         0,
    #         0,
    #         142
    #     ],
    #     "isthing": 1,
    #     "id": 3,
    #     "name": "car"
    # },
    # {
    #     "color": [
    #         0,
    #         0,
    #         70
    #     ],
    #     "isthing": 1,
    #     "id": 8,
    #     "name": "truck"
    # },
    # {
    #     "color": [
    #         0,
    #         60,
    #         100
    #     ],
    #     "isthing": 1,
    #     "id": 6,
    #     "name": "bus"
    # },
    # {
    #     "color": [
    #         0,
    #         80,
    #         100
    #     ],
    #     "isthing": 1,
    #     "id": 7,
    #     "name": "train"
    # },
    # {
    #     "color": [
    #         0,
    #         0,
    #         230
    #     ],
    #     "isthing": 1,
    #     "id": 4,
    #     "name": "motorcycle"
    # },
    # {
    #     "color": [
    #         119,
    #         11,
    #         32
    #     ],
    #     "isthing": 1,
    #     "id": 2,
    #     "name": "bicycle"
    # },
    # {
    #     "color": [
    #         255,
    #         0,
    #         0
    #     ],
    #     "isthing": 1,
    #     "id": 201,
    #     "trainId": 12,
    #     "name": "rider"
    # },
    # {
    #     "color": [
    #         153,
    #         153,
    #         153
    #     ],
    #     "isthing": 0,
    #     "id": 202,
    #     "trainId": 5,
    #     "name": "pole"
    # },
    # {
    #     "color": [
    #         244,
    #         35,
    #         232
    #     ],
    #     "isthing": 0,
    #     "id": 203,
    #     "trainId": 1,
    #     "name": "sidewalk"
    # },
    # {
    #     "color": [
    #         106,
    #         0,
    #         228
    #     ],
    #     "isthing": 1,
    #     "id": 5,
    #     "name": "airplane"
    # },
    # {
    #     "color": [
    #         0,
    #         0,
    #         192
    #     ],
    #     "isthing": 1,
    #     "id": 9,
    #     "name": "boat"
    # },
    # {
    #     "color": [
    #         100,
    #         170,
    #         30
    #     ],
    #     "isthing": 1,
    #     "id": 11,
    #     "name": "fire hydrant"
    # },
    # {
    #     "color": [
    #         175,
    #         116,
    #         175
    #     ],
    #     "isthing": 1,
    #     "id": 14,
    #     "name": "parking meter"
    # },
    # {
    #     "color": [
    #         250,
    #         0,
    #         30
    #     ],
    #     "isthing": 1,
    #     "id": 15,
    #     "name": "bench"
    # },
    # {
    #     "color": [
    #         255,
    #         179,
    #         240
    #     ],
    #     "isthing": 1,
    #     "id": 27,
    #     "name": "backpack"
    # },
    # {
    #     "color": [
    #         0,
    #         125,
    #         92
    #     ],
    #     "isthing": 1,
    #     "id": 28,
    #     "name": "umbrella"
    # },
    # {
    #     "color": [
    #         209,
    #         0,
    #         151
    #     ],
    #     "isthing": 1,
    #     "id": 31,
    #     "name": "handbag"
    # },
    # {
    #     "color": [
    #         188,
    #         208,
    #         182
    #     ],
    #     "isthing": 1,
    #     "id": 32,
    #     "name": "tie"
    # },
    # {
    #     "color": [
    #         0,
    #         220,
    #         176
    #     ],
    #     "isthing": 1,
    #     "id": 33,
    #     "name": "suitcase"
    # },
    # {
    #     "color": [
    #         255,
    #         180,
    #         195
    #     ],
    #     "isthing": 0,
    #     "id": 144,
    #     "name": "platform"
    # },
    # {
    #     "color": [
    #         96,
    #         96,
    #         96
    #     ],
    #     "isthing": 0,
    #     "id": 191,
    #     "name": "pavement-merged"
    # }
# ]
    with open(dest,'w') as f:
        json.dump(p1,f,indent=4)
append_annotations('coco/annotations/panoptic_train.json','CityscapesWithCocoPanopticLabels/annotations/city_panoptic_train.json','cityscapes_coco_panoptic_merged/annotations/panoptic_train.json')
append_annotations('coco/annotations/panoptic_val.json','CityscapesWithCocoPanopticLabels/annotations/city_panoptic_val.json','cityscapes_coco_panoptic_merged/annotations/panoptic_val.json')