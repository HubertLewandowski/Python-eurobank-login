import time
import unittest
from selenium import webdriver

class LoginPagTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='C:\TestFiles\chromedriver.exe')

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def test_header_login(self):
        driver = self.driver
        url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
        driver.get(url)

        header_text_site = driver.find_element_by_xpath('//*[@id="login_form"]/h1')
        header_text_site_name = header_text_site.text
        self.assertEqual(header_text_site_name, 'Wersja demonstracyjna serwisu eurobank online', f'Actual title differ from expected on a site : {url}')


    def test_button_dalej_is_diesabled_when_login_is_empty(self):
        driver = self.driver
        url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
        driver.get(url)

        form_input_login_box = driver.find_element_by_xpath('//*[@id="login_id"]')
        form_input_login_box.clear()


        login_dalej_button_tst = driver.find_element_by_xpath('//*[@id="login_next"]')
        login_dalej_button_tst_disabled = login_dalej_button_tst.get_property('disabled')
        self.assertEqual(login_dalej_button_tst_disabled, True, f'Actual state of button when place is empty : {login_dalej_button_tst_disabled} differ from expected True')

    def test_display_error_message_when_user_submit_less_than_8_signs_id(self):
        driver = self.driver
        url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
        driver.get(url)

        form_input_login_box = driver.find_element_by_xpath('//*[@id="login_id"]')
        form_input_login_box.clear()

        form_input_login_box.send_keys('1234567')
        ask_button = driver.find_element_by_xpath('//*[@id="login_id_container"]//*[@class ="i-hint-white tooltip widget-info"]')
        ask_button.click()

        warning_massage = driver.find_element_by_xpath('//*[@class="error"]')
        warning_massage_text = warning_massage.text
        self.assertEqual(warning_massage_text, 'identyfikator ma min. 8 znaków', f'Actual message is differ than expected one')

    def test_login_to_account(self):
        driver = self.driver
        url = 'http://demo.eurobank.pl/logowanie_etap_1.html'
        driver.get(url)

        login_input_place = driver.find_element_by_xpath('//*[@id="login_id"]')
        login_input_place.clear()
        login_text = '12345678'
        login_input_place.send_keys(login_text)

        login_dalej_button = driver.find_element_by_xpath('//*[@id="login_next"]')
        login_dalej_button.click()

        time.sleep(3)

        new_button_login = driver.find_element_by_xpath('//*[@id="login_next"]')
        new_button_login_text = new_button_login.text
        print(new_button_login_text)
        self.assertEqual(new_button_login_text, 'zaloguj się', 'Actual new button login text is differ than expected')

        login_button_to_remind_password = driver.find_element_by_xpath('//*[@id="ident_rem"]')
        login_button_to_remind_password.click()

        time.sleep(3)

        login_warning_text_function = driver.find_element_by_xpath('//*[@class="shadowbox-content contact-popup"]/div/h2')
        login_warning_text_function_text = login_warning_text_function.text
        self.assertEqual(login_warning_text_function_text, 'w wersji demonstracyjnej ta funkcja jest niedostępna', f'Actual login button text {login_warning_text_function_text}: differ from expected')

if __name__ == '__main__':
    unittest.main()