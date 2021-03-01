"""
COCOPanda :: Trash Panda COCO Data Manipulation

The goal of this package is to convert the COCO dataset into the
Trash Panda YOLO format (nested class directories).

The code in this file is based on:
- The official COCO Python API: pycocotools
    - https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/coco.py
    - License information can be found in `license.txt`
- ssaru/convert2Yolo
    - https://github.com/ssaru/convert2Yolo/
"""

from collections import defaultdict
import json
import os
import sys
import time

import numpy as np
import copy
import itertools

from pycocotools.coco import COCO


def _is_array_like(obj):
    return hasattr(obj, "__iter__") and hasattr(obj, "__len__")


def print_progress_bar(
    iteration, total, prefix="", suffix="", decimals=1, length=100, fill="█"
):
    """Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + "-" * (length - filled_length)
    print(
        "\r%s|%s| %s%% (%s/%s)  %s" % (prefix, bar, percent, iteration, total, suffix),
        end="\r",
    )
    # Print New Line on Complete
    if iteration == total:
        print("\n")


class Coco:
    def __init__(self, json_path=None):
        """Constructor of handler class for the COCO dataset format.
        :param json_path (str) : Location of annotation file (json)
        """
        # === Load dataset === #
        # Set up base variables as dictionaries
        self.dataset, self.annos, self.cats, self.imgs = {}, {}, {}, {}

        # Initialize index data structures as `defaultdict`
        self.img_to_annos, self.cat_to_imgs = defaultdict(list), defaultdict(list)

        if json_path:
            print("Loading annotations into memory...")
            tic = time.time()
            with open(json_path, "r") as jsf:
                dataset = json.load(jsf)  # Load json and confirm format is correct
                assert (
                    type(dataset) == dict
                ), f"File format {type(dataset)} not supported."
                print(f"Done (t = {time.time() - tic:0.2f}s)")

                self.dataset = dataset
                self.create_index()

    def create_index(self):
        """Creates an index between images and classes, and images and annotations."""
        print("Creating index...")
        annos, cats, imgs = {}, {}, {}
        img_to_annos, cat_to_imgs = defaultdict(list), defaultdict(list)

        if "annotations" in self.dataset:
            for anno in self.dataset["annotations"]:
                # For each annotation, add index on image_id
                # Each image_id will then have a list of its corresponding annotations
                img_to_annos[anno["image_id"]].append(anno)
                annos[anno["id"]] = anno  # anno lookup by anno_id

        if "images" in self.dataset:
            for img in self.dataset["images"]:
                imgs[img["id"]] = img  # image lookup by image_id

        if "categories" in self.dataset:
            for cat in self.dataset["categories"]:
                cats[cat["id"]] = cat  # cat lookup by cat_id

        if "annotations" in self.dataset and "categories" in self.dataset:
            for anno in self.dataset["annotations"]:
                # Create list of images within each class
                cat_to_imgs[anno["category_id"]].append(anno["image_id"])

        print("Index created!")

        # Set up class data structures
        self.annos = annos
        self.imgs = imgs
        self.cats = cats
        self.img_to_annos = img_to_annos
        self.cat_to_imgs = cat_to_imgs

    def info(self):
        """Print info about the annotation file."""
        for key, value in self.dataset["info"].items():
            print(f"{key}: {value}")

    def get_cat_dict(self):
        """Get category dictionary of {name: id}.
        :param coco_api (CoCo)  : Instance of CoCo handler class.
        :return cat_dict (dict) : Dictionary of {cat_name: cat_id}.
        """
        cats = self.load_cats(self.get_cat_ids())
        return {cat["name"]: cat["id"] for cat in cats}

    def get_anno_ids(self, img_ids=[], cat_ids=[], iscrowd=None):
        """Get ann ids that satisfy given filter conditions. default skips that filter
        :param img_ids (int array)      : get annos for given imgs
        :param cat_ids (int array)      : get annos for given cats
        :param iscrowd (boolean)        : get annos for given crowd label (False or True)
        :return: ids (int array)        : integer array of ann ids
        """
        # Always start with arrays
        img_ids = img_ids if _is_array_like(img_ids) else [img_ids]
        cat_ids = cat_ids if _is_array_like(cat_ids) else [cat_ids]

        # If nothing is passed, return entire list of annotations
        if len(img_ids) == len(cat_ids) == 0:
            annos = self.dataset["annotations"]
        else:
            # If image_ids are passed, create list of annos for each
            if len(img_ids) > 0:
                lists = [
                    self.img_to_annos[img_id]
                    for img_id in img_ids
                    if img_id in self.img_to_annos
                ]
                annos = list(itertools.chain.from_iterable(lists))
            else:
                annos = self.dataset["annotations"]

            annos = (
                annos
                if len(cat_ids) == 0
                else [anno for anno in annos if anno["category_id"] in cat_ids]
            )

        if iscrowd:
            ids = [anno["id"] for anno in annos if anno["iscrowd"] == iscrowd]
        else:
            ids = [anno["id"] for anno in annos]

        return ids

    def get_cat_ids(self, cat_names=[], super_cats=[], cat_ids=[]):
        """Filtering parameters. default skips that filter.
        :param cat_names (str array)   : get cats for given cat names
        :param super_cats (str array)  : get cats for given supercategory names
        :param cat_ids (int array)     : get cats for given cat ids
        :return: ids (int array)       : integer array of cat ids
        """
        # Once again, be sure they are always arrays
        cat_names = cat_names if _is_array_like(cat_names) else [cat_names]
        super_cats = super_cats if _is_array_like(super_cats) else [super_cats]
        cat_ids = cat_ids if _is_array_like(cat_ids) else [cat_ids]

        if len(cat_names) == len(super_cats) == len(cat_ids) == 0:
            cats = self.dataset["categories"]
        else:
            # If list of cats is passed, get list of ids
            cats = self.dataset["categories"]
            cats = (
                cats
                if len(cat_names) == 0
                else [cat for cat in cats if cat["name"] in cat_names]
            )
            # If supercategories is passed, get list of cats within
            cats = (
                cats
                if len(super_cats) == 0
                else [cat for cat in cats if cat["supercategory"] in super_cats]
            )
            cats = (
                cats
                if len(cat_ids) == 0
                else [cat for cat in cats if cat["id"] in cat_ids]
            )
        ids = [cat["id"] for cat in cats]

        return ids

    def get_img_ids(self, img_ids=[], cat_ids=[]):
        """Get img ids that satisfy given filter conditions.
        :param img_ids (int array) : get imgs for given ids
        :param cat_ids (int array) : get imgs with all given cats
        :return: ids (int array)   : integer array of img ids
        """
        # Always use arrays
        img_ids = img_ids if _is_array_like(img_ids) else [img_ids]
        cat_ids = cat_ids if _is_array_like(cat_ids) else [cat_ids]

        if len(img_ids) == len(cat_ids) == 0:
            ids = self.imgs.keys()
        else:
            ids = set(img_ids)
            for i, cat_id in enumerate(cat_ids):
                if i == 0 and len(ids) == 0:
                    ids = set(self.cat_to_imgs[cat_id])
                else:
                    ids &= set(self.cat_to_imgs[cat_id])
        return list(ids)

    def get_img_ids_from_cats(self, img_ids=[], cat_ids=[]):
        """Get img_ids that fall into *any* of the cat_ids.
        :param cat_ids (int array) : get imgs with all given cats
        :return: ids (int array)   : integer array of img ids
        """
        # Always use arrays
        img_ids = img_ids if _is_array_like(img_ids) else [img_ids]
        cat_ids = cat_ids if _is_array_like(cat_ids) else [cat_ids]

        if len(img_ids) == len(cat_ids) == 0:
            ids = self.imgs.keys()
        else:
            ids = set(img_ids)
            for i, cat_id in enumerate(cat_ids):
                if i == 0 and len(ids) == 0:
                    ids = set(self.cat_to_imgs[cat_id])
                else:
                    ids |= set(self.cat_to_imgs[cat_id])
        return list(ids)

    def load_annos(self, ids=[]):
        """Load annotations with the specified ids.
        :param ids (int array)       : integer ids specifying annos
        :return: annos (object array) : loaded ann objects
        """
        if _is_array_like(ids):
            return [self.annos[id] for id in ids]
        elif type(ids) == int:
            return [self.annos[ids]]

    def load_cats(self, ids=[]):
        """Load cats with the specified ids.
        :param ids (int array)       : integer ids specifying cats
        :return: cats (object array) : loaded cat objects
        """
        if _is_array_like(ids):
            return [self.cats[id] for id in ids]
        elif type(ids) == int:
            return [self.cats[ids]]

    def load_imgs(self, ids=[]):
        """Load annos with the specified ids.
        :param ids (int array)       : integer ids specifying img
        :return: imgs (object array) : loaded img objects
        """
        if _is_array_like(ids):
            return [self.imgs[id] for id in ids]
        elif type(ids) == int:
            return [self.imgs[ids]]

    def parse(self, imgs_data, cats_data, anno_data):
        # Dict to hold parsed data
        data = {}

        # Track and report progress using progress bar
        progress_length = len(anno_data)
        progress_cnt = 0
        print_progress_bar(
            0,
            progress_length,
            prefix="\nCOCO Parsing:".ljust(15),
            suffix="Complete",
            length=40,
        )

        for anno in anno_data:

            image_id = anno["image_id"]
            cls_id = anno["category_id"]

            filename = None
            img_width = None
            img_height = None
            cls = None

            for info in imgs_data:
                if info["id"] == image_id:
                    filename, img_width, img_height = (
                        info["file_name"].split(".")[0],
                        info["width"],
                        info["height"],
                    )

            for category in cats_data:
                if category["id"] == cls_id:
                    cls = category["name"]

            size = {"width": img_width, "height": img_height, "depth": "3"}

            bndbox = {
                "xmin": anno["bbox"][0],
                "ymin": anno["bbox"][1],
                "xmax": anno["bbox"][2] + anno["bbox"][0],
                "ymax": anno["bbox"][3] + anno["bbox"][1],
            }

            obj_info = {"name": cls, "bndbox": bndbox}

            if filename in data:
                obj_idx = str(int(data[filename]["objects"]["num_obj"]))
                data[filename]["objects"][str(obj_idx)] = obj_info
                data[filename]["objects"]["num_obj"] = int(obj_idx) + 1

            elif filename not in data:

                obj = {"num_obj": "1", "0": obj_info}

                data[filename] = {"size": size, "objects": obj}

            print_progress_bar(
                progress_cnt + 1,
                progress_length,
                prefix="COCO Parsing:".ljust(15),
                suffix="Complete",
                length=40,
            )
            progress_cnt += 1

        return True, data


class Yolo:
    """Handler Class for YOLO Format."""

    def __init__(self, cls_list_path):
        with open(cls_list_path, "r") as file:
            l = file.read().splitlines()

        self.cls_list = l

    def convert_coordinates(self, size, box):
        dw = 1.0 / size[0]
        dh = 1.0 / size[1]

        # Calculate box coordinates
        # (xmin + xmax / 2)
        x = (box[0] + box[1]) / 2.0
        # (ymin + ymax / 2)
        y = (box[2] + box[3]) / 2.0

        # Calculate width and height
        # (xmax - xmin) = w
        w = box[1] - box[0]
        # (ymax - ymin) = h
        h = box[3] - box[2]

        x = x * dw
        w = w * dw
        y = y * dh
        h = h * dh

        return (round(x, 3), round(y, 3), round(w, 3), round(h, 3))

    def parse(self, label_path, img_path, img_type=".jpg"):
        try:

            (dir_path, dir_names, filenames) = next(
                os.walk(os.path.abspath(label_path))
            )

            data = {}

            progress_length = len(filenames)
            progress_cnt = 0
            print_progress_bar(
                0,
                progress_length,
                prefix="\nYOLO Parsing:".ljust(15),
                suffix="Complete",
                length=40,
            )

            for filename in filenames:

                txt = open(os.path.join(dir_path, filename), "r")

                filename = filename.split(".")[0]

                img = Image.open(os.path.join(img_path, "".join([filename, img_type])))
                img_width = str(img.size[0])
                img_height = str(img.size[1])
                img_depth = 3

                size = {"width": img_width, "height": img_height, "depth": img_depth}

                obj = {}
                obj_cnt = 0

                for line in txt:
                    elements = line.split(" ")
                    name_id = elements[0]

                    xminAddxmax = float(elements[1]) * (2.0 * float(img_width))
                    yminAddymax = float(elements[2]) * (2.0 * float(img_height))

                    w = float(elements[3]) * float(img_width)
                    h = float(elements[4]) * float(img_height)

                    xmin = (xminAddxmax - w) / 2
                    ymin = (yminAddymax - h) / 2
                    xmax = xmin + w
                    ymax = ymin + h

                    bndbox = {
                        "xmin": float(xmin),
                        "ymin": float(ymin),
                        "xmax": float(xmax),
                        "ymax": float(ymax),
                    }

                    obj_info = {"name": name_id, "bndbox": bndbox}

                    obj[str(obj_cnt)] = obj_info
                    obj_cnt += 1

                obj["num_obj"] = obj_cnt

                data[filename] = {"size": size, "objects": obj}

                print_progress_bar(
                    progress_cnt + 1,
                    progress_length,
                    prefix="YOLO Parsing:".ljust(15),
                    suffix="Complete",
                    length=40,
                )
                progress_cnt += 1

            return True, data

        except Exception as e:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            msg = "ERROR : {}, moreInfo : {}\t{}\t{}".format(
                e, exc_type, fname, exc_tb.tb_lineno
            )

            return False, msg

    def generate(self, data):

        try:

            progress_length = len(data)
            progress_cnt = 0
            print_progress_bar(
                0,
                progress_length,
                prefix="\nYOLO Generating:".ljust(15),
                suffix="Complete",
                length=40,
            )

            result = {}

            for key in data:
                img_width = int(data[key]["size"]["width"])
                img_height = int(data[key]["size"]["height"])

                contents = ""

                for idx in range(0, int(data[key]["objects"]["num_obj"])):

                    xmin = data[key]["objects"][str(idx)]["bndbox"]["xmin"]
                    ymin = data[key]["objects"][str(idx)]["bndbox"]["ymin"]
                    xmax = data[key]["objects"][str(idx)]["bndbox"]["xmax"]
                    ymax = data[key]["objects"][str(idx)]["bndbox"]["ymax"]

                    b = (float(xmin), float(xmax), float(ymin), float(ymax))
                    bb = self.convert_coordinates((img_width, img_height), b)

                    cls_id = self.cls_list.index(data[key]["objects"][str(idx)]["name"])

                    bndbox = "".join(["".join([str(e), " "]) for e in bb])
                    contents = "".join([contents, str(cls_id), " ", bndbox[:-1], "\n"])

                result[key] = contents

                print_progress_bar(
                    progress_cnt + 1,
                    progress_length,
                    prefix="YOLO Generating:".ljust(15),
                    suffix="Complete",
                    length=40,
                )
                progress_cnt += 1

            return True, result

        except Exception as e:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            msg = "ERROR : {}, moreInfo : {}\t{}\t{}".format(
                e, exc_type, fname, exc_tb.tb_lineno
            )

            return False, msg

    def save(self, data, save_path, img_path, img_type, manifest_path):

        try:

            progress_length = len(data)
            progress_cnt = 0
            print_progress_bar(
                0,
                progress_length,
                prefix="\nYOLO Saving:".ljust(15),
                suffix="Complete",
                length=40,
            )

            m_path = os.path.abspath(os.path.join(manifest_path, "manifest.txt"))

            with open(m_path, "w") as manifest_file:

                for key in data:
                    manifest_file.write(
                        os.path.abspath(
                            os.path.join(img_path, "".join([key, img_type, "\n"]))
                        )
                    )

                    with open(
                        os.path.abspath(
                            os.path.join(save_path, "".join([key, ".txt"]))
                        ),
                        "w",
                    ) as label:
                        label.write(data[key])

                    print_progress_bar(
                        progress_cnt + 1,
                        progress_length,
                        prefix="YOLO Saving:".ljust(15),
                        suffix="Complete",
                        length=40,
                    )
                    progress_cnt += 1

            return True, None

        except Exception as e:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            msg = "ERROR : {}, moreInfo : {}\t{}\t{}".format(
                e, exc_type, fname, exc_tb.tb_lineno
            )

            return False, msg
