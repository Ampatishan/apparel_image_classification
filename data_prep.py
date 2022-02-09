import os
import shutil
import torch
from torchvision import transforms
from torch.utils import data

PROJECT_PATH = '/Users/ampatishan/PycharmProjects/apprael_image_classification/'
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
TEST_PATH = os.path.join(PROJECT_PATH, 'data/test')
TRAIN_PATH = os.path.join(PROJECT_PATH, 'data/train')
TRAIN_SAMPLE_PERCENTAGE = 0.8


def mkdir(path):
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)


classes = os.listdir(DATA_PATH)

mkdir(TRAIN_PATH)
mkdir(TEST_PATH)

for _class in classes:
    if _class.startswith('.') or _class in ['test', 'train']:
        continue
    class_path = os.path.join(DATA_PATH, _class)
    no_of_train_samples = len(os.listdir(class_path)) * TRAIN_SAMPLE_PERCENTAGE
    images = os.listdir(class_path)
    train_class_path = os.path.join(TRAIN_PATH, _class)
    test_class_path = os.path.join(TEST_PATH, _class)

    mkdir(train_class_path)
    mkdir(test_class_path)

    for n, image in enumerate(images):
        source_path = os.path.join(class_path, image)
        dest_path = None
        if n <= no_of_train_samples:
            dest_path = os.path.join(train_class_path, image)
        elif n > no_of_train_samples:
            dest_path = os.path.join(test_class_path, image)

        shutil.move(source_path, dest_path)

    os.rmdir(class_path)


