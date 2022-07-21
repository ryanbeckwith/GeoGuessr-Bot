""" 
GeoGuessr Bot
Author: Sohom Sen
Email: sohom416@hotmail.com
Current Version: 0.2-alpha
"""

#imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from inputs import maps, options, checkCustom, checkMap, checkOptions
import time
import os
from dotenv import load_dotenv
import yagmail
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

load_dotenv()

# Environment varible declarations
CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')
GGUSERNAME = os.getenv('GGUSERNAME')
GGPASSWORD = os.getenv('GGPASSWORD')
GGEMAILTO = os.getenv('GGEMAILTO').split(",")
GGEMAILFROM = os.getenv('GGEMAILFROM')
GGEMAILSENDER = os.getenv('GGEMAILSENDER')
GGEMAILFROMPASS = os.getenv('GGEMAILFROMPASS')
INVITE_XPATH = "//button[@data-qa='invite-friends-button']"

class GeoGuessorBot():
    def __init__(self):
        # Initializes Chrome driver and browser functions
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-sandbox')      
        chrome_options.add_argument('--disable-dev-shm-usage')
        print(CHROMEDRIVER_PATH)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),
                                       options=chrome_options)
        # self.driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)
        print("Bot Initialized")
    
    def login(self):
        self.driver.get("https://www.geoguessr.com/signin")
        emailField = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']")))
        emailField.send_keys(GGUSERNAME)
        passField = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
        passField.send_keys(GGPASSWORD)
        loginButton = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='login-cta-button']")))
        loginButton.click()

        print("GeoGuessr login successful.")
        time.sleep(1)

    def set_time_limit(self, time_limit):
        # TODO: implement by clicking and dragging on the slider to the desired position
        pass
        # time_div = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='styles_rangeslider__y45WS styles_variantDefault__vmnCV']")))
        # self.driver.execute_script("arguments[0].setAttribute('aria-valuenow', arguments[1])", time_div, time_limit)
    
    def default(self, time_limit):
        # This function is called when the game setting is set to default by the user. 
        self.set_time_limit(time_limit)
        invite = self.wait.until(EC.element_to_be_clickable((By.XPATH, INVITE_XPATH)))
        invite.click()
        time.sleep(5)

    def no_move(self, time_limit):
        # This function is called when the game setting is set to no move by the user.
        self.set_time_limit(time_limit)
        nmSelect = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='No move']")))
        nmSelect.click()
        invite = self.wait.until(EC.element_to_be_clickable((By.XPATH, INVITE_XPATH)))
        invite.click()
        time.sleep(5)    
    
    def no_zoom(self, time_limit):
        # This function is called when the game setting is set to no zoom by the user.
        self.set_time_limit(time_limit)
        nzSelect = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='No zoom']")))
        nzSelect.click()
        invite = self.wait.until(EC.element_to_be_clickable((By.XPATH, INVITE_XPATH)))
        invite.click()
        time.sleep(5)   

    def no_move_zoom(self, time_limit):
        # This function is called when the game setting is set to no move, no zoom by the user.
        self.set_time_limit(time_limit)
        nzSelect = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='No move, no zoom']")))
        nzSelect.click()
        invite = self.wait.until(EC.element_to_be_clickable((By.XPATH, INVITE_XPATH)))
        invite.click()
        time.sleep(5)
    
    def no_move_zoom_pan(self, time_limit):
        # This function is called when the game setting is set to no move, no pan, no zoom by the user.
        self.set_time_limit(time_limit)
        nzSelect = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='No move, no pan, no zoom']")))
        nzSelect.click()   
        invite = self.wait.until(EC.element_to_be_clickable((By.XPATH, INVITE_XPATH)))
        invite.click()
        time.sleep(5)

    def game_setting(self):
        # Function for checking if the game rule menu is being displayed. Returns False if the element is not found.
        try:
            self.driver.find_element_by_xpath("//div[@class='game-settings__detailed-settings']")
        except NoSuchElementException:
            return False
        return True
 
    def map_generator(self, map, option, time_limit):
        # Function for generating GeoGuessr game links
        map_checked = checkMap(map) # checks for a valid map
        if map_checked in maps:
            map_final = checkCustom(map) # checks for custom GeoGuessr Maps (unofficial ones have unique hash values instead of strings)
            option = checkOptions(option) # checks for a valid rule option
            if option in options:
                pass
            elif option == False:
                return False
            self.driver.get("https://www.geoguessr.com/maps/" + map_final + "/play")
            # challenge = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='radio-box']//div[@class='radio-box__illustration']")))
            # challenge = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='radio-box']//div[@class='radio-box_illustration___Yw_M']")))
            # challenge = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='radio-box_illustration___Yw_M']")))
            challenge = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='radio-box_root__ka_9S']")))
            # challenge = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//img[@alt='Challenge']")))
            # challenge = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@name='game-type']")))
            challenge.click()
        if map_checked == False:
            return False

        # Clicks default button initially
        defaultBtn = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@class='toggle_toggle__hwnyw']")))
        defaultBtn.click()

        link = None
        if option in options:
            if option == "default":
                # Generates game link with default settings.
                if GeoGuessorBot.game_setting(self):
                    defaultBtn = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='game-settings__checkbox']")))
                    defaultBtn.click()
                    GeoGuessorBot.default(self, time_limit)
                else:
                    GeoGuessorBot.default(self, time_limit)
                link = self.driver.find_element_by_xpath("//input[@name='copy-link']").get_attribute('value')
            elif option == "nm":
                # Generates game link with the no move setting.
                if GeoGuessorBot.game_setting(self):
                    GeoGuessorBot.no_move(self, time_limit)
                else:
                    noDefault = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='game-settings__checkbox']")))
                    noDefault.click()
                    GeoGuessorBot.no_move(self, time_limit)
                link = self.driver.find_element_by_xpath("//input[@name='copy-link']").get_attribute('value')
            elif option == "nz":
                # Generates game link with the no move zoom setting.
                if GeoGuessorBot.game_setting(self):
                    GeoGuessorBot.no_zoom(self, time_limit)
                else:
                    noDefault = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='game-settings__checkbox']")))
                    noDefault.click()
                    GeoGuessorBot.no_zoom(self, time_limit)
                link = self.driver.find_element_by_xpath("//input[@name='copy-link']").get_attribute('value')
            elif option == "nmz":
                # Generates game link with the no move, no zoom setting.
                if GeoGuessorBot.game_setting(self):
                    GeoGuessorBot.no_move_zoom(self, time_limit)
                else:
                    noDefault = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='game-settings__checkbox']")))
                    noDefault.click()
                    GeoGuessorBot.no_move_zoom(self, time_limit)
                link = self.driver.find_element_by_xpath("//input[@name='copy-link']").get_attribute('value')
            elif option == "nmpz":
                # Generates game link with the no move, no pan, no zoom setting.
                if GeoGuessorBot.game_setting(self):
                    GeoGuessorBot.no_move_zoom_pan(self, time_limit)
                else:
                    noDefault = self.wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='game-settings__checkbox']")))
                    noDefault.click()
                    GeoGuessorBot.no_move_zoom_pan(self, time_limit)
                link = self.driver.find_element_by_xpath("//input[@name='copy-link']").get_attribute('value')

        return link

def main():
    browser = GeoGuessorBot() #initiates GeoGuessrBot
    browser.login()
    map = "diverse-world"
    option = "default"
    time_limit = 600
    geoguessrlink = browser.map_generator(map, option, time_limit) # Generates link
    print("Game link generated:") 
    print(geoguessrlink) # User receives the generated game link
    print("Emailing to " + ", ".join(GGEMAILTO))
    msg = MIMEText(geoguessrlink, 'plain')
    msg['Subject'] = "Weekly Geoguessr Link"
    msg['From'] = GGEMAILSENDER

    with SMTP_SSL('smtp.zoho.com') as smtp_server:
        smtp_server.login(GGEMAILFROM, GGEMAILFROMPASS)
        smtp_server.sendmail(GGEMAILFROM, GGEMAILTO, msg.as_string())

    # yag = yagmail.SMTP(GGEMAILFROM, GGEMAILFROMPASS)
    # yag.send(GGEMAILTO, "Weekly Geoguessr Link", geoguessrlink)

if __name__ == "__main__":
    main()