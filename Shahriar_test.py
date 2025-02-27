# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTest():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test(self):
    self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(1) > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-valid").send_keys("Shahriar ")
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) > .form-control").send_keys("Hasan")
    self.driver.find_element(By.CSS_SELECTOR, ".ng-pristine").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-untouched").send_keys("1990")
    assert self.driver.switch_to.alert.text == "Customer added successfully with customer id :6"
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.ID, "userSelect").click()
    dropdown = self.driver.find_element(By.ID, "userSelect")
    dropdown.find_element(By.XPATH, "//option[. = 'Shahriar Hasan']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-binding:nth-child(7)").click()
    self.driver.find_element(By.ID, "currency").click()
    dropdown = self.driver.find_element(By.ID, "currency")
    dropdown.find_element(By.XPATH, "//option[. = 'Dollar']").click()
    self.driver.find_element(By.CSS_SELECTOR, "#currency > option:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-dirty > button").click()
    assert self.driver.switch_to.alert.text == "Account created successfully with account Number :1016"
    self.driver.find_element(By.CSS_SELECTOR, ".btn-lg:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-scope:nth-child(6) > .ng-binding:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-scope:nth-child(1) > td > button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-scope:nth-child(1) > td > button").click()
    self.driver.find_element(By.CSS_SELECTOR, ".home").click()
    self.driver.find_element(By.CSS_SELECTOR, ".center:nth-child(1) > .btn").click()
    self.driver.find_element(By.ID, "userSelect").click()
    dropdown = self.driver.find_element(By.ID, "userSelect")
    dropdown.find_element(By.XPATH, "//option[. = 'Shahriar Hasan']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ng-binding:nth-child(5)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-lg:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".fixedTopBox > .btn:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("50000000")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-lg:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-control").send_keys("1000000")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
    self.driver.find_element(By.CSS_SELECTOR, ".logout").click()
  
