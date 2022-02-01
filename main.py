# Image Generator
from PIL import Image
from IPython.display import display
import random
import json

# Traits for each image and weight of each trait
background = ["Red", "Blue"]
background_weights = [50, 50]

circle = ["Yellow", "Cyan"]
circle_weights = [50, 50]

background_jpgs = {
    "Red": "red",
    "Blue": "blue"
}

circle_jpgs = {
    "Yellow": "yellow_circle",
    "Cyan": "cyan_circle"
}

images = []


# test if images are working
def create_new_image():
    new_image = {}

    new_image["Background"] = random.choices(background, background_weights)[0]
    new_image["Circle"] = random.choices(circle, circle_weights)[0]

    return new_image


# add image
a_new_image = create_new_image()
images.append(a_new_image)

print(images)

# print all images as jpegs
for images in images:
    # background
    image1 = Image.open(f'./images/background/{background_jpgs[images["Background"]]}.jpg').convert('RGBA')
    # circle
    image2 = Image.open(f'./images/circle/{circle_jpgs[images["Circle"]]}.png').convert('RGBA')
    # combine the background and circle into one image
    #combo = Image.alpha_composite(image1, image2)
    image1.paste(image2, (0,0), image2)

    image1.save("generated_image.png")