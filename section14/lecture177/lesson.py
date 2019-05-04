#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_binary

# driver = webdriver.Chrome()
# driver.get('https://www.google.com/')
# time.sleep(5)
# search_box = driver.find_element_by_name("q")
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5)
# driver.quit()


class PythonOrgTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        self.driver.get('http://www.python.org')

        # titleに'Python'があるか
        self.assertIn('Python', self.driver.title)

        # Downloadsタブをクリックできるか
        self.driver.find_element_by_link_text('Downloads').click()
        # Looking for a specific release? があるか
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'widget-title')))
        self.assertEqual('Looking for a specific release?', element.text)

        # Documentationタブをクリックできるか
        self.driver.find_element_by_link_text('Documentation').click()
        # Browse the docs があるか
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'call-to-action')))
        self.assertIn('Browse the docs', element.text)
        # search box
        element = self.driver.find_element_by_name('q')
        element.clear()
        element.send_keys('pycon')
        element.send_keys(Keys.RETURN)
        assert 'No result found' not in self.driver.page_source


# CMD実行の場合、以下を記載し、CMDか通常のPycharm実行
if __name__ == '__main__':
    unittest.main()
