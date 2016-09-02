from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_classifier_and_predict_with_it(self):
        # Gustav has heard about a cool new classification app.
        # He goes to check out the homepage.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention Peak Classifier
        self.assertIn('Welcome to Peak', self.browser.title)

        # He is invited to login or register and sees a welcome message
        # explaining the site
        links = self.browser.find_elements_by_tag_name('a')
        self.assertIn('log in', [link.text for link in links])
        self.assertIn('sign up', [link.text for link in links])
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome', header_text)

        # He clicks register and is redirected to a register page
        next(link.click() for link in links if link.text == 'sign up')

        # He inputs a username, an email, and a password and clicks register
        inputbox = self.browser.find_element_by_id('id_username')
        inputbox.send_keys('gustav_55')
        inputbox = self.browser.find_element_by_id('id_password1')
        inputbox.send_keys('iheartbees')
        inputbox = self.browser.find_element_by_id('id_password2')
        inputbox.send_keys('iheartbees')
        self.browser.find_element_by_tag_name('button').click()

        # Gustav is redirected to the classifier page. # On the classifier
        # page he is invited to Create a new classifier by a button
        self.fail('Complete the test!')

        # Clicking the create new classifier button, he is redirected to a category page

        # On the category page, he sees an input field to name the classifier and names
        # it 'My Classifier'

        # He sees another input field with an add category button next to it

        # He types in 'happy' in the category and clicks add category. It adds it
        # to the page below the input field.

        # He types in 'sad' and clicks add category and it adds another category

        # Satisfied he clicks 'Next' and is redirected to the text sample input page

        # Here he sees an explaintion asking him to 'Input text to train the model'
        # above a text input field along with a category dropdown box.

        # He enters in the text "I'm feeling happy today" and selects happy in the
        # drop down box. He then clicks "Submit" and the form is submitted.

        # He sees the page update with a counter now saying happy samples: 1

        # He enters in the text "Today is terrible" and selects sad in the dropdown
        # box. He then clicks submit.

        # He sees the page update again and now the counter says
        # happy samples: 1, sad samples: 1

        # Satisfied, he clicks "Done" and is redirected back to his Classifier page

        # Now he sees a new classifier on the page with the name "My Classifier" with two
        # links, "Add training data" and "Predict"

        # He clicks "Predict" and is taken to a new page

        # He sees a text field where he types in "I'm happy to see you" and clicks submit

        # The page returns a prediction
        # Can't guarantee the prediction will be happy due to the nature of modeling

        # Satisfied, he closes the browser.

if __name__ == '__main__':
    unittest.main()
