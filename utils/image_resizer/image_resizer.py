import argparse
import os
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--imagedirectory", required = True, help = "Directory where image categories are")
args = vars(ap.parse_args())

image_directory = args["imagedirectory"]
image_directory_redim = image_directory + "_redim"

category_directories = os.listdir(image_directory)

for category in category_directories:
	category_path = image_directory + "/" + category
	image_files = os.listdir(category_path)
	for image_filename in image_files:
                image_filepath = image_directory + "/" + category + "/" + image_filename
                img = Image.open(image_filepath)
                img = img.resize((64, 64), Image.ANTIALIAS)
                image_redim_filepath = image_directory_redim + "/" + category + "/" + image_filename

                if not os.path.exists(os.path.dirname(image_redim_filepath)):
                        try:
                                os.makedirs(os.path.dirname(image_redim_filepath))
                        except OSError as exc:
                                if exc.errno != errno.EEXIST:
                                        raise
                print("Saving redim image ... " + image_redim_filepath)
                img.save(image_redim_filepath)
