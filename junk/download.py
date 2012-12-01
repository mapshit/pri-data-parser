#!/usr/bin/env python2
import os
import datetime
from selenium import webdriver
from time import sleep

def _driver_setup():
    desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
    desired_capabilities['name'] = 'Tompkins Trust'
    driver = webdriver.Remote(desired_capabilities=desired_capabilities,command_executor="http://localhost:4444/wd/hub")
    return driver

d = _driver_setup()
d.get('http://nirmalgrampuraskar.nic.in/Report/RptGPAwardedSummaryTill2010.aspx')
all_links = d.find_elements_by_xpath('//table[@class="Table"]/descendant::a')
for link in all_links:
    if link attribute contains 'g20', download it
    or just download everything. yeah.
