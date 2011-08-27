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

        ** Currently unsupported by SingleHopAPI

        Error: Call to undefined method MDB2_Error::fetchOne() in <b>/home/leap/lib/class/Tandem.class.php</b> on line <b>30</b>
        
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

class ServerModule(SingleHopModule):
    """
    Server module to handle SingleHop server
    operations

    http://apiwiki.singlehop.com/index.php/Server_Module

    """
    def __init__(self, *args, **kwargs):
        super(ServerModule, self).__init__(module='server', *args, **kwargs)

    def list_servers(self):
        """
        Gets list of servers

        """
        resp = self.do_request(command='listServers')
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def get_server_details(self, server_id=None):
        """
        Gets the details of the specified server

        ** Currently doesn't work with SingleHop API:

        Error: Call to undefined method Cascade::getFreeStorage() in <b>/home/leap/lib/class/Api.class.php</b> on line <b>624</b>

        :keyword server_id: ID of server

        """
        if not server_id:
            raise SingleHopError('You must specify a server_id')
        data = {}
        data['serverid'] = server_id
        resp = self.do_request(command='getServerDetails', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def get_server_ips(self, server_id=None):
        """
        Gets list of allocated IPs for specified server

        :keyword server_id: ID of server

        """
        if not server_id:
            raise SingleHopError('You must specify a server_id')
        data = {}
        data['serverid'] = server_id
        resp = self.do_request(command='getServerIps', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def get_server_bandwidth(self, server_id=None):
        """
        Gets bandwidth totals for specified server

        :keyword server_id: ID of server

        """
        if not server_id:
            raise SingleHopError('You must specify a server_id')
        data = {}
        data['serverid'] = server_id
        resp = self.do_request(command='getServerBandwidth', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def get_rdns_list(self, server_id=None):
        """
        Gets list of Reverse DNS entries for specified server

        :keyword server_id: ID of server

        """
        if not server_id:
            raise SingleHopError('You must specify a server_id')
        data = {}
        data['serverid'] = server_id
        resp = self.do_request(command='getRdnsList', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)
    
    def update_rdns(self, entries=None):
        """
        Updates Reverse DNS entries for an assigned IP

        :keyword entries: Dict of IP/host pairs

        """
        if not server_id or not entries:
            raise SingleHopError('You must specify a server_id and entries')
        resp = self.do_request(command='updateRdns', data=entries)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)
    
    def reboot_server(self, server_id=None):
        """
        Reboots the specified server

        :keyword server_id: ID of server

        """
        if not server_id:
            raise SingleHopError('You must specify a server_id')
        data = {}
        data['serverid'] = server_id
        resp = self.do_request(command='rebootServer', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def get_os_list(self, server_id=None):
        """
        Gets the list of operating systems available for installation

        :keyword server_id: ID of server

        """
        if not server_id:
            raise SingleHopError('You must specify a server_id')
        data = {}
        data['serverid'] = server_id
        resp = self.do_request(command='getOsList', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def reinstall_server(self, server_id=None, os_id=None):
        """
        Reinstalls the specified server with the specified OS id

        :keyword server_id: ID of server
        :keyword os_id: ID of operating system to install

        """
        if not server_id or not os_id:
            raise SingleHopError('You must specify a server_id and os_id')
        data = {}
        data['serverid'] = server_id
        data['osid'] = os_id
        resp = self.do_request(command='reinstallServer', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)
    
    def list_available_servers(self):
        """
        Lists servers available for purchase

        """
        resp = self.do_request(command='listAvailableServers')
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

