from selenium import webdriver
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
        self.fail("Finish test")
        # User is invited to enter a new to-do item

        # User enters "Write text" into a text field

        # User presses Enter, page updates with new item in list

        # User is still invited to enter a new item

        # User enters "Read text" into field, presses Enter, page updates with 2 items

        # User needs webapp to remember list
        # user sees generated unique URL for this list, with helping message

        # User visits that generated URL, list is still there

        # User is satisfied, closes browser


if __name__ == "__main__":
    unittest.main(warnings="ignore")
