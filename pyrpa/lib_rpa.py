# -*- coding: utf-8 -*-
"""
Library for RPA functions like image detection

@author: python-rpa-dev

Date        Author          Info
-----------------------------------------------------------------------
2022.06.20  python-rpa-dev  Initial Version
2022.06.22  python-rpa-dev  Added class definition

"""

import logging
import cv2 as cv
import numpy as np
import pyautogui
import imutils
import time



logger = logging.getLogger(__name__)

def set_tmp_dir(dir_path: str):
    """ set temporary directory for image files """

    global tmp_dir

    tmp_dir = dir_path
    logger.info("temp dir set to %s", tmp_dir)


def set_def_scale(scale: float):
    """ set default scale for resizing image files """
    global def_scale

    def_scale = scale
    logger.info("default scale set to %s", def_scale)


def set_def_max_wait(max_wait: float):
    """ set default maximum wait time for image recognition """
    global def_max_wait

    def_max_wait = max_wait
    logger.info("max wait set to %s", def_max_wait)


def init_queue():
    """ initialize simple queue """
    global result_queue
    global save_points

    result_queue = []
    save_points = {}


def add_queue(result):
    """ append queue element """
    state = False if result is None else True
    result_queue.append([state, result])


def end_of_queue():
    """ display last queue element """
    return result_queue[-1]


def end_of_queue_state():
    """ display state of last queue element: True or False """
    return result_queue[-1][0]


def save_queue(label):
    """ save current element of queue """
    save_points[label] = result_queue[-1]


def restore_queue(label):
    """ restore saved element of queue """
    result_queue.append(save_points[label])



def type_message(message, sleep=1):
    """ type message to the GUI """
    pyautogui.typewrite(message)

    time.sleep(sleep)


def load_image(image_path):
    """ load image from file into memory """
    full_path = tmp_dir + '/' + image_path

    logger.info("load image %s", full_path)
    image = cv.imread(full_path)

    # check if image is available
    if image is None:
        logger.error("Image %s not found", full_path)

    return image


def resize_image(image, scale):
    """ resize image according to scale """
    resized = imutils.resize(image, width=int(image.shape[1] * scale))

    return resized


def locate_image(image, confidence=0.8):
    """ locate image on screen """
    positions = None

    # using cv2 to identify image
    imglocation = pyautogui.locateAllOnScreen(image, grayscale=False, confidence=confidence)
    positions = list(imglocation)

    logger.debug("Positions %s", positions)

    return positions


def find_image(image_paths, confidence=0.8, scale=None):
    """ find position of 1 or more images """
    positions = None
    images = {}
    scale = scale if scale is not None else def_scale  # set scale to default value if empty

    # load image
    for image_path in image_paths:
        logger.debug("Image %s", image_path)
        images[image_path] = load_image(image_path)

    # locate image
    for image_path in images:
        image = images[image_path]
        logger.debug("Locate Image %s", image_path)
        positions = locate_image(resize_image(image, scale), confidence)

        if len(positions):
           break

    return positions


def wait_for_image(image_paths, confidence=0.8, max_wait=None, sleep=1, scale=None):
    """
    waiting for location of any image in a list
      - set scale to default value if empty
      - set max wait time to default value if empty
    """
    positions = None
    images = {}
    scale = scale if scale is not None else def_scale
    max_wait = max_wait if max_wait is not None else def_max_wait

    """ load image(s) """
    for image_path in image_paths:
        logger.debug("Image %s", image_path)
        images[image_path] = load_image(image_path)

    start = time.time()
    count = 0

    while time.time() - start < max_wait:
        count += 1
        logger.info('Loop count: %s', count)

        """ locate image(s) """
        for image_path in images:
            image = images[image_path]
            logger.debug("Locate Image %s", image_path)

            positions = locate_image(resize_image(image, scale), confidence)

            if len(positions):
                break

        if len(positions):
            break

        time.sleep(sleep)

    end = time.time()

    logger.info('Elapsed time: %s', end - start)

    add_queue(positions)

    return positions



def wait_and_click(image_paths, confidence=0.8, max_wait=None, sleep=1, scale=None):
    """ 
    find any image and click it
     - set scale to default value if empty
     - set max wait time to default value if empty
    """
    point = None
    scale = scale if scale is not None else def_scale
    max_wait = max_wait if max_wait is not None else def_max_wait

    positions = wait_for_image(image_paths, confidence, max_wait, sleep, scale)

    logger.debug("Positions %s", positions)

    if len(positions):
        point = pyautogui.center(positions[0])

        pyautogui.moveTo(point.x, point.y)
        pyautogui.click(point.x, point.y)

        logger.debug("Point clicked %s", point)

        time.sleep(sleep)

    add_queue(point)

    return point


""" old code, can be phased out """
def find_scaled_image(image_path, confidence=0.8, tries=1, sleep=1, fixed_scale=None):
    positions = None
    full_path = tmp_dir + '/' + image_path
    scale_low = 0.7
    scale_high = 1.0
    scale_step = 5

    if fixed_scale is not None:
        logger.info("Fixed scale: %s", fixed_scale)
        scale_low = fixed_scale
        scale_high = fixed_scale
        scale_step = 1

    logger.info("load image %s", full_path)

    image = cv.imread(full_path)

    if image is None:
        logger.error("Image %s not found", full_path)
        return positions

    for scale in np.linspace(scale_low, scale_high, scale_step)[::-1]:
        logger.debug("Scale %s", scale)

        for attempt in range(tries):
            logger.debug("Attempt out of %s/%s", attempt + 1, tries)

            # resize the image according to the scale, and keep track
            # of the ratio of the resizing
            resized = imutils.resize(image, width=int(image.shape[1] * scale))

            # r = image.shape[1] / float(resized.shape[1])
            # if the resized image is smaller than the template, then break
            # from the loop

            imglocation = pyautogui.locateAllOnScreen(resized, grayscale=False, confidence=confidence)
            positions = list(imglocation)
            # return scale as result?

            logger.debug("Positions %s", positions)

            if len(positions):
               break

            time.sleep(sleep)

        if len(positions):
           break

    return positions, scale


# find image and click it
def find_and_click(image_path, confidence=0.8, tries=1, sleep=1, fixed_scale=None):
    point = None
    positions, scale = find_scaled_image(image_path, confidence, tries, sleep, fixed_scale)

    if len(positions):
       point = pyautogui.center(positions[0])
       logger.debug("Point %s", point)

       pyautogui.click(point.x, point.y)

       time.sleep(sleep)

    return point, scale


# find image on click it - can be used in a loop
def find_and_click_all(image_path, confidence=0.8, tries=1, sleep=1, fixed_scale = None):
    point, scale = find_and_click(image_path, confidence, tries, sleep, fixed_scale) 

    return point


class Robotic_Process_Automation():
    def __init__(self, name: str, tmp_dir: str, scale: float, max_wait: float):
        self.name = name
        self.tmp_dir = tmp_dir
        self.scale = scale
        self.max_wait = max_wait

        set_tmp_dir(self.tmp_dir)
        set_def_scale(self.scale)
        set_def_max_wait(self.max_wait)

        init_queue()

    def press(sefl, keys, presses=1, interval=0.0):
        """ send pressed keys to gui """
        pyautogui.press(keys=keys, presses=presses, interval=interval)

    def wait_for_image(self, image_paths, confidence=0.8, max_wait=None, sleep=1, scale=None):
        return wait_for_image(image_paths, confidence, max_wait, sleep, scale)

    def wait_and_click(self, image_paths, confidence=0.8, max_wait=None, sleep=1, scale=None):
        """ 
        find any image and click it
         - set scale to default value if empty
         - set max wait time to default value if empty
        """
        return wait_and_click(image_paths, confidence, max_wait, sleep, scale)

    def sleep(self, wait):
        time.sleep(wait)

    def end_of_queue_state(self):
        return end_of_queue_state()

    def save_queue(self, label):
        save_queue(label)

    def restore_queue(self, label):
        restore_queue(label)


if __name__ == "__main__":
    """ setup logging capabilities """
    logging.basicConfig(
        format='%(asctime)s [%(filename)s:%(lineno)-5s] %(levelname)-5s - %(funcName)-20s - %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S',
        level=logging.DEBUG
        )

    rpa = Robotic_Process_Automation(
        name='test',
        tmp_dir='../tmp',
        scale=1.0,
        max_wait=10
        )

    rpa.wait_and_click(['logo_nexters.png', 'logo_nexters.png'])

    rpa.save_queue('test')

    logger.debug("End of Queue %s", end_of_queue())
    logger.debug("End of Queue State%s", end_of_queue_state())

    rpa.restore_queue('test')
    rpa.sleep(10)

#    set_tmp_dir('./tmp')
#    set_def_scale(1.0)
#    set_def_max_wait(10)

#    init_queue()

#    positions = find_image(['logo_nexters.png', 'logo_nexters.png'])

#    wait_for_image(['logo_nexters.png', 'logo_nexters.png'])

#    save_queue('test')

#    wait_and_click(['btn_guild.png'])

#    logger.debug("End of Queue %s", end_of_queue())
#    logger.debug("End of Queue State%s", end_of_queue_state())

#    restore_queue('test')

    logger.debug("End of Queue %s", end_of_queue())
    logger.debug("End of Queue State%s", end_of_queue_state())

#   positions, scale = find_scaled_image('logo_nexters.png')
#   point, scale     = find_and_click('logo_nexters.png', fixed_scale = scale)
#   pyautogui.press('esc', presses=3)
