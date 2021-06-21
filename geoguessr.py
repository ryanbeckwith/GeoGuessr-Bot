""" 
GeoGuessr Bot
Author: Sohom Sen
Email: sohom416@hotmail.com
"""

#imports

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from dev import PATH, username, password
from inputs import maps, options, checkCustom, checkMap, checkOptions
import time, sys

class GeoGuessorBot():
    # Initializes Chrome driver and browser functions
    def __init__(self):
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(PATH)
        self.wait = WebDriverWait(self.driver,10)
        self.busy = False
        print("Bot Initialized")

    # Function for logging in GeoGuessrPro account.
    def login(self):
        self.driver.get("https://www.geoguessr.com/")
        loginButton = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Log in']")))
        loginButton.click()
        emailField = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']")))
        emailField.send_keys(username)
        passField = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
        passField.send_keys(password)
        enter = self.driver.find_element_by_xpath("//button[@type='submit']")
        enter.click()

        print("GeoGuessr login successful.")
        time.sleep(1)
    
    def default(self):
        invite = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))
        invite.click()
        start = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='button button--medium button--primary margin--top']")))
        start.click()
        time.sleep(5)

    def no_move(self):
        nmSelect = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='No move']")))
        nmSelect.click()
        invite = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))
        invite.click()
        start = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='button button--medium button--primary margin--top']")))
        start.click()
        time.sleep(5)    
    
    def no_zoom(self):
        nzSelect = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='No zoom']")))
        nzSelect.click()
        invite = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))
        invite.click()
        start = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='button button--medium button--primary margin--top']")))
        start.click()
        time.sleep(5)   

    def no_move_zoom(self):
        nzSelect = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='No move, no zoom']")))
        nzSelect.click()
        invite = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))
        invite.click()
        start = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='button button--medium button--primary margin--top']")))
        start.click()
        time.sleep(5)
    
    def no_move_zoom_pan(self):
        nzSelect = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='No move, no pan, no zoom']")))
        nzSelect.click()   
        invite = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@type='button']")))
        invite.click()
        start = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='button button--medium button--primary margin--top']")))
        start.click()
        time.sleep(5)

    def game_setting(self):
        try:
            self.driver.find_element_by_xpath("//div[@class='game-settings__detailed-settings']")
        except NoSuchElementException:
            return False
        return True


    # Function for generating GeoGuessr game links
    def map_generator(self, map, option):
        map = checkCustom(map) # checks for custom GeoGuessr Maps (unofficial ones have unique hash values instead of strings)
        map = checkMap(map) # checks for a valid map
        if map in maps:
            option = checkOptions(option) # checks for a valid rule option
            if option in options:
                pass
            elif option == "Invalid Option.":
                return option
            self.driver.get("https://www.geoguessr.com/maps/" + map +"/play")
            challenge = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='radio-box']//div[@class='radio-box__illustration']")))
            challenge.click()
        if map == "Invalid Map.":
            return map

        if option in options:
            if option == "default":
                # Generates game link with default settings.
                if GeoGuessorBot.game_setting(self) == True:
                    GeoGuessorBot.default(self)
                else:
                    noDefault = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='checkbox__mark checkbox__mark--dark']")))
                    noDefault.click()
                    GeoGuessorBot.default(self)
                link = self.driver.current_url
                return link
            elif option == "nm":
                # Generates game link with the no move setting.
                if GeoGuessorBot.game_setting(self) == True:
                    GeoGuessorBot.no_move(self)
                else:
                    noDefault = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='checkbox__mark checkbox__mark--dark']")))
                    noDefault.click()
                    GeoGuessorBot.no_move(self)
                link = self.driver.current_url
                return link
                
            elif option == "nz":
                # Generates game link with the no move zoom setting.
                if GeoGuessorBot.game_setting(self) == True:
                    GeoGuessorBot.no_zoom(self)
                else:
                    noDefault = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='checkbox__mark checkbox__mark--dark']")))
                    noDefault.click()
                    GeoGuessorBot.no_zoom(self)
                link = self.driver.current_url
                return link
            elif option == "nmnz":
                # Generates game link with the no move, no zoom setting.
                if GeoGuessorBot.game_setting(self) == True:
                    GeoGuessorBot.no_move_zoom(self)
                else:
                    noDefault = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='checkbox__mark checkbox__mark--dark']")))
                    noDefault.click()
                    GeoGuessorBot.no_move_zoom(self)
                link = self.driver.current_url
                return link

            elif option == "nmnpnz":
                # Generates game link with the no move, no pan, no zoom setting.
                if GeoGuessorBot.game_setting(self) == True:
                    GeoGuessorBot.no_move_zoom_pan(self)
                else:
                    noDefault = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@class='checkbox__mark checkbox__mark--dark']")))
                    noDefault.click()
                    GeoGuessorBot.no_move_zoom_pan(self)
                link = self.driver.current_url
                return link



def main():
    browser = GeoGuessorBot()
    browser.login()
    map,option = input("Enter the Map you want and rule: ").split() 
    geoguessrlink = browser.map_generator(map,option)
    if geoguessrlink == "Invalid Map." or geoguessrlink == "Invalid Option.":
        print("Error Occured. Either the map or rule is incorrect. Please run program again.")
        sys.exit()
    else:
        print("Game link generated:")
        print(geoguessrlink)
        exitKey = input("Press X to close program: ")
        if exitKey == "x":
            sys.exit()


if __name__ == "__main__":
    main()