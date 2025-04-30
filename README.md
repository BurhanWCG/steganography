Python Image Steganography Project
Image Steganography is a python project in which we hide the secret message inside any image using Tkinter and the PIL module. Let’s start the development.

What is Image Steganography?
Steganography is the process of hiding a secret message which is text-based data within non-text files like image file, audio, video file etc. In such a way someone cannot know the presence of a hidden message in a particular file. The main purpose of Steganography is to maintain secret communication between two people. It generally refers to encoding and decoding. So in this image Steganography project, we will encode and decode the data into an image file.

Python Image Steganography – Project Details
Image steganography is a GUI-based project in which we are hiding a secret message within the image using encoding and decoding functions. We are creating a window in which there are two buttons: encoding and decoding.

For encoding, select any image, this image will be converted into png format. Type message in the message box then it will convert into base64, merge this encoded string into image and the user can save the image where he/she wants.

For decoding, select the image which is encoded, the base64 string will get separated by decoding, and by Tkinter module hidden text is shown in the textbox.

Project Prerequisite
This project requires good knowledge of python and the Tkinter library. Tkinter is the python binding to the Tk toolkit which is used across many programming languages for building the Graphical user interface which is a GUI.

Also, we require a PIL module. This is the images module from the pillow. The PIL module helps to open, manipulate and save many different forms of images.

Use the following command to install PIL

python -m pip install pillow
