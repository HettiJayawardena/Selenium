#This Python script uses Chrome browser to Login to the https://opensource-demo.orangehrmlive.com/" and access the Welcome page
#and Logout from the page. Also unit-test hast been implemented
#To run the file successfully, please make sure chromedriver.exe file is in the same folder as this script.

#to run the file open the terminal on the folder where this script and chromedriver.exe files are present and use the command < python -m unittest >


from selenium import webdriver
import time
import unittest






class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.implicitly_wait(10)

        # maximize window during testing
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        self.driver.find_element_by_id("txtUsername").send_keys("Admin")

        self.driver.find_element_by_id("txtPassword").send_keys("admin123")

        self.driver.find_element_by_id("btnLogin").click()

        self.driver.find_element_by_id("welcome").click()  #

        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(4) #sleep for 4 seconds so user would see the logout process

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test has been completed")


if __name__ == '__main__':
    unittest.main


