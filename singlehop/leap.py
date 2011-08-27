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

    def cancellation_request(self, servers=None, happy=None, reason=None):
        """
        Submit a cancellation request

        :keyword servers: List of server IDs to cancel
        :keyword happy: Satified with service or not
        :keyword reason: Reason for cancellation.  Avaialable options:
             Going out of buisness, Financial Reasons, Client Cancelled,
             Do not need a server, Service Interruptions,
             Support was not what I expected, Unsatisfied with price

        """
        if not servers or happy == None or not reason:
            raise SingleHopError('You must specify a server_id, happy, and reason')
        data = {}
        data['servers'] = servers
        data['happy'] = happy
        data['reason'] = reason
        resp = self.do_request(command='cancellationRequest', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)
    
    def cascade_get_cpu_usage(self, server_id=None):
        """
        Gets CPU usage of specified Cascade VM

        :keyword server_id: ID of server

        """
        if not server_id:
            raise SingleHopError('You must specify a server_id')
        data = {}
        data['serverid'] = server_id
        resp = self.do_request(command='cascadeGetCpuUsage', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def cascade_get_node_properties(self, server_id=None):
        """
        Get information about a Cascade host node

        ** Currently doesn't work with SingleHop API:

        Error: Call to undefined method Cascade::getFreeStorage() in <b>/home/leap/lib/class/Api.class.php</b> on line <b>624</b>

        :keyword server_id: ID of server

        """
        if not server_id:
            raise SingleHopError('You must specify a server_id')
        data = {}
        data['serverid'] = server_id
        resp = self.do_request(command='cascadeGetNodeProperties', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def cascade_list_snapshots(self):
        """
        Lists available operating system snapshots

        """
        resp = self.do_request(command='cascadeListSnapshots')
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def cascade_edit_vm(self, vm_id=None, hostname=None, ram=None, storage=None, \
        cpu=None, vcpu=None, password=None):
        """
        Edits specified Cascade VM

        :keyword vm_id: ID of virtual machine to edit
        :keyword hostname: (optional) Hostname of vm ; must be unique
        :keyword ram: (optional) Ram size in bytes
        :keyword storage: (optional) Storage size in bytes
        :keyword cpu: (optional) CPU priority, 1-100
        :keyword vcpu: (optional) Number of virtual cpus to create, 0-16
        :keyword password: (optional) Root password of VM

        """
        if not vm_id:
            raise SingleHopError('You must specify a vm_id')
        data = {}
        data['vmid'] = vm_id
        if hostname:
            data['hostname'] = hostname
        if ram:
            data['ram'] = ram
        if storage:
            data['storage'] = storage
        if cpu:
            data['cpu'] = cpu
        if vcpu:
            data['vcpu'] = vcpu
        if password:
            data['password'] = password
        resp = self.do_request(command='cascadeEditVm', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)
    
    def cascade_move_vm(self, vm_id=None, server_id=None):
        """
        Migrates a Cascade VM to another host

        * Only Canopy VMs can be migrated and target server must have
        enough free RAM to accomodate the VM

        :keyword vm_id: ID of virtual machine
        :keyword server_id: ID of server

        """
        if not vm_id or not server_id:
            raise SingleHopError('You must specify a vm_id and server_id')
        data = {}
        data['vmid'] = vm_id
        data['serverid'] = server_id
        resp = self.do_request(command='cascadeMoveVm', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def cascade_create_vm(self, server_id=None, hostname=None, os=None, ram=None, \
        storage=None, cpu=None, vcpu=None, ips=None, imgstore=None):
        """
        Creates a new Cascade VM

        :keyword server_id: ID of host node
        :keyword hostname: Hostname of vm ; must be unique
        :keyword os: ID of operating system to use (can be obtained from cascade_list_snapshots)
        :keyword ram: Ram size in bytes
        :keyword storage: Storage size in bytes
        :keyword cpu: CPU priority, 1-100
        :keyword vcpu: Number of virtual cpus to create, 0-16
        :keyword ips: IP block size (30, 29, 28)
        :keyword imgstore: Storage type (canopy, local)

        """
        if not server_id or not hostname or not os or not ram or not storage \
            or not cpu or not vcpu or not ips or not imgstore:
            raise SingleHopError("""You must specify a server_id, hostname, os, ram, """\
                """storage, cpu, vcpu, ips, and imgstore""")
        data = {}
        data['serverid'] = server_id
        data['hostname'] = hostname
        data['os'] = os
        data['ram'] = ram
        data['storage'] = storage
        data['cpu'] = cpu
        data['vcpu'] = vcpu
        data['ips'] = ips
        data['imgstore'] = imgstore
        resp = self.do_request(command='cascadeCreateVm', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def cascade_snapshot_vm(self, vm_id=None, image_id=None):
        """
        Creates a new OS snapshot image

        :keyword vm_id: ID of virtual machine
        :keyword image_id: (optional) ID of image to overwrite

        """
        if not vm_id:
            raise SingleHopError('You must specify a vm_id')
        data = {}
        data['vmid'] = vm_id
        if image_id:
            data['imageid'] = image_id
        resp = self.do_request(command='cascadeSnapshotVm', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def cascade_delete_vm(self, vm_id=None):
        """
        Deletes a Cascade virtual machine

        :keyword vm_id: ID of virtual machine

        """
        if not vm_id:
            raise SingleHopError('You must specify a vm_id')
        data = {}
        data['vmid'] = vm_id
        resp = self.do_request(command='cascadeDeleteVm', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def cascade_reboot_vm(self, vm_id=None):
        """
        Reboots a Cascade virtual machine

        :keyword vm_id: ID of virtual machine

        """
        if not vm_id:
            raise SingleHopError('You must specify a vm_id')
        data = {}
        data['vmid'] = vm_id
        resp = self.do_request(command='cascadeRebootVm', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)

    def cascade_shutdown_vm(self, vm_id=None):
        """
        Shuts down a Cascade virtual machine

        :keyword vm_id: ID of virtual machine

        """
        if not vm_id:
            raise SingleHopError('You must specify a vm_id')
        data = {}
        data['vmid'] = vm_id
        resp = self.do_request(command='cascadeShutdownVm', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)
    
    def cascade_start_vm(self, vm_id=None):
        """
        Starts a Cascade virtual machine

        :keyword vm_id: ID of virtual machine

        """
        if not vm_id:
            raise SingleHopError('You must specify a vm_id')
        data = {}
        data['vmid'] = vm_id
        resp = self.do_request(command='cascadeStartVm', data=data)
        try:
            return json.loads(resp.content)
        except:
            data = {}
            data['data'] = resp.content
            return json.loads(data)
    
