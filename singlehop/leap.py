from common import SingleHopError, SingleHopModule
try:
    import simplejson as json
except ImportError:
    import json

class AccountModule(SingleHopModule):
    """
    Account module to handle SingleHop account
    operations

    http://apiwiki.singlehop.com/index.php/Account_Module

    """
    def __init__(self, *args, **kwargs):
        super(AccountModule, self).__init__(module='account', *args, **kwargs)

    def get_account_details(self):
        """
        Gets account details

        """
        resp = self.do_request(command='getAccountDetails')
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def get_authorized_contacts(self):
        """
        Gets authorized accounts contacts

        """
        resp = self.do_request(command='getAuthorizedContacts')
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def tandem_list(self):
        """
        Gets list of Tandem users

        """
        resp = self.do_request(command='tandemList')
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def tandem_add_user(self, name=None, email=None, password=None):
        """
        Adds a new Tandem user

        :keyword name: First and last name of user
        :keyword email: Email address of user
        :keyword password: Password of user

        """
        if not name or not email or not password:
            raise SingleHopError('You must specify a name, email, and password')
        data = {}
        data['name'] = name
        data['email'] = email
        data['password'] = password
        resp = self.do_request(command='tandemAddUser', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def tandem_delete_user(self, user_id=None):
        """
        Deletes a Tandem user

        **Currently unsupported by SingleHopAPI
        
        :keyword user_id: ID of user to delete
        
        """
        if not user_id:
            raise SingleHopError('You must specify a user_id')
        data = {}
        data['userid'] = user_id
        resp = self.do_request(command='tandemDeleteUser', data=data)
        try:
            return json.loads(resp.content)
        except:
            return resp.content

    def tandem_add_user_permission(self, user_id=None, server_id=None):
        """
        Grants user permission to server

        :keyword user_id: ID of user
        :keyword server_id: ID of server
        
        """
        if not user_id or not server_id:
            raise SingleHopError('You must specify a user_id and server_id')
        data = {}
        data['userid'] = user_id
        data['serverid'] = server_id
        resp = self.do_request(command='tandemAddUserPermission', data=data)
        try:
            return json.loads(resp.content)
        except:
            return resp.content

    def tandem_delete_user_permission(self, user_id=None, server_id=None):
        """
        Removes user permission from server

        :keyword user_id: ID of user
        :keyword server_id: ID of server
        
        """
        if not user_id or not server_id:
            raise SingleHopError('You must specify a user_id and server_id')
        data = {}
        data['userid'] = user_id
        data['serverid'] = server_id
        resp = self.do_request(command='tandemDeleteUserPermission', data=data)
        try:
            return json.loads(resp.content)
        except:
            return resp.content

