# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 10:59:27 2018
@author: RuoqinLo
"""

from selenium import webdriver
from selenium.webdriver.common.keys import keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("./chromedriver")
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        
        self.assertIn('To-do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-do', header_text)
        
        #User is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )
        
        #User types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')
        
        #After user hits enter,the item is listed in a table
        inputbox.send_keys(keys.ENTER)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1:Buy peacock feathers' for row in rows)
                )
        
        #Afert this, there's still a text box for user to add items
        self.fail('Finish the test')
 
  
        
if __name__=='__main__':
    unittest.main(warnings='ignore')