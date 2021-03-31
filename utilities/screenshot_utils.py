#
# AUTHOR : ITTDigital
#
# coding=utf-8

import time
import allure
from allure_commons.types import AttachmentType

# check if a test has failed
from pytest_splinter.plugin import _take_screenshot


def test_failed_check(driver, scenario_name):
    import time
    import allure
    from allure_commons.types import AttachmentType
    if(driver == None):
        return None
    try:
        driver.maximize_window()
        screenshot = "./result/screenshot/"
        file_name = str(time.time())
        screenshot = screenshot + file_name + ".png"
        driver.save_screenshot(screenshot)
        time.sleep(3)
        allure.attach.file(screenshot, attachment_type=AttachmentType.PNG)
        time.sleep(2)
    except Exception as e:
        pass


def take_full_screenshot(driver, scenario_name):
    if(driver == None):
        return None
    driver.maximize_window()
    from Screenshot import Screenshot_Clipping
    screen_img_path = "./result/screenshot/"
    img_file_name = str(time.time())
    img_file_name = img_file_name + ".png"
    browserScreenShot = Screenshot_Clipping.Screenshot()
    img_url = browserScreenShot.full_Screenshot(driver, save_path=screen_img_path, image_name=img_file_name)
    # print(img_url)
    # allure.attach.file(source=img_url, name=scenario_name, attachment_type=AttachmentType.PNG)
    allure.attach.file(img_url, attachment_type=AttachmentType.PNG)
    # driver.quit()


def take_test_screen_shot(driver, scenario_name):
    import time
    import allure
    from allure_commons.types import AttachmentType
    if (driver == None):
        return None
    try:
        # time.sleep(5)
        # driver.maximize_window()
        screenshot = "./result/screenshot/"
        file_name = str(time.time())
        screenshot = screenshot + file_name + ".png"
        driver.save_screenshot(screenshot)
        time.sleep(3)
        allure.attach.file(screenshot, attachment_type=AttachmentType.PNG)
        time.sleep(2)
    except Exception as e:
        pass
    return driver
