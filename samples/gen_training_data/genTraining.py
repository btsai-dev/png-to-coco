"""
    Generates training dataset from paint-brushed dataset

    python3 genTraining.py --dataset=/path/to/dataset

    Expected Filesystem Structure:
    dataset <- Location as the optional --dataset argument
     ├── Annotations
     │ ├── 0
     │ │   ├── category1.jpg
     │ │   └── category2.jpg
     │ ├── ...
     │ └── 9
     │     ├── category1.jpg
     │     ├── category2.jpg
     │     └── category3.jpg
     └── Images
       ├── 0.jpg
       ├── ...
       └── 9.jpg

    If you do not pass the --dataset argument, the program will use the filesystem
    structure located at \dataset
"""

import os
import cv2
from pathlib import Path
import sys
import json

# ROOT_DIR = os.path.abspath("../../")
ROOT_DIR = str(Path(__file__).resolve().parents[2])
print(ROOT_DIR)

sys.path.append(ROOT_DIR)
RESOURCE_DIR = os.path.join(ROOT_DIR, 'resources', 'img')
TEST_DIR = os.path.join(RESOURCE_DIR, 'test')

from gen_annotation import segcolor



def make_image_annotation(img, file_name, image_id, bbox):
    width, height = img.size
    image_annotation = {
        "file_name": file_name,
        "width": width,
        "height": height,
        "id": image_id
    }
    return image_annotation


def get_colors_Test(img):
    mask = segcolor.get_colors(img)
    #od.display(mask, 'get_colors_Test')
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return mask


def get_mask_categorized_Test(mask):
    mask_categorized = segcolor.get_mask_categorized(mask)

    return mask_categorized


if __name__ == '__main__':
    original_img = cv2.imread(os.path.join(TEST_DIR, 'orig.tif'))
    marked_img = cv2.imread(os.path.join(TEST_DIR, 'marked.tif'))
    mask = get_colors_Test(marked_img)
    submasks = get_mask_categorized_Test(mask)

    is_crowd = 0
    # annotation_id = 1
    image_id = 1
    annotations = []
    images = []
    categories = [
        {"supercategory": "material defect",
         "id": 1,
         "name": "crack"}
    ]

    # TODO: IMPLEMENT MAKE IMAGE ANNOTATION
    # image = make_image_anngotation(img, filename, image_id)
    image = {
        "file_name": "marked.tif",
        "height": 2560,
        "width": 2560,
        "id": image_id
    }
    images.append(image)

    for color, submask in submasks.items():
        # category_id = category_ids[image_id][color]
        category_id = 1  # Default for now
        annotation = segcolor.make_submask_annotations(
            submask,
            image_id,
            category_id,
            is_crowd
        )
        annotations.extend(annotation)
    image_id += 1

    coco = {
        "images": images,
        "annotations": annotations,
        "categories": categories
    }
    # print(json.dumps(coco, indent=4))

    json_out = os.path.join(TEST_DIR, "output" + "." + "json")

    with open(json_out, 'w') as outfile:
        json.dump(coco, outfile)