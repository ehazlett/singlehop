import unittest
from random import Random
import string
from singlehop.common import SingleHopError, SingleHopModule
from singlehop import settings
from singlehop.leap import AccountModule, ServerModule

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
        ''' *** Currently doesn't work in the SingleHopAPI'''
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

class TestServerModule(unittest.TestCase):
    def setUp(self):
        self.srvm = ServerModule()

    def test_list_servers(self):
        resp = self.srvm.list_servers()
        self.assertNotEqual(resp, None)
        self.assertTrue(isinstance(resp, dict))
        if resp.has_key('error'):
            self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
            self.assertTrue(resp['error'].find('No Such Command') == -1)

    def test_get_server_details(self):
        ''' *** Currently doesn't work in the SingleHopAPI'''
        resp = self.srvm.list_servers()
        srvs = resp['servers']
        if len(srvs) > 0:
            srv_id = srvs[0]['server_id']
            resp = self.srvm.get_server_details(srv_id)
            self.assertTrue(isinstance(resp, dict))
            if resp.has_key('error'):
                self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
                self.assertTrue(resp['error'].find('No Such Command') == -1)
        else:
            print('You must have a server to test getting details')
        
    def test_get_server_ips(self):
        resp = self.srvm.list_servers()
        srvs = resp['servers']
        if len(srvs) > 0:
            srv_id = srvs[0]['server_id']
            resp = self.srvm.get_server_ips(srv_id)
            self.assertTrue(isinstance(resp, dict))
            if resp.has_key('error'):
                self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
                self.assertTrue(resp['error'].find('No Such Command') == -1)
        else:
            print('You must have a server to test getting details')
        
    def test_get_server_bandwidth(self):
        resp = self.srvm.list_servers()
        srvs = resp['servers']
        if len(srvs) > 0:
            srv_id = srvs[0]['server_id']
            resp = self.srvm.get_server_bandwidth(srv_id)
            self.assertTrue(isinstance(resp, dict))
            if resp.has_key('error'):
                self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
                self.assertTrue(resp['error'].find('No Such Command') == -1)
        else:
            print('You must have a server to test getting details')
        
    def test_get_rdns_list(self):
        resp = self.srvm.list_servers()
        srvs = resp['servers']
        if len(srvs) > 0:
            srv_id = srvs[0]['server_id']
            resp = self.srvm.get_rdns_list(srv_id)
            if resp != None:
                self.assertTrue(isinstance(resp, dict))
                if resp.has_key('error'):
                    self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
                    self.assertTrue(resp['error'].find('No Such Command') == -1)
        else:
            print('You must have a server to test getting details')
        
    def test_get_os_list(self):
        resp = self.srvm.list_servers()
        srvs = resp['servers']
        if len(srvs) > 0:
            srv_id = srvs[0]['server_id']
            resp = self.srvm.get_os_list(srv_id)
            self.assertTrue(isinstance(resp, dict))
            if resp.has_key('error'):
                self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
                self.assertTrue(resp['error'].find('No Such Command') == -1)
        else:
            print('You must have a server to test getting details')

    def test_list_available_servers(self):
        resp = self.srvm.list_available_servers()
        self.assertNotEqual(resp, None)
        self.assertTrue(isinstance(resp, dict))
        if resp.has_key('error'):
            self.assertTrue(resp['error'].find('JSON Decoding error') == -1)
            self.assertTrue(resp['error'].find('No Such Command') == -1)


if __name__=='__main__':
    unittest.main()
