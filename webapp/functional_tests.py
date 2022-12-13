import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.url = "http://localhost:8000"

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_fill_list_and_retrieve_it_by_unique_url(self):
        self.browser.get(self.url)
        # User sees page title that has mention of to-do
        self.assertIn("Todo", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("Todo", header_text)
        # User is invited to enter a new to-do item
        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a todo item")
        # User enters "Write text" into a text field
        input_box.send_keys("Write text")
        # User presses Enter, page updates with new item in list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        # User sees 1 item in the list on page
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == "1: Write text" for row in rows))
        # User is still invited to enter a new item

        # User enters "Read text" into field, presses Enter, page updates with 2 items
        self.fail("Finish test")
        # User needs webapp to remember list
        # user sees generated unique URL for this list, with helping message

        # User visits that generated URL, list is still there

        # User is satisfied, closes browser


if __name__ == "__main__":
    unittest.main(warnings="ignore")
