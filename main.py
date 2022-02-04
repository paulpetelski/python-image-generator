# Image Generator
from PIL import Image
import random
# for gui
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ImageGenerator:
    # number of images you want to create
    total_images = 12
    images = []
    # number the images
    filename_counter = 1
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

    def create_new_image(self):
        new_image = {}
        # chooses a "Background", "Stick Figure" and "Circle" for the new image
        new_image["Background"] = random.choices(self.background, self.background_weights)[0]
        new_image["Face"] = random.choices(self.face, self.face_weights)[0]
        new_image["Stick Figure"] = random.choices(self.stick_figure, self.stick_figure_weights)[0]
        new_image["Circle"] = random.choices(self.circle, self.circle_weights)[0]
        # example return: [{'Background': 'Red', 'Stick Figure': 'Body', 'Circle': 'Yellow'}]
        # return new_image
        if new_image in self.images:
            return self.create_new_image()
        else:
            return new_image

    def image_loop(self):
        for n in range(self.total_images):
            a_new_image = self.create_new_image()
            self.images.append(a_new_image)

    # save all images as pngs
    def print_images(self, images):
        for images in images:
            # background
            background_img = Image.open(f'./images/background/{self.background_jpgs[images["Background"]]}.png').convert('RGBA')
            # circle
            circle_img = Image.open(f'./images/circle/{self.circle_jpgs[images["Circle"]]}.png').convert('RGBA')
            # face
            face_img = Image.open(f'./images/face/{self.face_jpgs[images["Face"]]}.png').convert('RGBA')
            # stick figure
            stickfigure_body_img = Image.open(
                f'./images/stickfigure/{self.stick_figure_jpgs[images["Stick Figure"]]}.png').convert(
                'RGBA')
            # combine the background and circle into one image
            # places the circle on random coordinates each time
            # image1.paste(image2, (random.randint(0, 300), random.randint(0, 300)), image2)
            # places stick figure on background
            background_img.paste(stickfigure_body_img, (0, 0), stickfigure_body_img)
            # add face to stick figure
            background_img.paste(face_img, (150, 100), face_img)
            # number each image
            filename = str(self.filename_counter) + ".png"
            self.filename_counter = self.filename_counter + 1
            background_img.save("./generated_images/" + filename)


# Run the program
ig = ImageGenerator()
# creates the images and adds it to list
ig.image_loop()
# prints the images in the list
ig.print_images(ig.images)
# prints the list
print(ig.images)


""" GUI: WORK IN PROGRESS
# GUI window
def window():
    app = QApplication(sys.argv)
    win = QWidget()

    label = QLabel()
    label.setText("Number of images to generate: ")
    label.setAlignment(Qt.AlignLeft)

    num = QLineEdit()
    num.setValidator(QIntValidator())
    num.setMaxLength(4)
    #num.textChanged.connect(b1_clicked)
    #print(num.text())

    b1 = QPushButton()
    b1.setText("Button")
    b1.move(50, 20)
    app.setStyleSheet("QPushButton { margin: 5ex }")

    vbox = QVBoxLayout()
    vbox.addWidget(label)
    vbox.addStretch()
    vbox.addWidget(b1)
    vbox.addWidget(num)

    win.setLayout(vbox)
    win.show()
    sys.exit(app.exec_())
"""

"""
# open GUI window
if __name__ == '__main__':
    window()
"""
