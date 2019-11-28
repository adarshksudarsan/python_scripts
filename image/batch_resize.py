#image resize script
from PIL import Image
import os
import sys

directory = '/home/vvdn/Desktop/image_manipulations/images'
a,b=input('Enter required width * height seperated by "*"').split("*")
if not os.path.exists(output_directory):
        os.makedirs(output_directory)
for file_name in os.listdir(directory):
    image = Image.open(os.path.join(directory, file_name))

    x,y = image.size
    new_dimensions = (int(a),int(b)) #dimension set here
    output = image.resize(new_dimensions, Image.ANTIALIAS)

    output_file_name = os.path.join(directory, "small_" + file_name)
    output.save(output_file_name, "JPEG", quality = 95)

print("All done")

