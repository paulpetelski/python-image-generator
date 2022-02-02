# Image Generator
from PIL import Image
import random

# Traits for each image and weight of each trait
# backgrounds are 500x500 pixels
background = ["Orange", "Blue", "Green", "Purple", "Yellow"]
background_weights = [20, 20, 20, 20, 20]

face = ["b_face", "p_face", "y_face"]
face_weights = [33, 33, 33]

# drawn on 500x500 pixel transparent background
stick_figure = ["Body"]
stick_figure_weights = [100]

# 200 x 200 pixels with transparent background
circle = ["Yellow", "Cyan"]
circle_weights = [50, 50]

background_jpgs = {
    "Orange": "orange",
    "Blue": "blue",
    "Green": "green",
    "Purple": "purple",
    "Yellow": "yellow"
}

face_jpgs = {
    "b_face": "b_face",
    "p_face": "p_face",
    "y_face": "y_face"
}

stick_figure_jpgs = {
    "Body": "body"
}

circle_jpgs = {
    "Yellow": "yellow_circle",
    "Cyan": "cyan_circle"
}

total_images = 12

images = []

def create_new_image():
    new_image = {}
    # chooses a "Background", "Stick Figure" and "Circle" for the new image
    new_image["Background"] = random.choices(background, background_weights)[0]
    new_image["Face"] = random.choices(face,face_weights)[0]
    new_image["Stick Figure"] = random.choices(stick_figure, stick_figure_weights)[0]
    new_image["Circle"] = random.choices(circle, circle_weights)[0]
    # example return: [{'Background': 'Red', 'Stick Figure': 'Body', 'Circle': 'Yellow'}]
    #return new_image
    if new_image in images:
        return create_new_image()
    else:
        return new_image


for n in range(total_images):
    a_new_image = create_new_image()
    images.append(a_new_image)

# number the images
i = 0

print(images)

# save all images as pngs
for images in images:
    # background
    background_img = Image.open(f'./images/background/{background_jpgs[images["Background"]]}.png').convert('RGBA')
    # circle
    circle_img = Image.open(f'./images/circle/{circle_jpgs[images["Circle"]]}.png').convert('RGBA')
    # face
    face_img = Image.open(f'./images/face/{face_jpgs[images["Face"]]}.png').convert('RGBA')
    # stick figure
    stickfigure_body_img = Image.open(f'./images/stickfigure/{stick_figure_jpgs[images["Stick Figure"]]}.png').convert('RGBA')
    # combine the background and circle into one image
    # places the circle on random coordinates each time
    # image1.paste(image2, (random.randint(0, 300), random.randint(0, 300)), image2)
    # places stick figure on background
    background_img.paste(stickfigure_body_img, (0, 0), stickfigure_body_img)
    # add face to stick figure
    background_img.paste(face_img, (150, 100), face_img)
    # number each image
    filename = str(i) + ".png"
    i = i + 1
    background_img.save("./generated_images/" + filename)
