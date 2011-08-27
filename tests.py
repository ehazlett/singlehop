import unittest
from random import Random
import string
from singlehop.common import SingleHopError, SingleHopModule
from singlehop import settings
from singlehop.leap import AccountModule

class TestSingleHopModule(unittest.TestCase):
    pass

class TestAccountModule(unittest.TestCase):
    def setUp(self):
        self.am = AccountModule()
        self._testuser = 'shTESTUSER123'

    def test_init(self):
        self.assertEqual(self.am.module, 'account')

    def test_get_account_details(self):
        resp = self.am.get_account_details()
        self.assertNotEqual(resp, None)
        self.assertTrue(isinstance(resp, dict))
        if resp.has_key('error'):
            self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
            self.assertTrue(resp['error'].find('No Such Command') == -1)

    def test_get_authorized_contacts(self):
        resp = self.am.get_authorized_contacts()
        self.assertNotEqual(resp, None)
        self.assertTrue(isinstance(resp, dict))
        if resp.has_key('error'):
            self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
            self.assertTrue(resp['error'].find('No Such Command') == -1)

    def test_tandem_list(self):
        resp = self.am.tandem_list()
        self.assertNotEqual(resp, None)
        self.assertTrue(isinstance(resp, dict))
        if resp.has_key('error'):
            self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
            self.assertTrue(resp['error'].find('No Such Command') == -1)

    def test_tandem_add_user(self):
        user = self._testuser
        email = 'user@sample.com'
        password = user
        resp = self.am.tandem_add_user(user, email, password)
        self.assertNotEqual(resp, None)
        self.assertTrue(isinstance(resp, dict))
        if resp.has_key('error'):
            self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
            self.assertTrue(resp['error'].find('No Such Command') == -1)

    def test_tandem_delete_user(self):
        '''Currently doesn't work with SingleHopAPI'''
        resp = self.am.tandem_delete_user(self._testuser)
        self.assertNotEqual(resp, None)
        self.assertTrue(isinstance(resp, dict))
        if resp.has_key('error'):
            self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
            self.assertTrue(resp['error'].find('No Such Command') == -1)

    def tandem_add_user_permission(self):
        #TODO: in order to test, this must have a server id
        #server_id = None
        #resp = self.am.tandem_add_user_permission(self._testuser, server_id)
        #self.assertNotEqual(resp, None)
        #self.assertTrue(isinstance(resp, dict))
        #if resp.has_key('error'):
        #    self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
        #    self.assertTrue(resp['error'].find('No Such Command') == -1)
        pass

    def tandem_delete_user_permission(self):
        #TODO: in order to test, this must have a server id
        #server_id = None
        #resp = self.am.tandem_delete_user_permission(self._testuser, server_id)
        #self.assertNotEqual(resp, None)
        #self.assertTrue(isinstance(resp, dict))
        #if resp.has_key('error'):
        #    self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
        #    self.assertTrue(resp['error'].find('No Such Command') == -1)
        pass



if __name__=='__main__':
    unittest.main()
