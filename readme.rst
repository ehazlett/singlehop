Python SingleHop API
---------------------

This is a Python API wrapper around the SingleHop (http://www.singlehop.com) LEAP API.

Configuration
================

Create a `local_settings.py` file (or edit `settings.py`) in the `singlehop` directory with the following:

    API_KEY = '<SINGLEHOP_API_KEY>'

    CLIENT_ID = '<SINGLEHOP_CLIENT_ID>'

    PASSWORD = '<SINGLEHOP_PASSWORD>'


Modules
--------

SingleHop separates their API into modules based on functionality (i.e. Account, Billing, Support, Server).

AccountModule
==============

The account module is used to access SingleHop account data:

    >>> from singlehop.leap import AccountModule
    >>> am = AccountModule()
    >>> am.get_account_details()

    {'data': {'city': 'Anytown', 'fax': 'business #:123-456-7890', 'last': 'Hazlett', 'zip': '12345', 'country': 'US', 'company': 'Acme', 'clientid': 123456, 'phone': '123-456-7890', 'state': 'IN', 'address': '123 Anywhere', 'email': 'user@email.com', 'first': 'Evan'}, 'success': True}
    
    >>> am.tandem_add_user('New User', 'user@email.com', 's3cr3+p@ss')
    
    {'success': True}

ServerModule
============

The server module is used for working with dedicated as well as Cascade servers:

    >>> from singlehop.leap import ServerModule
    >>> sm = ServerModule()
    >>> sm.list_servers()
    
    {'success': True, 'servers': [{'server_id': '000001', 'type': 'vmnode', 'server': 'host1.domain.com'}, {'parent_id': '000001', 'server_id': '123456', 'type': 'vm', 'server': 'vm.domain.com'} }
    
    >>> sm.list_available_servers()
    
    [{'name': 'Supercharged S-L5410 Single Processor ', 'maxdrives': '2', 'orders_server_id': '22', 'price': '249', 'ram': '6GB (Included)', 'harddrive': '250GB Enterprise Hard Drive', 'bandwidth': '5,000GB', 'hdid': '19', 'processor': 'Intel Xeon Quad-Core Harpertown LV 5410 2.33GHz 12MB Cache', 'realname': 'Supercharged S-L5410 Single Processor Dedicated Server'}]
    
    >>> sm.cascade_list_snapshots()
    
    [{'name': 'CentOS 5.6 32Bit', 'arch': 'i386', 'price': 0, 'cpanel': '0', 'os': 'centos', 'id': '68'},  {'name': 'Standard Debian 64Bit', 'arch': 'amd64', 'price': 0, 'cpanel': '0', 'os': 'debian', 'id': '4'}]

    >>> sm.cascade_reboot_vm('123456')

    {'message': 'VM rebooted', 'result': 'ok', 'success': True}


