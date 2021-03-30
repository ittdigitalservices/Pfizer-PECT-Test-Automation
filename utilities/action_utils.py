from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class Driver_Actions:
    def __init__(self):
        pass

    def move_cursor_to_webelement(self, driver, xElement):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        action = ActionChains(driver)
        try:
            action.move_to_element(xElement)
            action.perform()
        except Exception as e:
            pass
        return driver


    def driver_page_down_action(self, driver, my_iterator=0):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        action = ActionChains(driver)
        try:
            i = 0
            for i in range(int(my_iterator)):
                try:
                    action.send_keys(Keys.PAGE_DOWN)
                    action.perform()
                except Exception as e0:
                    pass

        except Exception as e1:
            pass
        return driver


    def driver_page_pause_action(self, driver):
        from selenium import webdriver
        from selenium.webdriver import ActionChains
        action = ActionChains(driver)
        try:
            action.send_keys(Keys.PAUSE)
            action.perform()
        except Exception as e1:
            pass
        return driver


class Test_Actions:
    def __init__(self):
        pass

    def mark_test_step_as_failed(self, message="Test Step Failed"):
        try:
            assert False
            print(message)
        except Exception as e:
            print(message)


