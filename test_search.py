import unittest
from bok_choy.web_app_test import WebAppTest
from pages import EdXStudioSignInPage, EdXStudioUnitPage#, EdXStudioEditPage


class TestEdXStudio(WebAppTest):
    """
    Tests for the edX Studio site.
    """

    def setUp(self):
        """
        Instantiate the page object.
        """
        super(TestEdXStudio, self).setUp()
        self.edxstudio_signin_page = EdXStudioSignInPage(self.browser)
        
    '''
    def test_page_existence(self):
        """
        Make sure that the page is accessible.
        """
        self.edxstudio_signin_page.visit()
    '''
    def test_login(self):
        """
        Make sure that you can search for something.
        """
        self.edxstudio_signin_page.visit().login_enter_info('vicente.ochoa@nyu.edu', '****')
        


if __name__ == '__main__':
    unittest.main()
