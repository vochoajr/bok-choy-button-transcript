# -*- coding: utf-8 -*-
import re
from bok_choy.page_object import PageObject


class EdXStudioSignInPage(PageObject):
    """
    edX Studio's Sign In page
    """

    url = 'https://edx-studio.iblstudios.com/container/block-v1:edX+DemoX+Demo_Course+type@vertical+block@2114a4dd8bbf4abfa6dde506281c00a5'

    def is_browser_on_page(self):
        return "sign in" in self.browser.title.lower()

    def enter_username(self, text):
        """
        Fill the text into input fields
        """

        self.q(css='#login_form input[type="email"]').fill(text)

    def enter_password(self, text):
        """
        Fill the text into input fields
        """

        self.q(css='#login_form input[type="password"]').fill(text)

    def login(self):
        """
        Click on the Sign In button and wait for the
        Unit page to be displayed
        """
        self.q(css='button').click()
        EdXStudioUnitPage(self.browser).wait_for_page()  #goto_edit()

    def login_enter_info(self, username, password):
        """
        Fill in the log in info and click the
        Sign In button
        """
        self.enter_username(username)
        self.enter_password(password)
        self.login()

class EdXStudioUnitPage(PageObject):
    """
    edX Studio's Unit page
    """

    # You do not navigate to this page directly
    url = None

    def is_browser_on_page(self):
        return "unit" in self.browser.title.lower()

    '''
    def goto_edit(self):
        """
        Click on the Edit button and wait for the
        Edit page to load
        """
        self.q(css='action-item.action-edit').click()
        EdXStudioEditPage(self.browser).wait_for_page()
    '''

'''
class EdXStudioEditPage(PageObject):
    """
    edX Studio's Unit Edit page
    """

    # You do not navigate to this page directly
    url = None

    def is_browser_on_page(self):
        print("here")
        return true
    
'''
