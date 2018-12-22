# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 10:59:27 2018

@author: RuoqinLo
"""

from selenium import webdriver
browser =webdriver.Chrome("./chromedriver")
browser.get("http://localhost:8000")

assert "django" in browser.title