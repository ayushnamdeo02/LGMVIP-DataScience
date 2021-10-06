#Image to Sketch Converter using OPEN CV python library

import cv2
import numpy as np
from PIL import Image
import streamlit as st
def sketch(our_image):
    image = np.array(our_image.convert("RGB"))      # reading image in raw array format
    grey_img = cv2.cvtColor(
        image, cv2.COLOR_RGB2GRAY
    )                                               # Using cvtColor method to Convert RGB to Gray colorscale
    invert = cv2.bitwise_not(grey_img)              # Using bitwise_not method to invert the greyscale `image
    blur = cv2.GaussianBlur(
        invert, (35, 35), 0
    )                                               # Using GaussianBlur method to blur the inverted image
    invertedblur = cv2.bitwise_not(
        blur
    )                                               # Again using bitwise_not method to invert the blurred image
    return cv2.divide(
        grey_img, invertedblur, scale=256.0
    )                                               # performing bit-wise division between the grayscale image 
                                                    #   and the inverted-blurred image to obtain sketch image.


def main():
    st.subheader("Image To Pencil Art Conventer ")   # app subheader
    st.text("Build with Streamlit and OpenCV Project By Ayush LETSGROWMORE")
    image_file = st.file_uploader(
        "Upload Image", type=["jpg", "png", "jpeg"]
    )                                                # To get the user uploaded image
    if image_file is not None:
        our_image = Image.open(image_file)
        st.text("Original Image")
        st.image(our_image)                          # displays original image to the screen
        result = sketch(
            our_image
        )                                            # calls the sketch() function to convert the image to pencil drawing
        st.text("Sketch Image")
        st.image(result)                             # displays pencil drawing output image to the screen


if __name__ == "__main__":
    main()        