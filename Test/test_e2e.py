import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from utilities.base import BaseClass

class Testone(BaseClass):

     def teste2e(self,Invoke):

         self.driver.find_element_by_css_selector("a[href*='shop']").click()
         products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
         for product in products:
             productName = product.find_element_by_xpath("div/h4/a").text
             if productName == "Blackberry":
                 product.find_element_by_xpath("div/button").click()

         self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
         self.driver.find_element_by_css_selector("//button[@class='btn btn-success']").click()
         self.driver.find_element_by_id("country").send_keys("ind")
         wait = WebDriverWait(self.driver, 7)
         wait.until(expected_conditions.presence_of_element_loacted((By.LINK_TEXT, "India")))
         self.driver.find_element_by_link_text("India").click()
         self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
         self.driver.find_element_by_css_selector("[type='submit']").click()
         succesText = self.driver.find_element_by_class_name("alert-success").text
         assert "Success! Thank you!" in succesText
         self.driver.get_screenshot_as_file("screen.png")