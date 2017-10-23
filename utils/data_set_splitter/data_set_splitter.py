import argparse
import os
from PIL import Image

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import random

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--imagedirectory", required=True,
                help="Directory where image categories are")
args = vars(ap.parse_args())

image_directory = args["imagedirectory"]
image_directory_splitted = image_directory + "/splitted"
image_directory_splitted_training = image_directory_splitted + "/training"
image_directory_splitted_test = image_directory_splitted + "/test"

category_directories = os.listdir(image_directory)

for category in category_directories:
    category_path = image_directory + "/" + category

    image_files = os.listdir(category_path)
    batch_size = int(len(image_files) / 2)
    random.shuffle(image_files)

    train_image_files = image_files[:batch_size]
    print("Saving the training images of  " + category)
    for train_image in train_image_files:
        train_image_filepath = image_directory + "/" + category + "/" + train_image
        img = Image.open(train_image_filepath)
        image_splitted_filepath = image_directory_splitted_training + "/" + category + "/" + train_image

        if not os.path.exists(os.path.dirname(image_splitted_filepath)):
            try:
                os.makedirs(os.path.dirname(image_splitted_filepath))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        print("\nSaving redim image ... " + image_splitted_filepath)
        img.save(image_splitted_filepath)


    test_image_files = image_files[batch_size:]
    print("Saving the test images of  " + category)
    for test_image in test_image_files:
        test_image_filepath = image_directory + "/" + category + "/" + test_image
        img = Image.open(test_image_filepath)
        image_splitted_filepath = image_directory_splitted_test + "/" + category + "/" + test_image

        if not os.path.exists(os.path.dirname(image_splitted_filepath)):
            try:
                os.makedirs(os.path.dirname(image_splitted_filepath))
            except OSError as exc:
                if exc.errno != errno.EEXIST:
                    raise
        print("\nSaving redim image ... " + image_splitted_filepath)
        img.save(image_splitted_filepath)



