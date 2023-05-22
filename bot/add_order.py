from selenium import webdriver
from selenium.webdriver.common.by import By
from pymongo import MongoClient


client = MongoClient('localhost:27017', 27017)
db = client['Paymob']
collection = db['merchants']


class AddOrder(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(AddOrder, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get("https://fsm.paymob.com")

    def navigate_order_page(self):
        orders = self.find_element(By.CSS_SELECTOR, "li.pro-menu-item:nth-child(3) > div:nth-child(1)")
        orders.click()

        add_order = self.find_element(
            By.CSS_SELECTOR, ".transitioning > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2) > div:nth-child(1)")
        add_order.click()

    def fill_merchant_details(self):
        """
        Fill all the input fields in the merchant details page
        with the appropriate values from the database.

        No return.
        """
        # send merchant's name
        merchant_name = self.find_element(By.CSS_SELECTOR, ".grid > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
        merchant_name.clear()
        merchant_name.send_keys()

        # send merchant's id and click search
        merchant_id = self.find_element(By.CSS_SELECTOR, ".grow > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")
        merchant_id.clear()
        merchant_id.send_keys()
        search_id = self.find_element(By.CLASS_NAME, "mt-4")
        search_id.click()

        # send merchant's username
        merchant_username = self.find_element(By.CSS_SELECTOR, ".grid > div:nth-child(3) > div:nth-child(2) > input:nth-child(1)")
        merchant_username.clear()
        merchant_username.send_keys()

        # send branch number
        branch_no = self.find_element(By.CSS_SELECTOR, ".grid > div:nth-child(4) > div:nth-child(2) > input:nth-child(1)")
        branch_no.clear()
        branch_no.send_keys()

        # send branch code
        branch_code = self.find_element(By.CSS_SELECTOR, ".grid > div:nth-child(5) > div:nth-child(2) > input:nth-child(1)")
        branch_code.clear()
        branch_code.send_keys()

        # send phone number
        phone_number = self.find_element(By.CLASS_NAME, "form-control")
        phone_number.clear()
        phone_number.send_keys()

        # send category and pick first option from dropdown menu
        category = self.find_element(By.ID, "react-select-18-input")
        category.clear()
        category.send_keys()
        first_category_result = self.find_element(By.ID, "react-select-18-option-0")
        first_category_result.click()

        # click next page button
        next_page = self.find_element(By.CLASS_NAME, "bg-main")
        next_page.click()

    def fill_important_details(self):
        """
        Fill all the input fields in the important details page
        with the appropriate values from the database.

        No return.
        """
        # send errand channel and pick first option from dropdown menu
        errand_channel = self.find_element(By.ID, "react-select-9-input")
        errand_channel.clear()
        errand_channel.send_keys()
        first_errand_channel_result = self.find_element(By.ID, "react-select-9-option-0")
        first_errand_channel_result.click()

        # send pos type and pick first option from dropdown menu
        pos_type = self.find_element(By.ID, "react-select-15-input")
        pos_type.clear()
        pos_type.send_keys()
        first_pos_type_result = self.find_element(By.ID, "react-select-15-option-0")
        first_pos_type_result.click()

        # send number of elements
        no_of_elements = self.find_element(By.CSS_SELECTOR, ".focus\\:outline-none")
        no_of_elements.clear()
        no_of_elements.send_keys()

        # send department and pick first option from dropdown menu
        department = self.find_element(By.ID, "react-select-30-input")
        department.clear()
        department.send_keys()
        first_department_result = self.find_element(By.ID, "react-select-30-option-0")
        first_department_result.click()

        # send errand type and pick first option from dropdown menu
        errand_type = self.find_element(By.ID, "react-select-31-input")
        errand_type.clear()
        errand_type.send_keys()
        first_errand_type_result = self.find_element(By.ID, "react-select-31-option-0")
        first_errand_type_result.click()

        # click next page button
        next_page = self.find_element(By.CLASS_NAME, "bg-main")
        next_page.click()

    def fill_area_of_service_details(self):
        """
        Fill all the input fields in the area of service page
        with the appropriate values from the database.

        No return.
        """
        # send areas and pick first option from dropdown menu
        areas = self.find_element(By.ID, "react-select-39-input")
        areas.clear()
        areas.send_keys()
        first_areas_result = self.find_element(By.ID, "react-select-39-option-0")
        first_areas_result.click()

        # send merchant's address
        merchant_address = self.find_element(By.CSS_SELECTOR, ".grid > div:nth-child(4) > div:nth-child(2) > input:nth-child(1)")
        merchant_address.clear()
        merchant_address.send_keys()

        # send landmark
        landmark = self.find_element(By.CSS_SELECTOR, ".grid > div:nth-child(5) > div:nth-child(2) > input:nth-child(1)")
        landmark.clear()
        landmark.send_keys()

        # send comment
        comment = self.find_element(By.CSS_SELECTOR, "textarea.w-full")
        comment.clear()
        comment.send_keys()

        # send link
        link = self.find_element(By.CLASS_NAME, "bg-gray-100")
        link.send_keys()

        # click on "go to" button
        # go_to_link = self.find_element(By.CLASS_NAME, "save_btn")
        # go_to_link.click()

        # click next page button
        # next_page = self.find_element(By.CLASS_NAME, "bg-main")
        # next_page.click()

