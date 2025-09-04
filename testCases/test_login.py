from asyncio.log import logger
import time
from pageObjects.login_page import LoginPage
from utilities.readProperties import get_password, get_username, get_url
from utilities.customLogger import create_logger

LOGGER = create_logger(filename='Logs/logs.log', filemode='a')

class Test001Login:

    BaseUrl = get_url()
    username = get_username()
    password = get_password()

    def test_verify_login_page_title(self, setup):
        LOGGER.info("************ Test001Login ************")
        LOGGER.info("************ test_verify_login_page_title STARTED ************")
        driver1 = setup
        driver1.get(url=self.BaseUrl)
        time.sleep(2)
        expected_title = "Test Login | Practice Test Automation"
        if driver1.title == expected_title:
            LOGGER.info("************ test_verify_login_page_title PASSED ************")
            assert True
        else:
            driver1.save_screenshot(filename="Screenshots/test_verify_login_page_title.png")
            LOGGER.error("************ test_verify_login_page_title FAILED ************")
            assert False

    def test_login_positive(self, setup):
        LOGGER.info("************ test_login_positive STARTED ************")
        driver1 = setup
        driver1.get(url=self.BaseUrl)

        # Create an instance of LoginPage
        lp = LoginPage(driver=driver1)
        time.sleep(2)
        lp.set_username(username=self.username)
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)
        if driver1.title == 'Logged In Successfully | Practice Test Automation':
            # print(f'Login successful for user: student')
            lp.logout()
            time.sleep(2)
            LOGGER.info("************ test_login_positive PASSED ************")
            assert True
        else:
            LOGGER.error("************ test_login_positive FAILED ************")
            driver1.save_screenshot(filename="Screenshots/test_login_positive.png")
            assert False

    def test_negative_username(self, setup):
        LOGGER.info("************ test_negative_username STARTED ************")
        driver = setup
        driver.get(url=self.BaseUrl)
        time.sleep(2)

        lp = LoginPage(driver=driver)
        lp.set_username(username="incorrectUser")
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)

        if "Your username is invalid!" in driver.page_source:
            # driver.quit()
            LOGGER.info("************ test_negative_username PASSED ************")
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_negative_username.png")
            # driver.quit()
            LOGGER.error("************ test_negative_username FAILED ************")
            assert False


class Test002Login:
    BaseUrl = get_url()
    username = get_username()
    password = get_password()

    def test_verify_login_page_title2(self, setup):
        LOGGER.info("************ Test002Login ************")
        LOGGER.info("************ test_verify_login_page_title2 STARTED ************")
        driver1 = setup
        driver1.get(url=self.BaseUrl)
        time.sleep(2)
        expected_title = "Test Login | Practice Test Automation"
        if driver1.title == expected_title:
            LOGGER.info("************ test_verify_login_page_title PASSED ************")
            assert True
        else:
            driver1.save_screenshot(filename="Screenshots/test_verify_login_page_title2.png")
            LOGGER.error("************ test_verify_login_page_title2 FAILED ************")
            assert False

    def test_login_positive2(self, setup):
        LOGGER.info("************ test_login_positive2 STARTED ************")
        driver1 = setup
        driver1.get(url=self.BaseUrl)

        # Create an instance of LoginPage
        lp = LoginPage(driver=driver1)
        time.sleep(2)
        # lp.set_username(username=self.username)
        lp.set_username(username='username')
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)
        if driver1.title == 'Logged In Successfully | Practice Test Automation':
            # print(f'Login successful for user: student')
            lp.logout()
            time.sleep(2)
            LOGGER.info("************ test_login_positive2 PASSED ************")
            assert True
        else:
            LOGGER.error("************ test_login_positive2 FAILED ************")
            driver1.save_screenshot(filename="Screenshots/test_login_positive2.png")
            assert False

    def test_negative_username2(self, setup):
        LOGGER.info("************ test_negative_username2 STARTED ************")
        driver = setup
        driver.get(url=self.BaseUrl)
        time.sleep(2)

        lp = LoginPage(driver=driver)
        lp.set_username(username="incorrectUser")
        time.sleep(2)
        lp.set_password(password=self.password)
        time.sleep(2)
        lp.login()
        time.sleep(2)

        if "Your username is invalid!" in driver.page_source:
            # driver.quit()
            LOGGER.info("************ test_negative_username2 PASSED ************")
            assert True
        else:
            driver.save_screenshot(filename="Screenshots/test_negative_username2.png")
            # driver.quit()
            LOGGER.error("************ test_negative_username2 FAILED ************")
            assert False