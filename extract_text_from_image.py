"""
This module helps to extract text present on the image &
storing that text to json file
It has methods like image_to_text, create_file, write_result_file
"""
import pytesseract
import cv2
import argparse
from datetime import datetime
import os
import json


def image_to_text(image):
    """
    It provides text present on image
    :param image: ndarray
        it is an ndarray object returned by imread method.
    :return: string
        it returns text present on image
    """
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\\Tesseract-OCR\\tesseract.exe'
    text_from_image = pytesseract.image_to_string(image, lang='eng')
    return text_from_image


def create_file(start, extension):
    """
    It creates file with provided start & extension
    :param start: string
    initial of file name
    :param extension: string
    extension of file
    :return: string
    name of file
    """
    curtime = datetime.now()
    date_time = curtime.strftime("%d%m%y%H%M%S")
    filename = start + date_time + extension
    return filename


def write_result_file(result, start, extension):
    """
    It writes result into file
    :param result: string
    it is text returned by image_to_text function
    :param start: string
    initial of file
    :param extension: string
    Extension of file
    :return: It doesn't return.
    """
    filename = create_file(start, extension)
    result_dir = "store_result"
    path = os.path.join(os.getcwd(), result_dir)
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    os.chdir(path)
    result = {"result_text": result}
    f = open(filename, "w")
    json.dump(result, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass an image, start & extension of file ")
    parser.add_argument('image_name', help="Name of image file from you want to extract text")
    parser.add_argument('start', help="starting string of file")
    parser.add_argument('extension', help="extension of file")

    arg = parser.parse_args()
    image1 = cv2.imread(arg.image_name)
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    result_string = image_to_text(image1)
    write_result_file(result_string, arg.start, arg.extension)
